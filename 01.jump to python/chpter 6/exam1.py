

str_cnt = input("문자")
str_list = list(str(str_cnt))
cnt = 1
reserve = ''
str_output = []
common = 0
for str_save in str_list + ['']:
    if str_save != reserve and common == 1:
        str_output.append(str(cnt))
        cnt = 1
    if str_save != reserve:
        str_output.append(str_save)
    else:
        cnt += 1
    common = 1
    reserve = str_save
print("".join(str_output))
