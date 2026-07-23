import os
import shutil

# ------------------------------------------------------------
# CONFIGURATION — change these two paths to match your setup.
# ------------------------------------------------------------
SOURCE_FOLDER = "source_images"        # folder to scan for .jpg files
DESTINATION_FOLDER = "sorted_jpgs"     # folder they'll be moved into

# File extensions we're treating as "jpg" (covers both spellings).
JPG_EXTENSIONS = (".jpg", ".jpeg")


def find_jpg_files(folder):
    """
    Return a list of filenames in `folder` that end in .jpg or .jpeg
    (case-insensitive), ignoring subfolders — only files directly
    inside this folder are considered.
    """
    jpg_files = []
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if os.path.isfile(full_path) and filename.lower().endswith(JPG_EXTENSIONS):
            jpg_files.append(filename)
    return jpg_files


def get_unique_destination_path(destination_folder, filename):
    """
    If a file with this name already exists in the destination folder,
    add a number (1), (2), etc. to the new filename instead of
    silently overwriting an existing photo.
    """
    destination_path = os.path.join(destination_folder, filename)

    if not os.path.exists(destination_path):
        return destination_path

    name, extension = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name} ({counter}){extension}"
        new_path = os.path.join(destination_folder, new_filename)
        if not os.path.exists(new_path):
            return new_path
        counter += 1


def move_jpg_files(source_folder, destination_folder):
    if not os.path.isdir(source_folder):
        print(f"Source folder '{source_folder}' doesn't exist. Nothing to do.")
        return

    # Create the destination folder if it doesn't already exist.
    os.makedirs(destination_folder, exist_ok=True)

    jpg_files = find_jpg_files(source_folder)

    if not jpg_files:
        print(f"No .jpg or .jpeg files found in '{source_folder}'.")
        return

    print(f"Found {len(jpg_files)} image(s) in '{source_folder}':")

    moved_count = 0
    for filename in jpg_files:
        source_path = os.path.join(source_folder, filename)
        destination_path = get_unique_destination_path(destination_folder, filename)

        shutil.move(source_path, destination_path)
        print(f"  Moved: {filename} -> {destination_path}")
        moved_count += 1

    print(f"\nDone. Moved {moved_count} file(s) to '{destination_folder}'.")


if __name__ == "__main__":
    move_jpg_files(SOURCE_FOLDER, DESTINATION_FOLDER)