import re

def decide(str):
    if str:
        print("True")
    else:
        print("Fleas")

def one_thing(string):
    z=re.compile("[^0-9a-zA-Z].+")
    c=z.match(string)
    decide(c)

def two_thing(string):
    z=re.compile("ab+?")
    c = z.match(string)
    decide(c)

def three_thing(string):
    z=re.compile("ab*?")
    c = z.match(string)
    decide(c)

def four_thing(string):
    z=re.compile("ab?")
    c = z.match(string)
    decide(c)

def five_thing(string):
    z=re.compile("ab{3}")
    c = z.match(string)
    decide(c)

def six_thing(string):
    z=re.compile("ab{2,3}?")
    c = z.match(string)
    decide(c)

def seven_thing(string):
    z=re.compile("[a-z]+_[a-z]+")
    c = z.match(string)
    decide(c)

def eight_thing(string):
    z=re.compile("[A-Z]{1}[a-z]{1}")
    c = z.match(string)
    decide(c)

def nine_thing(string):
    z=re.compile("a.*?b&")
    c = z.match(string)
    decide(c)

def ten_thing(string):
    z=re.compile("^\w+")
    c = z.match(string)
    decide(c)

def eleven_thing(string):
    z=re.compile("\w+\S*$")
    c = z.match(string)
    decide(c)

def twelve_thing(string):
    z=re.compile("\w*z.\w*")
    c = z.match(string)
    print(c)

def thirteen_thing(string):
    z=re.compile("\Bz\B")
    c = z.search(string)
    print(c)

def fourteen_thing(string):
    z=re.compile("^[a-zA-Z0-9]*&")
    c = z.match(string)
    decide(c)

def fiftenteen_thing(string):
    z=re.compile(r"^\W")
    c = z.match(string)
    decide(c)

def sixteen_thing(string):
    c = re.sub('\.[0]*', '.', string)
    print(c)

def seventeen_thing(string):
    z=re.compile(r"[0-9]$")
    c = z.search(string)
    decide(c)

def eighteen_thing(string):
    z=re.findall(r"[0-9]{1,3}",string)
    for b in z:
        print(b)

def nineteen_thing():
    string='The quick brown fox jumps over the lazy dog.'
    z=re.findall("fox|dog|horse",string)
    for c in z:
        print(c)

def twenty_thing():
    string='The quick brown fox jumps over the lazy dog.'
    z=re.finditer("fox",string)
    for c in z:
        print(c)

def twentyone_thing():
    string='Python exercises, PHP exercises, C# exercises'
    z=re.findall("exercises",string)
    for c in z:
        print(c)

def twentytwo_thing():
    string='Python exercises, PHP exercises, C# exercises'
    z=re.finditer("exercises",string)
    for c in z:
        print(c)

def twentythree_thing(string):
    c = re.sub(' ', '_', string)
    print(c)

def twentyfour_thing():
    string = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    z = re.findall(r"/(\d{4}).(\d{1,2}).(\d{1,2})/", string)
    print(z)

def twentyfive_thing():
    string="2018-02-05"
    c = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\g<3>-\g<2>-\g<1>', string)
    print(c)

def twentysix_thing():
    words = ["Python PHP", "Java JavaScript", "c c++"]
    for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        # Check for success
        if m:
            print(m.groups())
def twentyseven_thing():
    string='20exercises,360exercises, 40exercises'
    z=re.finditer("\d*",string)
    for c in z:
        print(c)
def twentyeight_thing():
    string='a20exerciswwesa,360xrcisa se, 40exercises'
    z=re.findall("[ae]\w+", string)
    print(z)

def twentynine_thing():
    string='a20exerciswwesa,360xrcisa se, 40exercises'
    z=re.findall("[ae]\w+", string)
    print(z)

def twentyeight_thing():
    string='a20exerciswwesa,360xrcisa se, 40exercises'
    z=re.finditer("\D*\w+", string)
    print(z)
def thirty_thing():
    string="Roadbycar"
    c = re.sub('Road','rd' , string)
    print(c)

def thirtyone_thing():
    string="Road by car"
    c = re.sub('[,. ]',':' , string)
    print(c)


def thirtytwo_thing():
    string="Road by,.car"
    c = re.sub('[,. ]',':' , string,2)
    print(c)

def thirtythree_thing():
    string = 'wwesa,360xrcisa se, 40exercises'
    z = re.findall(r"\b\w{5}\b", string)
    print(z)

def thirtyfour_thing():
    string = 'a20exerciswwesa,360xrcisa se, 40exercises'
    z = re.findall(r"\b\w{3,5}\b", string)
    print(z)


def thirtyfive_thing():
    string = 'a20exerciswwesa,360xrcisa, se, 40exercises'
    z = re.findall(r"\b\w{4,}\b", string)
    print(z)


thirtyfive_thing()