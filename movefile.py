import os
import shutil

def move_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"The source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(source_folder)

    if not files:
        print("No items found in the folder.")
        return

    for file_name in files:
        if file_name.lower() == 'desktop.ini':
            continue
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name} to {destination_folder}")

if __name__ == "__main__":
    download_folder = ""
    downloadcorrect = ""
    screenshot = ""
    screenshotcorrect = ""
    recording = ""
    recordingcorrect = ""
    move_files(download_folder, downloadcorrect)
    move_files(screenshot, screenshotcorrect)
    move_files(recording, recordingcorrect)
