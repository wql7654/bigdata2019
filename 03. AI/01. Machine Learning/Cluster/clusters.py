#비지도 학습의 예제

import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics
from sklearn.cluster import KMeans
import matplotlib.pyplot  as plt
import seaborn as sns


alco=pd.read_csv("niaaa-report2009.csv",index_col="State")
columns=["Wine","Beer"]

kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco[columns])
alco["Clusters"] = kmeans.labels_

alco.to_csv("Clustering_Result.csv",index=False)

data=alco[["Wine","Beer"]]
label=alco["Clusters"]

predicted_result=kmeans.predict(data)
print("예측 클러스트링 결과")
print(predicted_result)
print("정답률: %s %%"%(metrics.accuracy_score(label,predicted_result)*100))

center_x = alco['Wine']
center_y = alco['Beer']
center_xy=alco["Clusters"]
center_yx=predicted_result
plt.scatter(center_x,center_y,s=50,marker='D',c='r')
plt.show()
