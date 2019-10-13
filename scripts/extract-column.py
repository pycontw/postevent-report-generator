#!/usr/bin/env python3
import csv

output = []

with open("../../attendees-analyzer-working/2017Attendees.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        output.append(row[12])

print("Now saving...")

with open("../../attendees-analyzer-working/titles.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in output:
        spamwriter.writerow([row])
