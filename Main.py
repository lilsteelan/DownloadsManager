import sys
from os import scandir, rename
from os.path import splitext, exists
from shutil import move
from time import sleep
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = r"C:/Users/stell/Downloads"
dest_dir_music = r"C:/Users/stell/Downloads/Downloaded Audio"
dest_dir_video = r"C:/Users/stell/Downloads/Downloaded Videos"
dest_dir_image = r"C:/Users/stell/Downloads/Downloaded Images"
dest_dir_documents = r"C:/Users/stell/Downloads/Documents"

dest_dir_compressed = r"C:/Users/stell/Downloads/Zip and RAR files"
dest_dir_other = r"C:/Users/stell/Downloads/Miscellaneous"
dest_dir_presets = r"C:/Users/stell/Downloads/Downloaded Presets"
dest_dir_exe = r"C:/Users/stell/Downloads/Installers and Excecutables"
dest_dir_osu = r"C:/Users/stell/Downloads/Beatmaps and Skins"
dest_dir_folders = r"C:/Users/stell/Downloads/Random Folders"
programRuntime = 7

#Initialisation
if not os.path.exists(dest_dir_music):
    os.makedirs(dest_dir_music)

if not os.path.exists(dest_dir_video):
    os.makedirs(dest_dir_video)

if not os.path.exists(dest_dir_image):
    os.makedirs(dest_dir_image)

if not os.path.exists(dest_dir_documents):
    os.makedirs(dest_dir_documents)

if not os.path.exists(dest_dir_compressed):
    os.makedirs(dest_dir_compressed)

if not os.path.exists(dest_dir_other):
    os.makedirs(dest_dir_other)

if not os.path.exists(dest_dir_presets):
    os.makedirs(dest_dir_presets)

if not os.path.exists(dest_dir_exe):
    os.makedirs(dest_dir_exe)

if not os.path.exists(dest_dir_osu):
    os.makedirs(dest_dir_osu)

if not os.path.exists(dest_dir_folders):
    os.makedirs(dest_dir_folders)

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico", ".avif"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".rtf", ".txt"]

folder_exceptions = ["Random Folders", "Beatmaps and Skins", "Installers and Excecutables","Downloaded Presets", "Miscellaneous","Zip and RAR files",
                     "Documents", "Downloaded Images","Downloaded Videos","Downloaded Audio"]
compressed_extensions = [".zip", ".rar", ".7zip", ".7z"]
presets_extensions = [".ffx", ".setting"]
exe_extensions = [".exe", ".jar", ".msi"]
osu_extensions = [".osz", ".osk", ".osr"]

def move_file(path,dest):
    move(path, dest)

def check_audio_files(path, name):  # * Checks all Audio Files
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            move_file(path, dest_dir_music)
            logging.info(f"Moved audio file: {name}")

def check_video_files(path, name):  # * Checks all Video Files
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(path, dest_dir_video)
            logging.info(f"Moved video file: {name}")

def check_image_files(path, name):  # * Checks all Image Files
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(path, dest_dir_image)
            logging.info(f"Moved image file: {name}")

def check_document_files(path, name):  # * Checks all Document Files
    for documents_extension in document_extensions:
        if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
            move_file(path, dest_dir_documents)
            logging.info(f"Moved document file: {name}")

def check_compressed_files(path, name):  # * Checks all Compressed Files
    for compresseds_extension in compressed_extensions:
        if name.endswith(compresseds_extension) or name.endswith(compresseds_extension.upper()):
            move_file(path, dest_dir_compressed)
            logging.info(f"Moved compressed file: {name}")

def check_preset_files(path, name):  # * Checks all Preset Files
    for preset_extension in presets_extensions:
        if name.endswith(preset_extension) or name.endswith(preset_extension.upper()):
            move_file(path, dest_dir_presets)
            logging.info(f"Moved preset file: {name}")

def check_exe_files(path, name):  # * Checks all Exe Files
    for exe_extension in exe_extensions:
        if name.endswith(exe_extension):
            move_file(path, dest_dir_exe)
            logging.info(f"Moved exe file: {name}")

def check_osu_files(path, name):  # * Checks all Osu Files
    for osu_extension in osu_extensions:
        if name.endswith(osu_extension) or name.endswith(osu_extension.upper()):
            move_file(path, dest_dir_osu)
            logging.info(f"Moved osu file: {name}")

timeOfStartup = (round(time.time()))
print(timeOfStartup)
while True:
    if (timeOfStartup + programRuntime) > time.time():
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                path = entry.path
                print(path)
                if not os.path.exists(path):
                    check_osu_files(path, name)
                    check_audio_files(path, name)
                    check_video_files(path, name)
                    check_image_files(path, name)
                    check_document_files(path, name)
                    check_compressed_files(path, name)
                    check_preset_files(path, name)
                    check_exe_files(path, name)

                # To prevent main folders from moving
                else:
                    if name in folder_exceptions:
                        pass
                    else:
                        move_file(path, dest_dir_folders)
    #Timer ran out
    else:
        sys.exit()
