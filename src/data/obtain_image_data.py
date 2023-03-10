import argparse, shutil, zipfile, os


def get_data(args):
    source = args.data_path
    destination = '../data/raw'

    print('Copying image files...')
    shutil.copy(source, destination)

    # with zipfile.ZipFile(source, 'r') as zip_ref:
    #     zip_ref.extractall('../data/raw')

    os.remove(destination)
    print('{} image folders extracted'.format(len(os.listdir('../data/raw'))))
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

    get_data(args)