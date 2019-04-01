#비지도 학습의 예제

import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics
from sklearn.cluster import KMeans
import matplotlib.pyplot  as plt
import seaborn as sns
from collections import Counter


alco=pd.read_csv("lotto.csv")
columns=['a','s','d','f','g','h']

kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco[columns])
alco["Clusters"] = kmeans.labels_

alco.to_csv("lotoresult.csv",index=False)

print(alco["Clusters"])

data=alco[columns]
label=alco["Clusters"]

predicted_result=kmeans.predict(data)
print("예측 클러스트링 결과")
print(predicted_result)
print("정답률: %s %%"%(metrics.accuracy_score(label,predicted_result)*100))

center_xy = alco['a']
center_yx = alco['s']
center_x=alco["Clusters"]
center_y=predicted_result
print(Counter(alco["Clusters"]))
plt.scatter(center_x,center_y,s=50,marker='D',c='r')
plt.show()
