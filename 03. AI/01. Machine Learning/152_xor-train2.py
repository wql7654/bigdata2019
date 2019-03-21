import pandas as pd
from sklearn import svm,metrics
# XOR의 계산 결과 데이터
xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
and_data = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]
or_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
nand_data = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
nor_data = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
]
not_data = [
    [0, 0],
    [0, 1]
]

xor_df = pd.DataFrame(xor_data)
and_df = pd.DataFrame(and_data)
or_df = pd.DataFrame(or_data)
not_df = pd.DataFrame(not_data)
nor_df = pd.DataFrame(nand_data)
nand_df = pd.DataFrame(nor_data)
# xor_dat=xor_df.loc[:,0:1]
xor_dat=xor_df.iloc[:,0:2]
xor_label=xor_df.iloc[:,2]

and_dat=and_df.loc[:,0:1]
and_label=and_df.loc[:,2]

or_dat=or_df.loc[:,0:1]
or_label=or_df.loc[:,2]

not_dat=not_df.loc[:,0:1]
not_label=not_df.loc[:,1]

nor_dat=nor_df.loc[:,0:1]
nor_label=nor_df.loc[:,2]

nand_dat=nand_df.loc[:,0:1]
nand_label=nand_df.loc[:,2]

clf = svm.SVC(gamma='auto')
clf2 = svm.SVC(gamma='auto')
clf3 = svm.SVC(gamma='auto')
clf4 = svm.SVC(gamma='auto')
clf5 = svm.SVC(gamma='auto')
clf6 = svm.SVC(gamma='auto')
clf.fit(xor_dat,xor_label)
clf2.fit(and_dat,and_label)
clf3.fit(or_dat,or_label)
clf4.fit(not_dat,not_label)
clf5.fit(nor_dat,or_label)
clf6.fit(nand_dat,nand_label)

pre=clf.predict(xor_dat)
pre2=clf2.predict(and_dat)
pre3=clf3.predict(or_dat)
pre4=clf4.predict(not_dat)
pre5=clf5.predict(nor_dat)
pre6=clf6.predict(nand_dat)
ac_score=metrics.accuracy_score(xor_label,pre)
ac_score2=metrics.accuracy_score(and_label,pre2)
ac_score3=metrics.accuracy_score(or_label,pre3)
ac_score4=metrics.accuracy_score(not_label,pre4)
ac_score5=metrics.accuracy_score(nor_label,pre5)
ac_score6=metrics.accuracy_score(nand_label,pre6)

print("xor정답률 = ",ac_score)
print("and정답률 = ",ac_score2)
print("or정답률 = ",ac_score3)
print("not정답률 = ",ac_score4)
print("nor정답률 = ",ac_score5)
print("nand정답률 = ",ac_score6)
