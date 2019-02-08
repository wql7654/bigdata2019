
# f=open("./새파일.txt",'w')  현재 경로에 파일 생성
#                             windows, unix 모든 운영체제에서 통용됨

# f=open("../../../mypath//new/새파일.txt",'w')
#워크스페이스를  벗어난 상태라면 위험할수가있다 (위치변경시)
# f=open("../path_exe/새파일.txt",'w')
# f=open("../path_exe//new1/새파일.txt",'w')
# f=open("../path_exe/wwwe/새파일.txt",'w')

f=open("../Path_exe/wwwe/새파일.txt",'w')
# 대소문자 구분없이 사용가능한건 windows에서만 가능하다
# 따라서 호완성을 위해서 대소문자는 가리는것이 좋다

f.close()