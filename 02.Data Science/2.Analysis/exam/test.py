
import pandas as pd

input_file="Demographic_Statistics_By_Zip_Code.csv"
# data_frame = pd.read_csv(data)

# header_list ='COUNT PARTICIPANTS'
# data_frame = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv",names=header_list)
# col_instance = data_frame.ix[header_list]

data_frame = pd.read_csv(input_file)

print(list(data_frame['COUNT PARTICIPANTS']))
# data_frame_column_by_index = data_frame.ix[data_frame['PERCENT PUBLIC ASSISTANCE TOTAL'].astype(int),:]
# data_frame_column_by_index = data_frame.ix[:,['PERCENT PUBLIC ASSISTANCE TOTAL']]
# data_frame_column_by_index=data_frame.ix[:, ['COUNT PARTICIPANTS']]
# print(list(data_frame_column_by_index))

# data_frame_column_by_index.to_csv(output_file,  index=False)

# data_frame = pd.read_csv(input_file)
# data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
#
# data_frame_column_by_index.to_csv(output_file,  index=False)