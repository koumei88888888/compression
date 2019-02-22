#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

path_data = 'revorg_moving_log_5min.csv'
output = 'revorg_moving_log_5min_2.csv'

df = pd.read_csv(path_data, sep=",", names=("Time","Ch","Protocol","Dir","Label","State","Type","Format","ID","DL","D1","D2","D3","D4","D5","D6","D7","D8","Sum"))

Time = df["Time"]
ID = df["ID"]
DATA = df[["D1","D2","D3","D4","D5","D6","D7","D8"]]
df = pd.concat([ID, DATA], axis=1)
#df = pd.concat([Time, ID, DATA], axis=1)
#df = df[["Time", "ID", "D1","D2","D3","D4","D5","D6","D7","D8"]]
df.to_csv(output, header=False, index=False)