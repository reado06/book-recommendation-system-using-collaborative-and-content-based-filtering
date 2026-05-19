import pickle
import os
import numpy as np


class HybridRecommender:
    """Hybrid recommender yang menggabungkan CF dan CBF"""

    def __init__(self, models_dir='models'):
        self.models_dir = models_dir
        self.loaded = False
        self.svd_model = None
        self.cosine_sim = None
        self.book_data = None
        self.rating_data = None
        self.indices = None

    def load_models(self):
        """Load semua pre-trained models dari folder models/"""
        try:
            with open(os.path.join(self.models_dir, 'svd_model.pkl'), 'rb') as f:
                self.svd_model = pickle.load(f)
            with open(os.path.join(self.models_dir, 'cosine_sim.pkl'), 'rb') as f:
                self.cosine_sim = pickle.load(f)
            with open(os.path.join(self.models_dir, 'book_data.pkl'), 'rb') as f:
                self.book_data = pickle.load(f)
            with open(os.path.join(self.models_dir, 'rating_data.pkl'), 'rb') as f:
                self.rating_data = pickle.load(f)
            with open(os.path.join(self.models_dir, 'indices.pkl'), 'rb') as f:
                self.indices = pickle.load(f)
            self.loaded = True
            print("✅ Semua model berhasil di-load!")
        except FileNotFoundError as e:
            print(f"❌ Model belum tersedia: {e}")
            print("   Jalankan notebook.ipynb terlebih dahulu untuk men-train dan export model.")
            self.loaded = False

    def get_popular_books(self, n=20):
        """Dapatkan buku populer berdasarkan rata-rata rating tertinggi"""
        if not self.loaded:
            return []

        avg_ratings = self.rating_data.groupby('ISBN').agg(
            avg_rating=('Book-Rating', 'mean'),
            count=('Book-Rating', 'count')
        ).reset_index()

        # Minimal 5 rating
        avg_ratings = avg_ratings[avg_ratings['count'] >= 5]
        avg_ratings = avg_ratings.sort_values('avg_rating', ascending=False).head(n)

        result = avg_ratings.merge(self.book_data, on='ISBN', how='inner')
        books = []
        for _, row in result.iterrows():
            books.append({
                'isbn': row['ISBN'],
                'title': row['Book-Title'],
                'author': row['Book-Author'],
                'year': int(row['Year-Of-Publication']),
                'avg_rating': round(row['avg_rating'], 2),
                'rating_count': int(row['count'])
            })
        return books

    def get_user_history(self, user_id):
        """Dapatkan histori rating user"""
        if not self.loaded:
            return []

        user_ratings = self.rating_data[self.rating_data['User-ID'] == user_id]
        if len(user_ratings) == 0:
            return []

        user_ratings = user_ratings.merge(self.book_data, on='ISBN', how='inner')
        user_ratings = user_ratings.sort_values('Book-Rating', ascending=False)

        history = []
        for _, row in user_ratings.iterrows():
            history.append({
                'isbn': row['ISBN'],
                'title': row['Book-Title'],
                'author': row['Book-Author'],
                'rating': int(row['Book-Rating'])
            })
        return history

    def hybrid_recommend(self, user_id, alpha=0.6, k=10):
        """
        Hybrid recommender: combine CF + CBF scores.
        alpha: bobot CF (0-1). Default 0.6 (CF lebih dominan)
        """
        if not self.loaded:
            return []

        rated_books = self.rating_data[self.rating_data['User-ID'] == user_id]

        # Cold start: return popular books
        if len(rated_books) == 0:
            return self.get_popular_books(k)

        rated_isbns = rated_books['ISBN'].values
        all_books = self.book_data['ISBN'].values
        unrated = [isbn for isbn in all_books if isbn not in rated_isbns]

        # CF scores
        cf_scores = {}
        for isbn in unrated:
            pred = self.svd_model.predict(user_id, isbn)
            cf_scores[isbn] = pred.est

        # Normalize CF to 0-1
        if cf_scores:
            cf_min, cf_max = min(cf_scores.values()), max(cf_scores.values())
            cf_range = cf_max - cf_min if cf_max != cf_min else 1
            cf_norm = {k: (v - cf_min) / cf_range for k, v in cf_scores.items()}
        else:
            cf_norm = {}

        # CBF scores
        top_rated = rated_books.nlargest(3, 'Book-Rating')
        cbf_scores = {}
        for _, row in top_rated.iterrows():
            title_match = self.book_data[self.book_data['ISBN'] == row['ISBN']]['Book-Title'].values
            if len(title_match) == 0 or title_match[0] not in self.indices:
                continue
            idx = self.indices[title_match[0]]
            import pandas as pd
            if type(idx) is pd.Series:
                idx = idx.iloc[0]
            sim = self.cosine_sim[idx]
            for i, score in enumerate(sim):
                book_isbn = self.book_data.iloc[i]['ISBN']
                if book_isbn not in rated_isbns:
                    cbf_scores[book_isbn] = max(cbf_scores.get(book_isbn, 0), score)

        # Combine
        hybrid = {}
        for isbn in unrated:
            cf = cf_norm.get(isbn, 0)
            cbf = cbf_scores.get(isbn, 0)
            hybrid[isbn] = alpha * cf + (1 - alpha) * cbf

        # Top-K
        sorted_books = sorted(hybrid.items(), key=lambda x: x[1], reverse=True)[:k]
        top_isbns = [b[0] for b in sorted_books]
        score_map = dict(sorted_books)

        result = self.book_data[self.book_data['ISBN'].isin(top_isbns)].copy()
        result['score'] = result['ISBN'].map(score_map)
        result = result.sort_values('score', ascending=False)

        recommendations = []
        for _, row in result.iterrows():
            recommendations.append({
                'isbn': row['ISBN'],
                'title': row['Book-Title'],
                'author': row['Book-Author'],
                'year': int(row['Year-Of-Publication']),
                'score': round(row['score'], 4)
            })
        return recommendations

    def get_all_user_ids(self):
        """Dapatkan semua user ID yang tersedia"""
        if not self.loaded:
            return []
        return sorted(self.rating_data['User-ID'].unique().tolist())
