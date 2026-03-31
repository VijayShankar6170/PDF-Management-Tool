import os
import shutil
import hashlib
from send2trash import send2trash

# ==============================
# CONFIG (CHANGE THESE PATHS)
# ==============================
SOURCE_FOLDER = r"C:\Users\Lenovo\Documents"
TARGET_FOLDER = r"D:\All PDFs"


# ==============================
# SCAN FOR PDF FILES
# ==============================
def find_pdfs(root_dir):
    pdf_files = []
    for folder, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(folder, file))
    return pdf_files


# ==============================
# GET SUBFOLDER NAME (A-Z)
# ==============================
def get_subfolder(filename):
    first_char = filename[0].upper()
    return first_char if first_char.isalpha() else "Others"


# ==============================
# ORGANIZE INTO SUBFOLDERS
# ==============================
def organize_pdfs(pdf_list, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    copied = 0

    for file in pdf_list:
        filename = os.path.basename(file)

        subfolder = get_subfolder(filename)
        subfolder_path = os.path.join(target_folder, subfolder)

        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        destination = os.path.join(subfolder_path, filename)

        # Handle duplicate file names
        base, ext = os.path.splitext(filename)
        count = 1

        while os.path.exists(destination):
            new_name = f"{base}({count}){ext}"
            destination = os.path.join(subfolder_path, new_name)
            count += 1

        try:
            shutil.copy2(file, destination)
            copied += 1
        except Exception as e:
            print(f"Error copying {file}: {e}")

    print(f"\n✅ {copied} PDFs organized into A-Z folders")


# ==============================
# HASH FUNCTION
# ==============================
def file_hash(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None


# ==============================
# FIND DUPLICATES (GROUPED)
# ==============================
def find_duplicates(folder):
    hashes = {}

    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                path = os.path.join(root, file)
                h = file_hash(path)

                if h:
                    hashes.setdefault(h, []).append(path)

    duplicate_groups = [files for files in hashes.values() if len(files) > 1]
    return duplicate_groups


# ==============================
# MOVE DUPLICATES TO RECYCLE BIN
# ==============================
def delete_duplicates(folder):
    duplicate_groups = find_duplicates(folder)

    if not duplicate_groups:
        print("✅ No duplicates found.")
        return

    print("\n⚠️ Duplicate groups found:\n")

    total_duplicates = 0

    for group in duplicate_groups:
        print("Group:")
        for file in group:
            print(" -", file)
        print()

        total_duplicates += len(group) - 1

    print(f"Total duplicate files to move: {total_duplicates}")

    confirm = input("Move duplicates to Recycle Bin? (y/n): ")

    if confirm.lower() != "y":
        print("Cancelled.")
        return

    moved = 0

    for group in duplicate_groups:
        original = group[0]
        duplicates = group[1:]

        for file in duplicates:
            try:
                send2trash(file)  # SAFE DELETE
                print(f"Moved to Recycle Bin: {file}")
                moved += 1
            except Exception as e:
                print(f"Error moving {file}: {e}")

    print(f"\n🗑️ {moved} duplicate files moved to Recycle Bin.")


# ==============================
# SEARCH (RECURSIVE)
# ==============================
def search_pdfs(folder, keyword):
    results = []

    for root, _, files in os.walk(folder):
        for file in files:
            if keyword.lower() in file.lower():
                results.append(os.path.join(root, file))

    return results


# ==============================
# MENU
# ==============================
def menu():
    while True:
        print("\n========== PDF MANAGER ==========")
        print("1. Scan and organize PDFs (A-Z folders)")
        print("2. Search PDFs by name")
        print("3. Show duplicate PDFs")
        print("4. Move duplicates to Recycle Bin")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n🔍 Scanning for PDFs...")
            pdfs = find_pdfs(SOURCE_FOLDER)

            print(f"Found {len(pdfs)} PDF files")
            confirm = input("Organize into A-Z folders? (y/n): ")

            if confirm.lower() == "y":
                organize_pdfs(pdfs, TARGET_FOLDER)

        elif choice == "2":
            keyword = input("Enter keyword: ")
            results = search_pdfs(TARGET_FOLDER, keyword)

            if results:
                print("\n📄 Results:")
                for r in results:
                    print(" -", r)
            else:
                print("No files found.")

        elif choice == "3":
            groups = find_duplicates(TARGET_FOLDER)

            if groups:
                print("\n⚠️ Duplicate groups:\n")
                for g in groups:
                    for f in g:
                        print(" -", f)
                    print()
            else:
                print("✅ No duplicates found.")

        elif choice == "4":
            delete_duplicates(TARGET_FOLDER)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    menu()
