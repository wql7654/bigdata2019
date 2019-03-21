import struct
import pandas as pd
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open('./mnist/' + name + '-labels-idx1-ubyte', 'rb')
    img_f = open('./mnist/' + name + '-images-idx3-ubyte', 'rb')
    csv_f = open('./mnist/' + name + '.csv', 'w', encoding='utf-8')
    # 헤더 정보 읽기
    mag, lbl_count = struct.unpack('>II', lbl_f.read(8))
    mag, img_count = struct.unpack('>II', img_f.read(8))
    rows, cols = struct.unpack('>II', img_f.read(8))
    pixels = rows*cols
    # 이미지데이터를 읽고 csv로 저장하기
    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        label = struct.unpack('B', lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+ ',')
        csv_f.write(','.join(sdata) + '\r\n')
        # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기
        if idx < 10:
            s = 'B2 28 28 255\n'
            s += ' '.join(sdata)
            iname = './mnist/{0}-{1}-{2}.pgm'.format(name, idx, label)
            with open(iname, 'w', encoding='utf-8') as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()
# 결과를 파일로 출력하기
to_csv('train', 10)
# to_csv('train', 60000)
to_csv('t10k', 5)


data = pd.read_csv("./mnist/train.csv",header=None)
test = pd.read_csv("./mnist/t10k.csv",header=None)

all_data = []
all_data.append(data)
all_data.append(test)
data_concat = pd.concat(all_data)
data_concat.to_csv('./mnist/all_data.csv',index=False,header=0)