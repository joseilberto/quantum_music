import numpy as np
import pandas as pd
import os
from collections import Counter


def frequency_data(notes, song_name):
    os.makedirs('{}_estatisticas'.format(song_name), exist_ok=True)
    dir_path = './{}_estatisticas/'.format(song_name)
    with open(dir_path + 'frequency_data.csv', 'w') as file1:
        print('k,n(k)', file=file1)
        zipf_dict = Counter(Counter(notes).values())
        for freq in zipf_dict.keys():
            print('{},{}'.format(freq, zipf_dict[freq]), file=file1)
