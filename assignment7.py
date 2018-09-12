print( "Please enter three numbers, seperate them by Taping Enter key. ")
a = input("First:")
b = input("Second:")
c = input("Third:")
def sort(a,b,c):
    d = max(a,b)
    e = max(b,c)
    f = max(a,c)
    if d <c:
        d,c = c,d
        if a<b:
            return d,b,a
        else:
            return d,a,b
    elif a>e:

        if b<c:
            b,c= c,b
            return a,b,c
        else:
            return a,b,c
    elif b>f:
        if a<c:
            a,c=c,a
            a,b = b,a
            return a,b,c
        else:
            a,b= b,a
            return a,b,c

print(sort(a,b,c))
