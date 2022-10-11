from asyncore import write
import csv

from matplotlib.pyplot import summer


sum = 0
with open('goldMedal.csv') as original_data_file:
    reader = csv.reader(original_data_file)
    for row in reader:
        sum += int(row[1])
print(sum)
