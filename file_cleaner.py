#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import csv, sys, os
#
# path = './data/fit/'
#
# csv_day_files = [f for f in os.listdir(path) if (f.endswith('.csv') and f != "Résumés quotidiens.csv")]
#
# for csv_day_file in csv_day_files:
#     with open(path+csv_day_file,"rt") as source:
#         reader= csv.reader( source )
#         next(reader, None)  # skip the source headers
#         result_file = path+(csv_day_file.replace(".csv",""))+"-only-steps.csv" # create result file
#         with open(result_file,"wt") as result:
#             writer= csv.writer(result)
#             writer.writerow(("Begin date", "End date", "Number of steps")) # write result headers
#             for r in reader:
#                 writer.writerow((r[0], r[1], r[14]))
#     os.remove(path+csv_day_file) # remove original file

import pandas as pd
import glob, os

os.chdir('./data/fit/')
results = pd.DataFrame([])

for counter, file in enumerate(glob.glob("2016*")):
    namedf = pd.read_csv(file, skiprows=0, usecols=[0,1, 2])
    results = results.append(namedf)

results.to_csv('/home/suraj/PycharmProjects/Novin/datas/2016_steps.csv')
