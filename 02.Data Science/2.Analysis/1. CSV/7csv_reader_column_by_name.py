#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]    # supplier_data.csv
output_file = sys.argv[2]   # output_files/output.csv

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)


#['Invoice Number', 'Purchase Date'] 원하는 열로 필터링하는 코드