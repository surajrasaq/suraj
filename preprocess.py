# Author Surajudeen Abdulrasaq
# University of Lyon/University Jean Monnet France

"""
Here we pre-process our data for de-noising and
compute the sma....
===============================================
Filtering and computing sma of accelerator
Am using low-pass filtering, maybe we can
try kalman or high-pass in future
===============================================

"""

import numpy as np
import pandas as pd
import math
from matplotlib import  pyplot as plt

# Load the accelerator data

COLUMNS = ['Time','X_axis', 'Y_axis', 'Z_axis']
# IN_THE_OFFICE = pd.read_csv('./data/sitting_offic.txt', sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Standing  = np.loadtxt('./data/standing.txt',delimiter =',',unpack =True)
# INDOOR = pd.read_csv('./data/indoor.txt', sep = ',',header = None, names= COLUMNS, low_memory=False)[:2000]
# WALK_TRAM2OFFICE = pd.read_csv('./data/walk_Tram2office.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# IN_THE_TRAM = pd.read_csv('./data/in_the_tram.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# CLIMB = pd.read_csv('./data/stair_climb.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Decend = pd.read_csv('./data/stair_decend.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
slow = pd.read_csv('./data/slow_walking.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Football = pd.read_csv('./data/football.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]

#Filtering the data with low pass filtering

#plt.plot(Slow_walk)

def filter(activity):
    fc = 0.1
    b = 0.08
    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1
    n = np.arange(N)
    sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
    window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    sinc_func = sinc_func * window
    sinc_func = sinc_func / np.sum(sinc_func)

    x1 = list(activity['X_axis'])

    x2 = list(activity['Y_axis'])

    x3 = list(activity['Z_axis'])

    new_signal1 = np.convolve(x1, sinc_func)
    new_signal2 = np.convolve(x2, sinc_func)
    new_signal3 = np.convolve(x3, sinc_func)

#Compute the SMA
    X = new_signal1 * new_signal1
    Y = new_signal2 * new_signal2
    Z = new_signal3 * new_signal3
    mag = X + Y + Z
    sma = np.sqrt(mag)
    return  sma

#Compute the SMA
def temm(act):
    X = act['X_axis'] * act['X_axis']
    Y = act['Y_axis'] * act['Y_axis']
    Z = act['Z_axis'] * act['Z_axis']
    mag = X + Y + Z
    sma = np.sqrt(mag)
    return  sma
#
no_filter = temm(slow)
filters = filter(slow)
#
img = [no_filter, filters]
titles = ['Slow walking before Filtering','Slow_ walking after Filtering ' ]
for i in range(0,len(img)):
    plt.plot(img[i])
    plt.title(titles[i])
    plt.show()

# Ploting each axis...(un_Comments the lines below if you want 2 visualise the signal on all the 3-axis after filtering)
#
#     signalist = [new_signal1, new_signal2, new_signal3]
#     titles = ['X_axis', 'Y_axis', 'Z_axis']
#     for i in range(0,len(signalist)):
#         plt.plot(signalist[i])
#         plt.title(titles[i])
#         plt.show()
#     return new_signal1, new_signal2, new_signal3
# filter(Slow_walk)


# VISUALIZE THE SIGNAL MAGNITUDE AREA (uncomment to plot the Signal magnitude Area)
#
# Slow_walk = temp(slow)

#print(Slow_walk)

#print(pd(Climbing_Stair.head()))





