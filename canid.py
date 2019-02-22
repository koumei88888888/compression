#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

path_data = 'id_probability_levorg.csv'
output = 'canid_levorg.txt'

df = pd.read_csv(path_data, sep=",", names=("ID", "probability"))

df = df["ID"]
df.to_csv(output, header=False, index=False)