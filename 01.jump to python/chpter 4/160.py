# f=open("새파일.txt",'w') 현재 소스코드 파일이 있는 경로에 파일 생성
                           #유닉스 계열에서는 실행이 안될수도 있다.
# f=open("D:\\새파일.txt",'w') #절대 경로에 파일 생성
# f=open("D:\\mypath\새파일.txt",'w')
# f=open("D:/새파일.txt",'w')
# f=open("D:\\mypath\\new\\새파일.txt",'w') \n 같이 안될때를 대비해서 \\를 사용
# f=open("D:/mypath/new/새파일.txt",'w') /를 한번만 사용해도 됨
f.close()