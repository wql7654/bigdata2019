#!/usr/bin/env python3
import csv
import sys
import glob
import os

input_path = sys.argv[1]    # supplier_data.csv

file_counter= 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
       filereader = csv.reader(csv_in_file)
       header = next(filereader)
       for row in filereader:
           row_counter += 1
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print('Numb er of files: {0:d}'.format(file_counter))


#폴더안에 원하는 네임을가진 파일의 갯수와 리스트를 보여주는 코드