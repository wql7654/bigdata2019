import math
import pandas as pd
import numpy as np
from pandas import DataFrame

def get_csv_row_instance(primary_key): #행
    # Row_instance=[]

    data['JURISDICTION NAME'] = data['JURISDICTION NAME'].astype(str)
    Row_instance = data.ix[(data['JURISDICTION NAME'].str.contains(primary_key)),:]
    print(Row_instance)
    # Row_instance.to_csv('get_row.csv', index=False)
    return Row_instance

def get_csv_col_instance(col_name): #열 기준점
    col_instance=[]
    col_instance = data.ix[:,[col_name]]
    # col_instance.to_csv('get_col.csv', index=False)
    print(col_instance)

    return col_instance

def Convert_Type(col_instance):
    # 내용을 작성하세요.
    return col_instance

def My_Sum(data_list):
    My_Sum=0
    My_Sum=get_csv_col_instance(data_list).sum()
    return My_Sum

def My_Average(data_list):
    My_Average=0
    My_Average=My_Sum(data_list)/len(data.loc[:, data_list])

    return My_Average

def My_Max(data_list):
    My_Max=0
    My_Max=get_csv_col_instance(data_list).max()
    return My_Max

def My_Min(data_list):
    My_Min = 0
    My_Min=get_csv_col_instance(data_list).min()
    return My_Min

def My_Deviation(data_list): # 편차
    My_Deviation=0

    print(data)
    retrun_deviation=[]
    index="My_Deviation"
    list_data=list(data[data_list])
    avg = float(My_Average(data_list))
    for i in list_data:
        My_Deviation = i - avg
        # print(My_Deviation)
        retrun_deviation.append(My_Deviation)

    # print(retrun_deviation)
    test={index:retrun_deviation}
    data.append(test)
    data_df=DataFrame(data)
    data_df.to_csv('get_col.csv', index=False)

    return retrun_deviation

def My_Standard_Deviation(data_list):# 표준편차
    Variance=0
    My_Standard_Deviation=math.sqrt(My_Variance(data_list))
    return My_Standard_Deviation

def My_Variance(data_list):#분산
    My_Variance=0
    My_Variance = get_csv_col_instance(data_list).var()
    return My_Variance

def My_Ascendant(data_list):#오름차순
    print(sorted(list(data[data_list]),reverse=True))

def My_Descendant(data_list):#내림차순
    print(sorted(list(data[data_list]),reverse=False))


def print_row(row_instance):
    row=get_csv_row_instance(row_instance)
    rows = '\n'.join(row)
    print(rows)

def print_col(col_instance):
    col=get_csv_col_instance(col_instance)
    cols = '\n'.join(col)
    print(cols)


data=pd.read_csv("Demographic_Statistics_By_Zip_Code.csv")
# print(data_frame)
# data=[]

while True:
    print("<CSV Handle 연습예제>\n"
          "0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬")
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num == 1:
        Access_num = input('Access Key를 입력하세요: ')
        get_csv_row_instance(Access_num)
        # print_row(Access_num)
    elif menu_num == 2:
        Access_num2 = input('Access Key를 입력하세요: ')
        get_csv_col_instance(Access_num2)
        # print_col(Access_num2)
    elif menu_num == 3:
        Access_num3 = input('Access Key를 입력하세요: ')
        My_Sums=My_Sum(Access_num3)
        print_col(Access_num3)
        print("총합:%s" % My_Sums)
    elif menu_num == 4:
        Access_num4 = input('Access Key를 입력하세요: ')
        My_Averages=My_Average(Access_num4)
        print_col(Access_num4)
        print("평균:%s" % My_Averages)
    elif menu_num == 5:
        Access_num5 = input('Access Key를 입력하세요: ')
        My_Maxs=My_Max(Access_num5)
        print_col(Access_num5)
        print("최대값:%s"%My_Maxs)
    elif menu_num == 6:
        Access_num6 = input('Access Key를 입력하세요: ')
        My_Mins = My_Min(Access_num6)
        print_col(Access_num6)
        print("최소값:%s" % My_Mins)
    elif menu_num == 7:
        Access_num7 = input('Access Key를 입력하세요: ')
        print("편차(Deviation) 공식 : 표본값 - 평균\n표본  편차")
        My_Deviation(Access_num7)
    elif menu_num == 8:
        Access_num8 = input('Access Key를 입력하세요: ')
        Standard_Deviation=My_Standard_Deviation(Access_num8)
        print_col(Access_num8)
        print("표준편차(Standard Deviation) 공식: √분산")
        print("표준편차:%s"%Standard_Deviation)
    elif menu_num == 9:
        Access_num9 = input('Access Key를 입력하세요: ')
        My_Variances=My_Variance(Access_num9)
        print_col(Access_num9)
        print("분산(Variance) 공식: ∑(표본-평균)**2/표본수")
        print("분산:%s"%My_Variances)
    elif menu_num == 10:
        Access_num10 = input('Access Key를 입력하세요: ')
        My_Ascendant(Access_num10)
    elif menu_num == 11:
        Access_num11 = input('Access Key를 입력하세요: ')
        My_Descendant(Access_num11)

    elif menu_num == 0:
        quit()

