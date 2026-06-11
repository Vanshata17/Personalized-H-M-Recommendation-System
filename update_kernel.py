import json

notebook_path = r"c:\Users\SUNIL KUMAR\Downloads\krish_naik\H_and_m\notebooks\1_fp_computing_features.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Display current kernel spec
print("Current kernelspec:")
print(json.dumps(nb.get('metadata', {}).get('kernelspec', {}), indent=2))

# Update kernel spec to python3
nb['metadata']['kernelspec'] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
}

# Update language info as well
if 'language_info' not in nb['metadata']:
    nb['metadata']['language_info'] = {}

nb['metadata']['language_info'] = {
    "name": "python",
    "version": "3.12.0",
    "mimetype": "text/x-python",
    "codemirror_mode": {
        "name": "ipython",
        "version": 3
    },
    "pygments_lexer": "ipython3",
    "nbconvert_exporter": "python",
    "file_extension": ".py"
}

print("\nNew kernelspec:")
print(json.dumps(nb['metadata']['kernelspec'], indent=2))

# Save the notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("\n✅ Notebook kernel updated to python3")
