mutiple_out=0
for mutiple_cnt in range(1,1000):
    if mutiple_cnt%3 == 0:
        mutiple_out+=mutiple_cnt
    elif mutiple_cnt%5 == 0:
        mutiple_out+=mutiple_cnt

print(mutiple_out)
