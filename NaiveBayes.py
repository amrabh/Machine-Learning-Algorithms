##############################################################################################
# Machine Learning Summer 2020
# Assignment 1 -NaiveBayes Classification
# Author- Amruta Abhyankar UCID-aa2348
###############################################################################################

import sys

data_file = sys.argv[1]
f = open(data_file, 'r')
data = []
i = 0
l = f.readline()

########### Reading Data File  #########

while l != '':
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

########## Reading Training Labels #########

label_file = sys.argv[2]
f = open(label_file)
train_labels = {}
n = [0, 0]
l = f.readline()
while l != '':
    a = l.split()
    train_labels[a[1]] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1

################# Computing means for each Class #################
mean_0 = []
for j in range(0, cols, 1):
    mean_0.append(0.01)

mean_1 = []
for j in range(0, cols, 1):
    mean_1.append(0.01)

for i in range(0, rows, 1):
    if train_labels.get(str(i)) is not None:
        if train_labels.get(str(i)) == 0:
            for j in range(0, cols, 1):
                mean_0[j] = mean_0[j] + data[i][j]
        if train_labels.get(str(i)) == 1:
            for j in range(0, cols, 1):
                mean_1[j] = mean_1[j] + data[i][j]
for j in range(0, cols, 1):
    mean_0[j] = mean_0[j] / n[0]
    mean_1[j] = mean_1[j] / n[1]

############### Calculating Standard Deviation for each Class ########################
sd_0 = []
for j in range(0, cols, 1):
    sd_0.append(0.1)
sd_1 = []
for j in range(0, cols, 1):
    sd_1.append(0.1)

for i in range(0, rows, 1):
    if train_labels.get(str(i)) is not None:
        if train_labels.get(str(i)) == 0:
            for j in range(0, cols, 1):
                sd_0[j] = sd_0[j] + (data[i][j] - mean_0[j]) ** 2
        if train_labels.get(str(i)) == 1:
            for j in range(0, cols, 1):
                sd_1[j] = sd_1[j] + (data[i][j] - mean_1[j]) ** 2
for j in range(0, cols, 1):
    sd_0[j] = (sd_0[j] / n[0]) ** 0.5
    sd_1[j] = (sd_1[j] / n[1]) ** 0.5

############ Naives Classifier ######################

for i in range(0, rows, 1):
    if train_labels.get(str(i)) is None:
        d0 = 0
        d1 = 0

        for j in range(0, cols, 1):
            d0 += ((data[i][j] - mean_0[j]) / sd_0[j]) ** 2
            d1 += ((data[i][j] - mean_1[j]) / sd_1[j]) ** 2
        if d0 < d1:
            print("0 ", i)
        else:
            print("1 ", i)
