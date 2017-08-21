import numpy as np
import pandas as pd
import os
import sys
from collections import Counter
sys.path.append(os.path.abspath('..'))
from stats_metrics import frequency_data, general_data
from processors.processors import get_arguments


#find sigmas for each note token
def find_sigma(distances):
    sigmas = []
    for token in distances:
        sigmas.append(np.std(token)/np.mean(token))
    return pd.Series(sigmas)


#find entropy for each note token
def find_entropy(distances):
    entropies = []
    for token in distances:
        unique_distances = np.unique(token, return_counts = True)[1]
        probs = unique_distances/np.sum(unique_distances)
        entropies.append(-np.sum(probs*np.log(probs)))
    return pd.Series(entropies)


#get the distances list for each note token ignoring notes with all zero distances
def find_distances(note_counts, durations, make_bar_code):
    distances = []
    for token, count in note_counts:
        positions = np.array([durations[i] for i in range(len(song['notes'])) if token == song['notes'][i] and count > 2])
        if make_bar_code:
            print_bar_code(dir_path, token, positions)
        if np.count_nonzero(np.diff(positions)) != 0 and len(np.diff(positions)) > 0:
            distances.append([np.diff(positions), token])
    return np.array(distances)


def print_bar_code(dir_path, token, positions):
    with open(dir_path + str(token) + '_bar_code.csv', 'w') as file1:
        print('pos,handler', file=file1)
        for pos in positions:
            print('{},{}'.format(pos, 1), file=file1)


params = [['h', 's', 'b'], ["song=","bar_code="], ['song_name', 'true/false']]
song_name, make_bar_code, _ = get_arguments(params)
make_bar_code = make_bar_code.lower() in ['true']

os.makedirs('{}_bar_code'.format(song_name), exist_ok=True)
dir_path = './{}_bar_code/'.format(song_name)

song = pd.read_csv('{}_file_colunas.txt'.format(song_name), sep = '\t', header = None)
song[0] = pd.Series([note[0] + note[2] + str(song[1][index]) if note[2] != ' ' else  note[0] + str(song[1][index]) for index, note in enumerate(song[0])])
del song[1]; song.columns = ['notes', 'duration']
song.dropna(axis=0, how='any')

frequency_data(song['notes'], song_name)
general_data(song['notes'], song_name)

durations = np.array(song['duration'].cumsum()) #returns a np array with the durations
note_counts = Counter(list(song['notes'])).most_common() # return the notes and respective counts
distances = find_distances(note_counts, durations, make_bar_code) #returns the values and their counts
sigmas = find_sigma(distances[:, 0]) #finds all sigmas returning a pandas Series
entropies = find_entropy(distances[:, 0]) #finds all entropies returning a pandas Series

df_stats = pd.DataFrame({'note': pd.Series(distances[:, 1]), 'sigma': sigmas, 'entropy': entropies})
df_notes_stats = pd.DataFrame({'note': pd.Series(np.array(note_counts)[:, 0]), 'frequency': pd.Series(np.array(note_counts)[:, 1])})
df = pd.merge(df_stats, df_notes_stats, how = 'outer')
df.to_csv('{}_estatistica.csv'.format(song_name), index = False)
