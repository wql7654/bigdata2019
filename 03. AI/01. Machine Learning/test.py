import random

def calc_bmi(w,h):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5:
        return 'tine'+ '\n'
    elif bmi >=18.5 and bmi <25:
        return 'nomale'+ '\n'
    elif bmi >= 25:
        return 'fat'+ '\n'
data=[]

label = 'height,weight,label\n'
data.append(label)
for i in range(30000):
    h = random.randint(120, 200)
    w = random.randint(35, 80)
    data.append(str(h) + ',' + str(w) + ',' + calc_bmi(w,h))

with open('data.csv', 'w', encoding='utf-8') as f:
    f.writelines(data)