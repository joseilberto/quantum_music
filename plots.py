import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.abspath('..'))
from processors.processors import get_arguments

def plot_zipf(song_name, method):
    if not song_name:
        print('Enter a song name with -s parameter')
    frequency_data = '{}/{}_estatisticas/frequency_data.csv'.format(method, song_name)
    df = pd.read_csv(frequency_data, sep = ',')
    f, ax = plt.subplots(figsize = (7,7))
    ax.set(xscale='log', yscale='log')
    plot = sns.regplot('k', 'n(k)', df, ax=ax, scatter_kws={'s': 100}, fit_reg=False)
    plot.get_figure().savefig('{}/{}_zipf.eps'.format(method, song_name))

def plot_hh(song_name, method):
    summary_data = '{}/data_summary.csv'.format(method)
    df = pd.read_csv(summary_data, sep=',')
    f, ax = plt.subplots(figsize = (7,7))
    ax.set(xscale='log', yscale='log')
    plot = sns.regplot('N', 'T', df, ax=ax, scatter_kws={'s': 100}, fit_reg=False)
    plot.get_figure().savefig('{}/herdan-heaps.eps'.format(method))

def plot_bars(song_name, method):
    if not song_name:
        print('Enter a song name with -s parameter')
    os.makedirs('{}/{}_bar_code/plots'.format(method, song_name), exist_ok=True)
    for file1 in os.listdir('{}/{}_bar_code/'.format(method, song_name)):
        if file1.endswith('.csv'):
            make_bar_plot('{}/{}_bar_code/'.format(method, song_name) + file1)

def make_bar_plot(file1):
    df = pd.read_csv(file1, sep=',')
    len_df = len(df['pos'])
    if len_df > 0:
        plt.rcParams.update({'figure.max_open_warning': 0})
        f, ax = plt.subplots(figsize = (7,7))
        out_file = file1.replace('_code/', '_code/plots/')
        for idx, position in enumerate(df['pos']):
            ax.plot([position, position], [0, 1], 'k')
        plt.savefig(out_file.replace('.csv', '.eps'))
        plt.clf()


params = [['h', 's', 'p', 'm'], ["song=","plot="], ['song_name', 'zipf'], ['method=', 'distancia_musical']]
song_name, plot_type, method = get_arguments(params)
if 'zipf' in plot_type:
    plot_zipf(song_name, method)
elif 'herdan-heaps' in plot_type:
    plot_hh(song_name, method)
elif 'bar_code' in plot_type:
    plot_bars(song_name, method)
else:
    print('Plot not yet implemented.')
