import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from collections import Counter, OrderedDict

def find_sigma(distances):
    sigmas = []
    for token in distances:
        sigmas.append(np.std(token)/np.mean(token))
    return pd.Series(sigmas)

def find_entropy(distances):
    entropies = []
    for token in distances:
        unique_distances = np.unique(token, return_counts = True)[1]
        probs = unique_distances/np.sum(unique_distances)
        entropies.append(-np.sum(probs*np.log(probs)))
    return pd.Series(entropies)

def find_distances(note_counts, initial, dir_path):
    distances = []
    for token, count in note_counts:
        positions = np.array([initial[i] for i in range(len(song['notes'])) if token == song['notes'][i] and count > 2])
        if count > 2: print_bar_code(positions, dir_path, token)
        if np.count_nonzero(np.diff(positions)) != 0 and len(np.diff(positions)) > 0:
            distances.append([np.diff(positions), token])
    return np.array(distances)

def print_bar_code(positions, dir_path, token):
    df = pd.DataFrame({'positions': pd.Series(positions), 'v1col': pd.Series([1]*len(positions))})
    df.to_csv('{}/{}_bar_code.dat'.format(dir_path, token), sep = '\t', index = False, header = False)

def clear_channel(note):
    return ''.join([char for char in note if char != ' ' and not char.isdigit()])

def intensity_handler(song):
    song_notes = []
    distances = []
    for index, note in enumerate(song['notes']):
        for index2, note2 in enumerate(song['notes']):
            if index > index2 and note == note2:
                song_notes.append(note + '_' + str(abs(song['intensity'][index2] - song['intensity'][index])))
                break
    return pd.Series(song_notes)

song_name = 'macarena'; os.makedirs('{}_bar_code'.format(song_name), exist_ok=True); dir_path = './{}_bar_code'.format(song_name)
song = pd.read_csv('{}_file_colunas_novo.txt'.format(song_name), sep = '\t', header = None)
song[0] = pd.Series([clear_channel(note) + str(song[3][index]) for index, note in enumerate(song[0])]) #clear the numbering in notes and append the channel value to it
del song[2]; del song[3]; song.columns = ['notes', 'initial', 'intensity'] #delete unnecessary columns from df and rename the columns
song = song.sort_values('initial'); song = song.reset_index(drop = True) #sort values and reset the indeces
song['notes'] = intensity_handler(song); del song['intensity'] #handle the intensity differences and remove intensity column once it is done

note_counts = Counter(list(song['notes'])).most_common() #returns the notes and their counts
distances = find_distances(note_counts, song['initial'], dir_path) #returns the values and their counts
sigmas = find_sigma(distances[:, 0]) #finds all sigmas returning a pandas Series
entropies = find_entropy(distances[:, 0]) #finds all entropies returning a pandas Series
df_stats = pd.DataFrame({'note': pd.Series(distances[:, 1]), 'sigma': sigmas, 'entropy': entropies})
df_notes_stats = pd.DataFrame({'note': pd.Series(np.array(note_counts)[:, 0]), 'frequency': pd.Series(np.array(note_counts)[:, 1])})
df = pd.merge(df_stats, df_notes_stats, how = 'outer')
df.to_csv('{}_estatistica_novo.csv'.format(song_name), index = False)
