import os
import shutil

source = "source_folder"
destination = "destination_folder"

for file in os.listdir(source):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        shutil.move(os.path.join(source, file), destination)

print("Files moved successfully!")