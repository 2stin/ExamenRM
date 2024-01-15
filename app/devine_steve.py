def decomposer(n):
    u=n%10
    d=int(n/10)%10
    c=int(n/100)%10
    rep=(c,d,u)
    return rep

def somme(d,c,u):
    return c+u==d

def divisible(n):
    return n%9==0

def devine():
    code=100
    trouve=False
    while code <=999 and not trouve:
        (c,d,u)=decomposer(code)
        if somme(c,d,u) and divisible(code):
            trouve=True
        else: code=code+1
    return code

print(devine())