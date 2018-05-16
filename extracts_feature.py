# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
==========================================
Feature Selection, Classification
==========================================

"""

import pandas as pd
import numpy as np
import math
import scipy
import csv
import pylab
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load the accelerator raw data

COLUMNS = ['time','x_axis', 'y_axis', 'z_axis']
walking = pd.read_csv('./data/cane_data/walking_slowly.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
walk = pd.read_csv('./data/cane_data/walking_normal.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
# slow = pd.read_csv('./data/cane_data/walking_very_slow.txt', delimiter = ',', header= None, names = COLUMNS)[:3000]
# vibrate = pd.read_csv('./data/cane_data/vibrations.txt', delimiter = ',', header= None, names = COLUMNS)[:3000]



#
# # # Compute the SMA(signal magnitude area)
activity = [walk, walking]
def sma(activity):

  X = activity['x_axis'] * activity['x_axis']
  Y = activity['y_axis'] * activity['y_axis']
  Z = activity['z_axis'] * activity['z_axis']
  mag = X + Y + Z
  sma = mag.apply(lambda x: math.sqrt(x))



#  Filtering the signal using low pass

  fc = 0.1
  b = 0.08
  N = int(np.ceil((4 / b)))
  if not N % 2: N += 1
  n = np.arange(N)
  sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
  window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
  sinc_func = sinc_func * window
  sinc_func = sinc_func / np.sum(sinc_func)
  sma = np.convolve(sma, sinc_func)
  return sma

#walks = sma(walking)
# plt.plot(walkings)
# plt.show()
# with open('./datas/sitting.csv', 'w') as file:
#   f = csv.writer(file)
#   f.writerow(sitting)


# Originally from http://stackoverflow.com/a/6891772/125507

def stft(x, fftsize=256, overlap=2):
    hop = fftsize / overlap
    w = scipy.hanning(fftsize + 1)[:-1]

    return np.array([np.fft.rfft(w * x[i:i + fftsize]) for i in range(0, len(x) - fftsize, hop)])

# Extract the Energy Feauture
energy_signal = []

for i in range(0, len(activity)):
    stft_signal = stft(sma(activity[i]))
#
    for k, amp in enumerate(stft_signal):
        energy_signal.append(np.sum(np.power(abs(stft_signal[k] ), 2)))



# Extract all feauture for every activities

def feature(x, fftsize=256, overlap=2):
    meanamp = []
    maxamp = []
    minamp = []
    stdamp = []
    energyamp = []
    hop = fftsize / overlap
    for i in range(0, len(x) - fftsize, hop):
        meanamp.append(np.array(np.mean(x[i:i + fftsize])))
        maxamp.append(np.array(np.max(x[i:i + fftsize])))
        minamp.append(np.array(np.min(x[i:i + fftsize])))
        stdamp.append(np.array(np.std(x[i:i + fftsize])))
        energyamp.append(np.array(np.sum(np.power(x[i:i + fftsize], 2))))

    return meanamp, maxamp, minamp, stdamp, energyamp
for i in range(0,len(activity)):
    valmean ,valmax,valmin,valstd,valenergy = feature(sma(activity[i]))
# Save the extrcted feature as csv

for i ,val in enumerate(valmean):
        saveFile = open ('./data/walk.csv','a')
        saveFile.write(str(i) + ',' + str(valmean[i]) + ',' +str(valmax[i]) + ',' + str(valmin[i]) + ','
                    + str(valstd[i]) + ',' + str(valenergy[i])+','+ str(energy_signal[i]))
        saveFile.write('\n')
