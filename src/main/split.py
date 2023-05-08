import pandas as pd
import numpy as np
import glob
import os
import re

def check_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def split(file_name,input_dir, output_dir, split_size = 4):
    df = pd.read_csv(f'{input_dir}/{file_name}.csv', low_memory=False)
    parts = np.array_split(df, split_size)

    dir = f"{output_dir}/{file_name}"
    check_dir(dir)

    for i, part in enumerate(parts):
        part.to_csv(
            f'{output_dir}/{file_name}/{file_name}_part_{i}.csv', index=False)


def main(isTest=False):
    if not isTest:
        INPUT_DIR = 'resources/input'
        OUTPUT_DIR = 'resources/output'


        files = list(x for x in glob.glob(f'{INPUT_DIR}/*.csv') if not os.path.isdir(x))

        regex = fr'{INPUT_DIR}\\|\.csv'
        files = list(map(lambda x: re.sub(regex, '', x), files))

        for file in files:
            split(file, INPUT_DIR, OUTPUT_DIR)
            print(file)
    else:
        INPUT_DIR = 'resources/test/input'
        OUTPUT_DIR = 'resources/test/output'
        
        files = list(x for x in glob.glob(f'{INPUT_DIR}/*.csv') if not os.path.isdir(x))

        regex = fr'{INPUT_DIR}\\|\.csv'
        files = list(map(lambda x: re.sub(regex, '', x), files))

        for file in files:
            split(file, INPUT_DIR, OUTPUT_DIR)
            print(file)
