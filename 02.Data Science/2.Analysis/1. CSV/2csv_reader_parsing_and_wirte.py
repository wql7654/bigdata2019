#!/usr/bin/env python3
import sys
import csv

input_file = sys.argv[1]    # supplier_data.csv
output_file = sys.argv[2]   # output_files/1output.csv

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file, delimiter=',')
        filewriter=csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            filewriter.writerow(row_list)


#데이터 불러와서 데이터통째로 이동