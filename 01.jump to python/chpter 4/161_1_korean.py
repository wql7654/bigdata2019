#파이참에서 한글설정을 할려면 file encoding 을 euc-kr로 변경
#이지만 공용적으로 사용하기위해 인코딩을 따로 넣어줌

f=open("새폴더.txt",'w',encoding='UTF-8')
f.write('안녕하세요\n')
f.close()
