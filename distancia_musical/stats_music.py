import numpy as np
import pandas as pd
from collections import Counter


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
def find_distances(note_counts, durations):
    distances = []
    for token, count in note_counts:
        positions = np.array([durations[i] for i in range(len(song['notes'])) if token == song['notes'][i] and count > 2])
        if np.count_nonzero(np.diff(positions)) != 0 and len(np.diff(positions)) > 0:
            distances.append([np.diff(positions), token])
    return np.array(distances)

#next three lines read the data and converts it to the format we want: C#88|duration
song = pd.read_csv('macarena_file_colunas.txt', sep = '\t', header = None)
song[0] = pd.Series([note[0] + note[2] + str(song[1][index]) if note[2] != ' ' else  note[0] + str(song[1][index]) for index, note in enumerate(song[0])])
del song[1]; song.columns = ['notes', 'duration']

note_counts = Counter(list(song['notes'])).most_common() #returns the notes and their counts
durations = np.array(song['duration'].cumsum()) #returns a np array with the durations

distances = find_distances(note_counts, durations) #returns the values and their counts
sigmas = find_sigma(distances[:, 0]) #finds all sigmas returning a pandas Series
entropies = find_entropy(distances[:, 0]) #finds all entropies returning a pandas Series

df_stats = pd.DataFrame({'note': pd.Series(distances[:, 1]), 'sigma': sigmas, 'entropy': entropies})
df_notes_stats = pd.DataFrame({'note': pd.Series(np.array(note_counts)[:, 0]), 'frequency': pd.Series(np.array(note_counts)[:, 1])})
df = pd.merge(df_stats, df_notes_stats, how = 'outer')
df.to_csv('maracena_estatistica.csv', index = False)
