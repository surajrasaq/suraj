# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
==========================================
Feature Selection, Classification
==========================================

"""

import pandas as pd
import numpy as np
import scipy
import csv
from matplotlib import pyplot as plt

# Load the accelerator raw data

COLUMNS = ['time','x_axis', 'y_axis', 'z_axis']
zero = pd.read_csv('./step_data/walking_ 0step1.txt', delimiter = ',',  header= None, names = COLUMNS)[:5000]
ten = pd.read_csv('./step_data/walking_ 10step1.txt', delimiter = ',',  header= None, names = COLUMNS)[:5000]
twety8 = pd.read_csv('./step_data/walking_ 28step.txt',  delimiter = ',',  header= None, names = COLUMNS)[:5000]
hundred = pd.read_csv('./step_data/walking_100step.txt', delimiter = ',',  header= None, names = COLUMNS)[:5000]
sevtin = pd.read_csv('./step_data/walking_ 17step.txt', delimiter = ',',  header= None, names = COLUMNS)[:5000]
four50 = pd.read_csv('./step_data/walking_450step.txt', delimiter = ',', header= None, names = COLUMNS)[:5000]
# climbing= pd.read_csv('./data/stair_climb.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
# decending = pd.read_csv('./data/stair_decend.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
# slow_walk = pd.read_csv('./data/slow_walking.txt', delimiter = ',',  header= None, names = COLUMNS)[:3000]
# football = pd.read_csv('./data/football.txt',delimiter = ',',header= None, names = COLUMNS)[:3000]


# Compute the SMA(signal magnitude area)

def sma(activity):

  X = activity['x_axis'] * activity['x_axis']
  Y = activity['y_axis'] * activity['y_axis']
  Z = activity['z_axis'] * activity['z_axis']
  mag = X + Y + Z
  sma = np.sqrt(mag)

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

# plot each activity after De-noise -----TO DO---- or
#
activity = [zero, ten, twety8, hundred,sevtin, four50]
# titles = ['Slow_Walk', 'Normal_Work','Vibrating_arm','Sitting','Very_Slow_Walk','Walk_Stop',]
# for i in range(0, len(activity)):
#     plt.xlabel('Freq')
#     plt.ylabel('Energy')
#     plt.plot(sma(activity[i]))
#     plt.title(titles[i])
#     plt.show()

#Feature Extraction(Short Time Fourier Transform)

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

   # valmean ,valmax,valmin,valstd,valenergy = feature(sma(activity[i]))

# Save the extrcted feature as csv

for i in range(0, len((activity))):
    valmean, valmax, valmin, valstd, valenergy = feature(sma(activity[i]))

    for k ,val in enumerate(valmean):
            saveFile = open ('./step_data/walking_features.csv','a')
            saveFile.write(str(i) + ',' + str(valmean[k]) + ',' +str(valmax[k]) + ',' + str(valmin[k]) + ','
                    + str(valstd[k]) + ',' + str(valenergy[k])+','+ str(energy_signal[k]))
            saveFile.write('\n')

# with open('./data/Feat.csv', 'w') as out:
#   rows = csv.writer(out)
#   for i in range(0, len(sma(activity))):
#          for f in feature(sma(activity[i] + energy_signal[i])):
#             rows.writerow([i] + f)