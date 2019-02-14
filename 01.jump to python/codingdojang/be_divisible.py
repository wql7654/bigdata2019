prime_number =[]
for i in range(2,21):
    chk = True
    for j in range(2,i):
        if i%j == 0:
            chk = False
            break
    if chk:
        prime_number .append(i)
multiplication=1
for z in prime_number:
    multiplication*=int(z)

answer=0
while True:
    ti=0
    answer = answer + multiplication
    for i in range(1,21):
        i=int(i)
        if answer%i==0:
            ti+=1
        if ti==20:
            print(answer)
            quit()

