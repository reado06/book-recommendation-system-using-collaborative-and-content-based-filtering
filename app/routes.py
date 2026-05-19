from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Homepage - menampilkan buku populer dan form input User ID"""
    from . import recommender

    popular_books = recommender.get_popular_books(12)
    return render_template('index.html', popular_books=popular_books)


@main.route('/recommend', methods=['GET', 'POST'])
def recommend():
    """Halaman rekomendasi personal berdasarkan User ID"""
    from . import recommender

    if request.method == 'POST':
        user_id = request.form.get('user_id', '').strip()
        if user_id:
            try:
                user_id = int(user_id)
                return redirect(url_for('main.recommend', user_id=user_id))
            except ValueError:
                pass

    user_id = request.args.get('user_id', type=int)

    if user_id is None:
        return redirect(url_for('main.index'))

    # Dapatkan rekomendasi dan histori user
    recommendations = recommender.hybrid_recommend(user_id, alpha=0.6, k=10)
    history = recommender.get_user_history(user_id)

    return render_template(
        'recommend.html',
        user_id=user_id,
        recommendations=recommendations,
        history=history[:10]  # Tampilkan max 10 histori
    )
