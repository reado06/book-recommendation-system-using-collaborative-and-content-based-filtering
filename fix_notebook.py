import nbformat

with open("notebook.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

nb = nbformat.v4.new_notebook()
current_cell = []
current_type = "code"  # Start assuming first cell is code if no # %% is found

for line in lines:
    if line.startswith("# %%"):
        if current_cell:
            content = "".join(current_cell).strip("\n")
            if content:
                if current_type == "markdown":
                    # Remove "# " from markdown lines
                    clean_lines = []
                    for l in content.split("\n"):
                        if l.startswith("# "): clean_lines.append(l[2:])
                        elif l.startswith("#"): clean_lines.append(l[1:])
                        else: clean_lines.append(l)
                    nb.cells.append(nbformat.v4.new_markdown_cell("\n".join(clean_lines)))
                else:
                    nb.cells.append(nbformat.v4.new_code_cell(content))
        current_cell = []
        if "[markdown]" in line:
            current_type = "markdown"
        else:
            current_type = "code"
    else:
        current_cell.append(line)

# Flush the last cell
if current_cell:
    content = "".join(current_cell).strip("\n")
    if content:
        if current_type == "markdown":
            clean_lines = []
            for l in content.split("\n"):
                if l.startswith("# "): clean_lines.append(l[2:])
                elif l.startswith("#"): clean_lines.append(l[1:])
                else: clean_lines.append(l)
            nb.cells.append(nbformat.v4.new_markdown_cell("\n".join(clean_lines)))
        else:
            nb.cells.append(nbformat.v4.new_code_cell(content))

with open("notebook.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook successfully synced from notebook.py!")
