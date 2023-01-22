import math
import os, sys, glob
import re
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import datetime
import csv
import japanize_matplotlib

#file_name = '/Users/mac10/Desktop/stock/data' + datetime.datetime.now().strftime('%Y-%m-%d')
file_name = '/Users/mac10/Desktop/stock/data' + "2021-11-02"

data1 = []
data2 = []
data3 = []
data4 = []

select_num = [21,31,46,50,68,77,97]
select_len = len(select_num)

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
fig1, axes1 = plt.subplots(3,math.ceil(select_len/3),figsize=(20, 14), dpi=100, facecolor='w', linewidth=0, edgecolor='w')

count1 = 1
count2 = 1
for k in range(100):
  if k+1 == select_num[0] or k+1 == select_num[1] or k+1 == select_num[2] or k+1 == select_num[3] or k+1 == select_num[4] or k+1 == select_num[5] or k+1 == select_num[6]:
    axes1[count1][count2].plot(time_transition,[int(data1[k+1][3]),int(data2[k+1][3]),int(data3[k+1][3]),int(data4[k+1][3])],marker = "o",label='over',color='b')
    count1 += 1
  if count1 == 3:
    count1 = 1
    count2 += 1

i = 0
for ax_row1 in axes1:
  j = 0
  print("1i+j=",i+j)
  for ax1 in ax_row1:
    ax2 = ax1.twinx()
    print("2i+j=",i+j)
    if i+j+1 == select_num[0] or i+j+1 == select_num[1] or i+j+1 == select_num[2]:
      ax1.plot(time_transition,[int(data1[i+j+1][3]),int(data2[i+j+1][3]),int(data3[i+j+1][3]),int(data4[i+j+1][3])],marker = "o",label='over',color='b')
      ax1.plot(time_transition,[int(data1[i+j+1][4]),int(data2[i+j+1][4]),int(data3[i+j+1][4]),int(data4[i+j+1][4])],marker = "o",label='under',color='r')
      ax2.plot(time_transition,[int(data1[i+j+1][5]),int(data2[i+j+1][5]),int(data3[i+j+1][5]),int(data4[i+j+1][5])],marker = "o",label='offer',color='cyan',linestyle = "dashdot")
      ax2.plot(time_transition,[int(data1[i+j+1][6]),int(data2[i+j+1][6]),int(data3[i+j+1][6]),int(data4[i+j+1][6])],marker = "o",label='bid',color='pink',linestyle = "dashdot")
      ax2.set_title(data1[i+j+1][2])
    j += 1
  i += 10


plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig1.tight_layout()
"""
plt.gcf().text(0.05,0.55,"over/under",rotation=90, backgroundcolor='yellow')
plt.gcf().text(0.45,0.90,"time", backgroundcolor='yellow')
"""
plt.legend()
plt.savefig(file_name + '_select.jpg')
#plt.show()
