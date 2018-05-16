# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
==========================================
Data preparation to a single activity csv file
==========================================

"""
from functools import reduce
import  pandas as pd
#from preprocess import filter as f1

# Load the accelerator data

# COLUMNS = ['Time','X_axis', 'Y_axis', 'Z_axis']
# IN_THE_OFFICE = pd.read_csv('./data/sitting_offic.txt', sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Standing = pd.read_csv('./data/standing.txt', sep = ',',header = None, names= COLUMNS, low_memory=False)[:2000]
# INDOOR = pd.read_csv('./data/indoor.txt', sep = ',',header = None, names= COLUMNS, low_memory=False)[:2000]
# WALK_TRAM2OFFICE = pd.read_csv('./data/walk_Tram2office.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# IN_THE_TRAM = pd.read_csv('./data/in_the_tram.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# CLIMB = pd.read_csv('./data/stair_climb.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Decend = pd.read_csv('./data/stair_decend.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Slow_walk = pd.read_csv('./data/slow_walking.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]
# Football = pd.read_csv('./data/football.txt',sep = ',', header = None, names= COLUMNS, low_memory=False)[:2000]

# PRE-PROCESS RAW DATA BY DE-NOISE AND COMPUTING THE SMA (Signal Magnitude Area)

# Climbing_Stair = f1(CLIMB)
# Decending_Stair = f1(Decend)
# Walking = f1(WALK_TRAM2OFFICE)
# In_Tram = f1(IN_THE_TRAM)
# In_door = f1(INDOOR)
# Sitting = f1(IN_THE_OFFICE)
# Standing = f1(Standing)
# Slow_walk = f1(Slow_walk)
# Football = f1(Football)


#(un-comment below line to visualise any of the acvities after Pre-process)

# plt.plot(Standing)
# # plt.title('Walking from tram station 2 office')
# plt.show()

# Convert data in to frames and create a CSV FILES FROM DATA-FRAME
#
# Climbing_Stair = pd.DataFrame(Climbing_Stair)
# Climbing_Stair.to_csv('Climbing')
# Decending_Stair = pd.DataFrame(Decending_Stair)
# Decending_Stair.to_csv('Decending')
# Walking = pd.DataFrame(Walking)
# Walking.to_csv('Walking')
# In_Tram = pd.DataFrame(In_Tram)
# In_Tram.to_csv('Tram')
# In_door = pd.DataFrame(In_door)
# In_door.to_csv('Indoor')
# Sitting = pd.DataFrame(Sitting)
# Sitting.to_csv('Sitting')
# Standing = pd.DataFrame(Standing)
# Standing.to_csv('Standing')
# Football = pd.DataFrame(Football)
# Football.to_csv('Football')
# Slow_walk = pd.DataFrame(Slow_walk)
# Slow_walk.to_csv('Slow_walking')

# load the csv files and merge all to single csv...


df1 = pd.read_csv('./data/Climbing', header = None)[:2000]
df1.columns = ['index','Climbing']
df2 = pd.read_csv('./data/Decending',header = None)[:2000]
df2.columns = ['index','Decend']
df3 = pd.read_csv('./data/Walking',header = None)[:2000]
df3.columns = ['index','Walking']
df4 = pd.read_csv('./data/Tram', header = None)[:2000]
df4.columns = ['index','Tram']
df5 = pd.read_csv('./data/Indoor', header = None)[:2000]
df5.columns = ['index','Indoor']
df6 = pd.read_csv('./data/Sitting', header = None)[:2000]
df6.columns = ['index','Sitting']
df7 = pd.read_csv('./data/Standing', header = None)[:2000]
df7.columns = ['index','Standing']
df8 = pd.read_csv('./data/Slow_walking', header = None)[:2000]
df8.columns = ['index','Slow_walk']
df9 = pd.read_csv('./data/Football', header = None)[:2000]
df9.columns = ['index','Football']

act = [df1, df2, df3, df4, df5 ,df6, df7, df8, df9]

activity = reduce(lambda left, right: pd.merge(left,right), act)
#activity.set_index('count')
activity.to_csv('activity')

print(activity.head())



