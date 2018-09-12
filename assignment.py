fruits = ['apple', 'pear', 'orange', 'pinapple', 'mandarin']
for fruit in fruits:
    if fruit == 'apple':
        print("I find it!")
fruits.append('bannana')
fruits.append('kiwi')
newfruit =[]
for fruit in fruits:
    newfruit.append(fruit)
for item in newfruit:
    if len(item)==1:
        print(item.title()  + " has 1 letter.")
    else:
        print(item.title() + " has "+str(len(item))+" letters.")
