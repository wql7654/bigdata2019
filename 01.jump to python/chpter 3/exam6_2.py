# coding: cp949
cnt_star=int(input("홀수를 입력하세요(0 <- 종료): "))
cnt_line=int((cnt_star+1)/2)
if cnt_star == 0 or cnt_star%2==0:
   exit()
pic_draw=1
length=cnt_star+2
while length>0:
	length-=1
	width=cnt_star+2
	if length>=(cnt_star/2):
		cnt_empt=(cnt_line-1)
		view_star=int(cnt_star-(cnt_empt*2)-2)
	elif length<(cnt_star/2):
		cnt_empt=-(cnt_line+1)
		view_star=int(cnt_star-(cnt_empt*2)-2)
	while width>0:    
		if length%(cnt_star+1)==0 and 1<width<cnt_star+2:
			pic_draw='-'
		elif (width==1 or width==cnt_star+2) and 0<length<cnt_star+1:
			pic_draw='l'
		elif cnt_empt>(cnt_star-width):
			pic_draw=' '
		elif view_star>0:
			pic_draw='*'
			view_star-=1
		else:
			pic_draw=' '
		print("%s"%pic_draw ,end='')
		width-=1
	cnt_line-=1
	print(' ')
