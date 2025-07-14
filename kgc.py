string=input("enter a string:")
v="aeiouAEIOU"
d="123456789"
c="bcdfghklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
cov=0
coc=0
cod=0
cos=0
for ch in string:
    if ch in v:
        cov=cov+1
    elif ch in d:
        cod=cod+1
    elif ch in c:
        coc=coc+1
    else:
        cos=cos+1
print(cov)
print(cod)
print(coc)
print(cos)
