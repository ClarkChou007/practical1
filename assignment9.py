def f(x):
    y = x**3
    return y
for i in range(100):
    result = f(i)
    name = str(result)
    name = list(name)


    snig =[]
    for num in name:
        num = int(num)
        snig.append(num)
    astring = name[0]

    if len(snig)>1 and sum(snig) == i :
        for j in range(1,len(snig)):
            astring =astring+ "+"
            astring = astring+ name[j]

        print (str(i)+"^3 = "+str(result)+"->"+str(i)+"="+astring)
    elif len(snig) <= 1 and sum(snig) == i:
        print(str(i) + "^3 = " + str(result) )




