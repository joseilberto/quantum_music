import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from processors.processors import get_arguments

def plot_zipf(song_name):
    frequency_data = '{}_estatisticas/frequency_data.csv'.format(song_name)
    df = pd.read_csv(frequency_data, sep = ',')
    f, ax = plt.subplots(figsize = (7,7))
    ax.set(xscale='log', yscale='log')
    plot = sns.regplot('k', 'n(k)', df, ax=ax, scatter_kws={'s': 100}, fit_reg=False)
    plot.get_figure().savefig('{}_zipf.eps'.format(song_name))

def plot_hh(song_name):
    summary_data = 'data_summary.csv'
    df = pd.read_csv(summary_data, sep=',')
    f, ax = plt.subplots(figsize = (7,7))
    ax.set(xscale='log', yscale='log')    
    plot = sns.regplot('N', 'T', df, ax=ax, scatter_kws={'s': 100}, fit_reg=False)
    plot.get_figure().savefig('herdan-heaps.eps')


params = [['h', 's', 'p'], ["song=","plot="], ['song_name', 'zipf']]
song_name, plot_type = get_arguments(params)
if 'zipf' in plot_type:
    plot_zipf(song_name)
elif 'herdan-heaps' in plot_type:
    plot_hh(song_name)
else:
    print('Plot not yet implemented.')
