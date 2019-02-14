while True:
    page_num = input("게시물의 총건수와 한페이지에 보여줄 게시물수를 입력하세요 (띄어쓰기로 구분):").split()
    page_num[0]=int(page_num[0])
    page_num[1] =int(page_num[1])
    if page_num[0] % page_num[1]!=0:
         output=(page_num[0]/ page_num[1])+1
    else:
         output = (page_num[0] / page_num[1])
    print("%s , %s , %s"%(page_num[0],page_num[1],int(output)))
