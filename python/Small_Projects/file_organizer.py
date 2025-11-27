import os
import shutil

# 1️⃣ Folder categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json"],
    "Installers": [".exe", ".msi", ".dmg"],
    "Others": []  # fallback for uncategorized files
}


def organise_file(source_folder):
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        category = "Others"
        for cat, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                category = cat
                break

        new_folder = os.path.join(source_folder, category)
        os.makedirs(new_folder, exist_ok=True)

        new_path = os.path.join(new_folder, file_name)

        shutil.move(file_path, new_path)


source_folder = input("Enter the source folder: ")
organise_file(source_folder)
