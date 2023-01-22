import math
import os, sys, glob
import re
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import datetime
import csv
import japanize_matplotlib

file_name = '/Users/mac10/Desktop/stock/data' + datetime.datetime.now().strftime('%Y-%m-%d')

data1 = []
data2 = []
data3 = []
data4 = []

with open(file_name + '-08-45.csv') as f1:
  for row1 in csv.reader(f1):
    data1.append(row1)
with open(file_name + '-08-50.csv') as f2:
  for row1 in csv.reader(f2):
    data2.append(row1)
with open(file_name + '-08-55.csv') as f3:
  for row1 in csv.reader(f3):
    data3.append(row1)
with open(file_name + '-08-57.csv') as f4:
  for row1 in csv.reader(f4):
    data4.append(row1)

#data[0]はそれぞれのタイトル

time_transition = ['45','50','55','57']
fig1, axes1 = plt.subplots(10,10,figsize=(20, 14), dpi=100, facecolor='w', linewidth=0, edgecolor='w')

i = 0
for ax_row1 in axes1:
  j = 0
  for ax1 in ax_row1:
    ax2 = ax1.twinx()
    #ax4 = ax3.twinx()
    """
    if i+j+k+1 == select_num[0] or i+j+k+1 == select_num[1] or i+j+k+1 == select_num[2]:
      ax3.plot(time_transition,[int(data1[i+j+k+1][3]),int(data2[i+j+k+1][3]),int(data3[i+j+k+1][3]),int(data4[i+j+k+1][3])],marker = "o",label='over',color='b')
      ax3.plot(time_transition,[int(data1[i+j+k+1][4]),int(data2[i+j+k+1][4]),int(data3[i+j+k+1][4]),int(data4[i+j+k+1][4])],marker = "o",label='under',color='r')
      ax4.plot(time_transition,[int(data1[i+j+k+1][5]),int(data2[i+j+k+1][5]),int(data3[i+j+k+1][5]),int(data4[i+j+k+1][5])],marker = "o",label='offer',color='cyan',linestyle = "dashdot")
      ax4.plot(time_transition,[int(data1[i+j+k+1][6]),int(data2[i+j+k+1][6]),int(data3[i+j+k+1][6]),int(data4[i+j+k+1][6])],marker = "o",label='bid',color='pink',linestyle = "dashdot")
      ax3.set_title(data1[i+j+k+1][2])
    """
    #print(time_transition,[int(data1[i+j+k+1][3]),int(data2[i+j+k+1][3]),int(data3[i+j+k+1][3]),int(data4[i+j+k+1][3])])
    ax1.plot(time_transition,[int(data1[i+j+1][3]),int(data2[i+j+1][3]),int(data3[i+j+1][3]),int(data4[i+j+1][3])],marker = "o",label='over',color='b')
    ax1.plot(time_transition,[int(data1[i+j+1][4]),int(data2[i+j+1][4]),int(data3[i+j+1][4]),int(data4[i+j+1][4])],marker = "o",label='under',color='r')
    ax2.plot(time_transition,[int(data1[i+j+1][5]),int(data2[i+j+1][5]),int(data3[i+j+1][5]),int(data4[i+j+1][5])],marker = "o",label='offer',color='cyan',linestyle = "dashdot")
    ax2.plot(time_transition,[int(data1[i+j+1][6]),int(data2[i+j+1][6]),int(data3[i+j+1][6]),int(data4[i+j+1][6])],marker = "o",label='bid',color='pink',linestyle = "dashdot")
    ax1.set_title(data1[i+j+1][2])
    j += 1
  i += 10

plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig1.tight_layout()
#fig2.tight_layout()
"""
plt.gcf().text(0.05,0.55,"over/under",rotation=90, backgroundcolor='yellow')
plt.gcf().text(0.45,0.90,"time", backgroundcolor='yellow')
"""
plt.legend()
plt.savefig(file_name + '.jpg')
#fig2.savefig(file_name + 'select.jpg')
#plt.show()
