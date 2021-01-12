import os
from PIL import Image

inputpath = "insert/the/path/to/your/highquality/images"
outputpath = "insert/the/path/to/your/highquality/images"

verbose = False
optimization = True
quality = 30
minimum_size = 1000000  # Bytes


def main():
    for dirpath, dirnames, filenames in os.walk(inputpath):
        structure = os.path.join(outputpath, os.path.relpath(dirpath, inputpath))
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            if verbose:
                print("This folder already exists")

    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(inputpath) for f in filenames]
    for file in result:
        if os.stat(file).st_size > minimum_size:
            file_name = file.split(os.sep)[-1]
            path_after_folder = file.replace(inputpath, "")
            print(path_after_folder)
            print(f"compressing {file_name}")
            if os.path.exists(outputpath + os.sep + path_after_folder):
                print("This file has already been processed.")
                continue
            try:
                image = Image.open(file)
                image.save(outputpath + os.sep + path_after_folder, optimize=optimization, quality=quality)
                print(f"The image {file_name} has been correctly processed.")
            except IOError:
                print(f"The file {file_name} is not an image.")

    print()
    print("Finished!)")


if __name__ == '__main__':
    main()
