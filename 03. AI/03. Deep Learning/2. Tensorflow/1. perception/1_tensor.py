import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
#warring 에 대해서 오류제거용 코드 올바른 버젼으로 텐스플로우를 재설치하면 오류는 사라진다 명시해놓음

ta=tf.zeros((2,2))

session=tf.InteractiveSession()
print(ta.eval())
session.close()