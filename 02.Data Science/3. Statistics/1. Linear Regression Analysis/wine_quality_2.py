# 그룹화 히스토그램

# import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
# import statsmodels.formula.api as smf
# from statsmodels.formula.api import ols, glm

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())

# Display descriptive statistics for all variables
print('변수별 요약통계 표시')
print(wine.describe())

# Identify unique values
print('\n유일값 찾기')
print(sorted(wine.quality.unique()))

# Calculate value frequencies
print('\n빈도 찾기')
print(wine.quality.value_counts())

# Display descriptive statistics for quality by wine type
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print("\n"+ '='*80)
print('7.2.2 그룹화, 히스토그램, t 검정')
# red_wine = wine.ix[wine['type']=='red', 'quality']
red_wine = wine.loc[wine['type']=='red', 'quality']
# white_wine = wine.ix[wine['type']=='white', 'quality']
white_wine = wine.loc[wine['type']=='white', 'quality']

sns.set_style('dark')
print(sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label='Red wine'))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label='White wine'))

# sns.axlabel('Quality Score', 'Density')
plt.xlabel('Quality Score')
plt.ylabel('Density')
plt.title('Distribution of Quality by wine Type')
plt.legend()
plt.show()

# Test whether mean quality is different between red and white wines
print('\n와인의 종류에 따라 품질의 차이 검정')
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f' %(tstat, pvalue))

# pvalue:유의확률(통계값을 얼마나 신뢰할수있는가를 나타내는 지표)
# pbalue가 0.05 보다 크면 결과를 기각할 수 있다.
# t 검정(t-test) 서로 다른 두 그룹 간 평균의 차이가 유의한지를 검정하는 통계적인 방법으로
# 샘플의 등분신성, 독립성을 충족하고 정규성이 부족할 경우적용할 수 있다
#  이 예제에서 두 샘플은 독립이고
# 표준편차가 작으므로 등분상성을 충족한다고 볼 수 있다.
# 히스토그램과 계수(30개이상)로 볼때 정규분포 데이터를 활용해도 좋다

