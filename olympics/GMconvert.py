from asyncore import write
import csv

GM = []
with open('event_results.csv') as original_data_file,\
        open('nocs.csv') as nocs_data_file,\
            open('goldMedal.csv', 'w', newline = "") as GM_results_file:
    reader = csv.reader(original_data_file)
    nocsReader = csv.reader(nocs_data_file)
    writer = csv.writer(GM_results_file)
    for row in reader:
        if row[4] == 'Gold':
            GM.append(row[2])
    print(len(GM))
    sat = set(GM)
    for s in sat:
        writer.writerow([s, GM.count(s)])
