import re

def q3():
    s = """
    park 010-9999-9988
    kim 010-9909-7789
    lee 010-8789-7768
    """
    pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
    result = pat.sub("\g<1>-####", s)

    print(result)


def q4():
    file_name=["lee@myhome.co.kr","park@naver.com","kim@daum.net"]
    p = re.compile(".*[@].*[.](?=com$|net$).*$")
    for file in file_name:
        m = p.match(file)
        print(m)


q3()
q4()