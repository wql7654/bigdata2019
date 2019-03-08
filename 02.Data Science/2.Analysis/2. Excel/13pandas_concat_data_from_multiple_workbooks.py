# !/uer/bin/env python3
import pandas as pd
import sys
import glob
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frames = []
for workbook in all_workbooks:
    all_workbooks = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_workbooks.items():
        data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()


