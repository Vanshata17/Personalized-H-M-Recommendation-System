import json

notebook_path = r"C:\Users\SUNIL KUMAR\Downloads\krish_naik\H_and_m\notebooks\1_fp_computing_features.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find and fix the install_dependencies function
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'def install_dependencies' in source and '!pip install' in source:
            # Found the cell, now modify it
            new_source = [
                "def install_dependencies() -> None:\n",
                "    # !pip install --upgrade uv\n",
                "    # !uv pip install --all-extras --system --requirement pyproject.toml\n",
                "    pass\n"
            ]
            cell['source'] = new_source
            print("✅ Fixed notebook 1")
            break

# Save the notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("✅ Notebook 1 saved")
