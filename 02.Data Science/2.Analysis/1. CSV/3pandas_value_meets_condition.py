#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_value = data_frame.loc[(data_frame['Supplier Name'].str.contains('3')) & (data_frame['Cost'] > 600.0), :]

data_value.to_csv(output_file, index=False)


##cointains 지정된 문자열이 포함되는지 확인하는 함수
