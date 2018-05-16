import pandas as pd
import numpy as np
import math, csv
from matplotlib import pyplot as plt
import scipy.signal as signal


COLUMNS = ['time','x_axis', 'y_axis', 'z_axis']
sitting = np.loadtxt('./data/sitting_offic.txt', delimiter = ',', )[:3000]
standing= pd.read_csv('./data/standing.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
indoor = pd.read_csv('./data/indoor.txt',  delimiter = ',',  header= None, names = COLUMNS)[:3000]
walking = pd.read_csv('./data/walk_Tram2office.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
walk = pd.read_csv('./data/walk_Home2Tram_Station.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
tram = pd.read_csv('./data/in_the_tram.txt', delimiter = ',', header= None, names = COLUMNS)[:3000]
climbing= pd.read_csv('./data/stair_climb.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
decending = pd.read_csv('./data/stair_decend.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
slow_walk = pd.read_csv('./data/slow_walking.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
football = pd.read_csv('./data/football.txt',delimiter = ',',header= None, names = COLUMNS)[:3000]

N = 2  # Filter order
Wn = 0.01  # Cutoff frequency
B, A = signal.butter(N, Wn, output='ba')

sitting = signal.filtfilt(B, A, standing)


# plt.plot(walkings)
# plt.show()
with open('./datas/sitting.txt', 'w') as file:
  f = csv.writer(file)
  f.writerow(sitting)