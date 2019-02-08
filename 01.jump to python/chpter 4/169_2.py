f=open("sample.txt")
lines=f.readlines()
f.close()

total = 0
for line in lines:
    score=int(line)
    total+=score

print(total)


average=int(total)/int(len(lines))

f=open("result.txt",'w',encoding="UTF-8")
f.write(str(average))
f.close()