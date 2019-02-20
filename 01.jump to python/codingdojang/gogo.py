from random import randint

SEEDMAX = 100000
BETMAX = 10000


def seed(name):
    s = int(input(f"{name} seed(1~{SEEDMAX}): "))
    return s if 1<=s<=SEEDMAX else seed(name)


def bet(usr):
    lmt = min(usr['money'], BETMAX)
    b = int(input(f"{usr['name']} bet(1~{lmt}): "))
    return b if 1<=b<=lmt else bet(usr)


def roll():
    return randint(1, 6), randint(1, 6)


def dbl(d):
    return d[0] == d[1]


def score(d):
    return d[0] + d[1] + dbl(d) * 10


def play(usr, bet):
    rd, ru = roll(), roll()
    if score(ru) >= score(rd):
        winner, loser = (usr['name'], ru), ('dealer', rd)
    else:
        winner, loser = ('dealer', rd), (usr['name'], ru)

    return calc(usr, bet, winner, loser)


def calc(usr, bet, winner, loser):
    doubled = dbl(winner[1]) and not dbl(loser[1])
    stake =  bet * (1 + doubled)
    if usr['name'] in winner:
        usr['money'] += stake
    else:
        usr['money'] -= stake

    print("{}{} win{}, {}{} lose, {}'s money={}".format(*winner, '(x2)'*doubled, *loser, *usr.values()))
    return usr['money'] > 0


usrs = [{'name':n, 'money':seed(n)} for n in ('User1', 'User2', 'User3')]
while len(usrs) > 1:
    usr = usrs.pop(0)
    usrs += [usr] if play(usr, bet(usr)) else []
    print()

last_usr = max(usrs, key=lambda u: u['money'])
print('Finally {} win, money={}'.format(*last_usr.values()))