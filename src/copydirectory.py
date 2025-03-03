import shutil
import os

def copy_directory(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
        return
    
    for item in os.listdir(destination):
        item_path = os.path.join(destination, item)
        for item in os.listdir(destination):
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied {src_path} to {dest_path}")  # Placeholder for logging
        elif os.path.isdir(src_path):
            os.mkdir(dest_path)
            copy_directory(src_path, dest_path)  # Recursive call

             


    
    