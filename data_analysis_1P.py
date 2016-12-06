#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author: Jason Schenck
Date 12/04/16
"Should I Buy This Stock?" Workshop 1 Excercise 1 (Tentative)
Data Analysis with Python and Pandas

Practice example: I will collect data from the Yahoo finance API for a 38 years..period on one of the stocks in my portfolio (AMD),store the data in a dataframe, and then experiment with output of both the dataframe, stat functions, and a visualization chart.

Sites of interest:
http://pandas.pydata.org/pandas-docs/version/0.15.2/remote_data.html (List of Pandas Stock APIs)
http://pandas.pydata.org/pandas-docs/version/0.15.2/basics.html (Descriptive Statistics Functions)
"""

import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt 

"""
Retrieve Data & Build Dataframe
"""

# Data date range 38 years: January 6th 78' - 2016
start = datetime.datetime(1978, 1, 6)
end = datetime.datetime(2016, 12, 2)

# Building a dataframe of historical stock data on AMD, from Google API, between 1996-2016 
df = web.DataReader("AMD", "yahoo", start, end)


"""
Output testing
"""

# Print dataframe
("**************----Dataframe----**************")
print(df, "\n")


# Print first 5 rows (head) Short sweet and to the point..
print("************----Dataframe Head----************")
print(df.head(), "\n")


# The data has been provided/stored with the most recent date first, however
# we need the data to be sorted from oldest to newest, let's fix that.
#df.sort()



""" 
Analysis, Observation, & Manipulation
"""

print("************----Descriptive Statistics----************")
print(df.describe(), "\n")



# AMD's stocks MODES for each column value (most repetitive over 38 years)
# @param 0 -> mode of all elements across x-axis
# @param 1 -> mode of all elements across y-axis
print("************----AMD's Mode----************")
print(df.mode(0), "\n")



""" 
Data Visualization (Charts, graphs, plots, tables, etc)    
"""
# One of the most simple and basic data visualization charts is a histogram which visually depicts the frequency distribution for a particular attribute. Probabilities are often estimated from these charts. I will create a histogram for the close price. The close price is often a strong indicator of decision making in stock investments.

# Aesthetics:
# Size : should be about roughly 1.33x wider than taller
plt.figure(figsize=(12, 9))

# Frame line borders, remove them 
ax = plt.subplot(111)  
ax.spines["top"].set_visible(False)  
ax.spines["right"].set_visible(False)

# Axis ticks location, display only for left and bottom of chart    
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()  

# Axis ticks size, default tick size is typically too small
# we can simply increase the size a bit to improve clarity
plt.xticks(fontsize=14)  
plt.yticks(fontsize=14)  

# Axis labels size, should be only a bit larger than axis tick labels
plt.xlabel("AMD Stock Close Price", fontsize=16)  
plt.ylabel("Frequency", fontsize=16) 

# OK. Let's feed in the values for our data, along with color, and num bins
plt.hist(list(df.Close.values),  
         color="#3F5D7D", bins=100)  


# Save the chart/graph as an image for reference outside of the console
plt.savefig("AMD_START_YR.png", bbox_inches="tight");  

# Another graph, simple line graph, close price over time (entire 20 year span)
plt.figure(figsize=(14, 9))
plt.ylabel("Price", fontsize=16)
df['Close'].plot(figsize=(16, 12))

#Output dataframe to CSV for use with Glue
df.to_csv('amdstock.csv', sep='\t')


