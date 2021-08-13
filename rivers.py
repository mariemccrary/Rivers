#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:18:17 2021

@author: mariemccrary
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.dates import (DateFormatter, MonthLocator, DayLocator)
import matplotlib.dates as mdates
import matplotlib.ticker as ticker



# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 

# Read temperatures
d = pd.read_csv("Mackenzie.csv", header=8, parse_dates=[2], index_col=[2]) 
df = pd.DataFrame(data=d)
# Drop the unit row
df=df.drop([df.index[0]])

# Convert to float
df['Temp'] = df['Temp'].astype(float, errors = 'raise')
df['Discharge'] = df['Discharge'].astype(float, errors = 'raise')

df.index = pd.to_datetime(df.index)

# Read discharge
df_M= pd.read_excel('discharge_data.xlsx', sheet_name='Mackenzie')


### Plot with matplotlib###


fig, ax1 = plt.subplots(figsize=(14,6))
color = 'tab:red'

ax1.set_ylabel('Temperature', color=color)
ax1 = df['Temp'].plot(color='red')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Discharge ($m^3$/s)', color=color)  # we already handled the x-label with ax1
ax2 = df['Discharge'].plot()
ax2.tick_params(axis='y', labelcolor=color)

date_form = DateFormatter("%b %Y")
ax2.xaxis.set_major_formatter(date_form)


fig.tight_layout() # otherwise the right y-label is slightly clipped
plt.show()


## Plot with Pandas ##

axleft = df['Temp'].plot(figsize=(15,6), title='Mackenzie River')
axright = df['Discharge'].plot(secondary_y=True, alpha=0.5)

axleft.set_xticklabels(df.index, rotation=45, ha='right')
date_form = DateFormatter("%b %Y")
axleft.xaxis.set_major_formatter(date_form)
ticklocations = mdates.MonthLocator()
ax2.xaxis.set_major_locator(ticklocations)


axleft.set_ylabel('Temperature (C)', color='blue');
axright.set_ylabel('Discharge ($m^3$/s)', color='orange');

fig.tight_layout() # otherwise the right y-label is slightly clipped
plt.show()






