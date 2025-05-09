import os

base_dir = "plant_disease_flask_app"

# Folders to create
folders = [
    "templates",
    "static/uploads",
    "model"
]

# Files to create (with path relative to base_dir)
files = [
    "app.py",
    "utils.py",
    "requirements.txt",
    "README.md",
    "templates/index.html"
]

# Create base directory
os.makedirs(base_dir, exist_ok=True)

# Create subfolders
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Create empty files
for file in files:
    file_path = os.path.join(base_dir, file)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure parent dirs exist
    with open(file_path, 'w') as f:
        f.write("")

print("✅ Flask project structure and files created successfully.")
