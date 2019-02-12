name="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
name_etc=name.split(',')
name_cnt=0
lee_cnt=0
for name_find in name_etc:
    if name_find[:1] in '김' or name_find[:1] in '이':
        name_cnt+=1
    if name_find in "이재영":
        lee_cnt+=1
name_set=set(name_etc)
name_list=list(name_set)
print(name_cnt)
print(lee_cnt)
print(name_list)
name_list.sort()
print(name_list)
