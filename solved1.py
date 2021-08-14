def best_things_ever():
    a = open('best_things_ever.txt','r')
    b = a.read()
    c = b.split(',')
    for i in c:
        print(i)
best_things_ever()