import os
import glob
import yaml
import pandas as pd
import mlflow 
import sys
sys.path.append('src/')

from utils.mlflow_run_decorator import mlflow_run


@mlflow_run
def make_csv_path(excluded_labels=None):

    # List all the images in raw/ 
    # list_images = glob.glob('./data/external/**/*.jpg', recursive=True)
    df = pd.read_csv('./data/external/Breast_cancer_dataset.csv')
    # df['label'] = df['path'].apply(lambda x:os.path.basename(os.path.dirname(x)))
    print(df.shape)

    # Do we filter certain classes ? 
    # if excluded_labels is not None:
    #     df = df[~df['label'].isin(excluded_labels)]
    #     print('Csv file constituted with {nrows} images, representing {nclasses} classes, excluding {exclusion}'.format(
    #     nrows=df.shape[0],
    #     nclasses=len(df['label'].unique()),
    #     exclusion= ', '.join(excluded_labels)
    #     ))
    # else:
    #     print('Csv file constituted with {nrows} images, representing the {nclasses} classes'.format(
    #         nrows=df.shape[0],
    #         nclasses=len(df['label'].unique())
    #     ))
    
    mlflow.log_param("excluded_classes", excluded_labels)
    # Converting classes to number 
    labels = df['class'].unique()
    labels.sort()
    labels_map = {label:i for i, label in enumerate(labels)}
    df['y'] = df['class'].map(labels_map)
    
    # Saving the map numbers -> label
    # os.mkdir('data/processed')
    labels_map_save = {i:label for i, label in enumerate(labels)}
    with open("./data/processed/labels_map.yaml", "w") as outfile:
        yaml.dump(labels_map_save, outfile)

        
if __name__ == '__main__':
    
    # Read params
    params = yaml.safe_load(open('./params.yaml'))['prepare']
    excluded_classes = params['excluded_classes']
    # Exclude class
    make_csv_path(excluded_labels=excluded_classes)
