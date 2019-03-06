#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]    # supplier_data.csv
output_file = sys.argv[2]   # output_files/1output.csv

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number1', 'Cost', 'Purchase Date']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)


#파일을 헤더파일로 나눠어서 편집