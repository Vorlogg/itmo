import csv

csv.writer(open('output.txt', 'w+'), delimiter='\t').writerows(csv.reader(open("wordsim353_sample.csv")))