import os
import shutil


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Python_Files": [".py"],
    "Compressed": [".zip", ".rar", ".7z"],
}


def get_category(file_extension):
    """
    Return the folder category based on file extension.
    If extension is not found, return 'Others'.
    """
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def organize_folder(folder_path):
    """
    Organize files in the given folder according to file type.
    """
    if not os.path.exists(folder_path):
        print("Error: Folder path does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: The given path is not a folder.")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        source_path = os.path.join(folder_path, filename)

        if os.path.isdir(source_path):
            continue

        _, file_extension = os.path.splitext(filename)
        category = get_category(file_extension)

        destination_folder = os.path.join(folder_path, category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, filename)

        try:
            shutil.move(source_path, destination_path)
            files_moved += 1
            print(f"Moved: {filename} -> {category}")
        except Exception as error:
            print(f"Could not move {filename}: {error}")

    print(f"\nOrganization completed. Total files moved: {files_moved}")


def main():
    print("Python File Organizer")
    print("---------------------")

    folder_path = input("Enter the folder path you want to organize: ").strip()
    organize_folder(folder_path)


if __name__ == "__main__":
    main()
