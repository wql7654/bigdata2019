import sys


def greet_users(usernames):
       usernames=usernames[0].upper()+usernames[1:]
       return usernames

usernames=sys.argv[1:]

print(usernames)

for name in usernames:
    name = greet_users(name)
    print("hello,%s !"%name )