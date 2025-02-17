import os

def rename_files_in_folder(folder_path, project_name):
    try:
        # Get the list of files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        if not files:
            print("No files found in the provided folder.")
            return
        
        print(f"Found {len(files)} files in the folder.")
        
        for index, file in enumerate(files, start=1):
            file_extension = os.path.splitext(file)[1]  # Get the file extension
            new_name = f"{project_name}({index}){file_extension}"
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
        
        print("Renaming completed successfully.".encode('utf-8').decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder containing the files: ").strip()
    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        project_name = input("Enter the project name: ").strip()
        rename_files_in_folder(folder_path, project_name)
    else:
        print("The provided folder does not exist or is not valid.")
