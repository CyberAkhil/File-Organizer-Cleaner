import os
import shutil

FOLDER_PATH = input("Enter folder path to organize: ")

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
}


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def organize_files():
    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    create_folder(os.path.join(FOLDER_PATH, folder))
                    shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))
                    moved = True
                    break

            if not moved:
                create_folder(os.path.join(FOLDER_PATH, "Others"))
                shutil.move(file_path, os.path.join(FOLDER_PATH, "Others", file))


organize_files()
print("Files organized successfully.")
