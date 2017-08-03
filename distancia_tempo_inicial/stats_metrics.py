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

def general_data(notes, song_name):
    summary_file = 'data_summary.csv'
    verify_summary(summary_file, song_name)
    with open(summary_file, 'a') as file1:
        print('{},{},{},{}'.format(*get_summary(notes), song_name), file=file1)

def verify_summary(summary_file, song_name):
    """
    Faz duas verificações:
    1 - Verifica se o arquivo de resumo já foi criado.
    2 - Verifica se a música já possui dados no arquivo e os deleta.
    """
    summary_fields = ['T', 'N', 'kmax', 'song']
    if not os.path.isfile(summary_file):
        with open(summary_file, 'w') as file1:
            print('{},{},{},{}'.format(*summary_fields), file=file1)
    else:
        with open(summary_file, 'r') as file1:
            lines = file1.readlines()
        with open(summary_file, 'w') as file1:
            for line in lines:
                if song_name not in line:
                    file1.write(line)

def get_summary(notes):
    T = len(notes)
    V = len(set(notes))
    k_max = Counter(notes).most_common()[0][1]
    return T, V, k_max
