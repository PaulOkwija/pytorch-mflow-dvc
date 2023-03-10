import argparse, shutil, zipfile, os, glob


def get_data(source):
    
    destination = '../data/raw'

    print('Copying image files...')
    import glob, os, shutil

    files = glob.iglob(os.path.join(source, "*).png"))
    # print("{} images found in folder".format(len(list(files))))
    for f in files:
        if os.path.isfile(f):
            shutil.copy(f, destination)
    # shutil.copytree(source, destination)

    # with zipfile.ZipFile(source, 'r') as zip_ref:
    #     zip_ref.extractall('../data/raw')

    # os.remove(destination)
    print('{} images extracted'.format(len(os.listdir('../data/raw'))))
    print('Images copied and extracted to:','../data/raw')
    print("Done!")

if __name__ == '__main__':
    # Obtain image data path from the Command Line Interface (CLI)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path", "-dp", type=str, dest="data_path",
        required=True, help="collect data and put it in raw folder."
        )
    args = parser.parse_args()
    source = args.data_path
    get_data(source)