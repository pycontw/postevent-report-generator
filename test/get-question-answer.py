#!/usr/bin/env python3
from title import cat_title


with open('../../attendees-analyzer-working/titles.csv') as db:
    lines = db.readlines()
    for line in lines:
        line = line.rstrip()
        print(line + ',' + cat_title(line))

