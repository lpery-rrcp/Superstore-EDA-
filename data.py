import kagglehub
import shutil
import os

# Download dataset to KaggleHub cache
download_path = kagglehub.dataset_download(
    "vivek468/superstore-dataset-final"
)

print("Downloaded to:", download_path)

# Your project data folder
destination = r"D:\Projects_Python\Superstore_EDA\data"

os.makedirs(destination, exist_ok=True)

# Copy all files
for file in os.listdir(download_path):
    src = os.path.join(download_path, file)
    dst = os.path.join(destination, file)

    if os.path.isfile(src):
        shutil.copy2(src, dst)

print("Files copied to:", destination)
