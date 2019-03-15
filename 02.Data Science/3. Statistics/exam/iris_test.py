import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import statsmodels.api as sm
# import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

print("빅데이터 로드 중...")
iris = pd.read_csv('iris.csv', sep = ',', header = 0)

print("분석용 빅데이터 가공 중...")
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace('.', '_')]
iris['variety01'] = np.where(iris['variety'] == 'Setosa', 1., 0.)

print("빅데이터 통계 분석 모델 생성 중..")
dependent_variable = iris['variety01']
independent_variables = iris[['sepal_length', 'sepal_width', 'petal_length' ,'petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend = True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()
print("테스트 데이터 선별 중...")

print('\n샘플링 데이터 예측 테스트 중')
print('6개 샘플링 데이터 리스트')
new_observations = iris.ix[iris.index.isin(range(48, 54)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
print(new_observations_with_constant)

print('\n예측 결과 분석 중')
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]

variety01 = []
for i in range(48, 54):
    variety01.append(iris['variety01'][i])

correct = 0
incorrect = 0
for i in range(len(variety01)):
    if y_predicted_rounded[i] == 1.0:
        print('%s번째 샘플링 데이터 예측 결과 %s : Setosa 확실' % (i + 1, y_predicted_rounded[i]), end='')
        if y_predicted_rounded[i] == variety01[i]:
            print('=> 정답')
            correct += 1
        else:
            print('Setosa 확실 = > 오답')
            incorrect += 1
    else:
        print('%s번째 샘플링 데이터 예측 결과 %s : Setosa이 아닌 다른 품종' % (i + 1, y_predicted_rounded[i]), end='')
        if y_predicted_rounded[i] == variety01[i]:
            print('=> 정답')
            correct += 1
        else:
            print('Setosa 확실 = > 오답')
            incorrect += 1

print('\n<분석 결과 요약>')
print('관측계수: %d' % len(y_predicted_rounded))
print("정답률: %d / %d = %.1f" %(correct, len(y_predicted_rounded),correct/len(y_predicted_rounded)*100), end='')
print('%')