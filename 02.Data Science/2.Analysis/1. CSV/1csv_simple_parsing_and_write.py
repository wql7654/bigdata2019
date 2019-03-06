#!/usr/bin/env python3
import sys

input_file = sys.argv[1]    # supplier_data.csv
output_file = sys.argv[2]   # output_files/1output.csv


# newline 줄바꿈문자생략
with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
        header = filereader.readline() # 헤더행
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(header_list) + '\n')
                        #join(map(str, header_list))
                        # ','.join(header_list)
        for row in filereader:
            row = row.strip() #공백제거
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str, row_list)) + '\n')

#데이터 불러와서 헤드따로 데이터따로 이동

# supplier_data.csv output_files/1c_output.csv
# supplier_data.csv output_files/1p_output.csv
#
# supplier_data.csv output_files/2c_output.csv
#
# supplier_data.csv output_files/3c_output.csv
# supplier_data.csv output_files/3p_output.csv
#
# supplier_data.csv output_files/4c_output.csv
# supplier_data.csv output_files/4p_output.csv
#
# supplier_data.csv output_files/5c_output.csv
# supplier_data.csv output_files/5p_output.csv
#
# supplier_data.csv output_files/6c_output.csv
# supplier_data.csv output_files/6p_output.csv
#
# supplier_data.csv output_files/7c_output.csv
# supplier_data.csv output_files/7p_output.csv
#
# 8,9번째 실행인자
# bigdata_repository
#
# bigdata_repository output_files/9c_output.csv
# bigdata_repository output_files/9p_output.csv
#
# bigdata_repository output_files/10c_output.csv
# bigdata_repository output_files/10p_output.csv
#
#
# supplier_data_unnecessary_header_footer.csv output_files/11c_output.csv
# supplier_data_unnecessary_header_footer.csv output_files/11p_output.csv
#
# supplier_data_no_header_row.csv output_files/12c_output.csv
# supplier_data_no_header_row.csv output_files/12p_output.csv