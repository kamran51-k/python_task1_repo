def open_file(): 
        f = open('bestsellers.txt','r')
        list1 = []
        for line in f:
            a = line.strip().split('\t')
            list1.append(a)
        return list1             
def month_range():
    a = open_file()
    year_input = input('enter the year: ')
    month_input = input('enter the month: ')
    c = list()
    for i in a:
            m = i[3].strip().split('/')
            if year_input == m[2] and month_input == m[0]:
                     c.append(i[0])
    return c
def str_range():
        a = open_file()
        b = input('enter the string: ')
        c = list()
        for i in a:
                if b in i[0]:
                        c.append(i[0])
        return c
def if_range():
     k = """ 
     What would you like to do?
     1: Look up year range
     2: Look up month/year
     3: Search for author
     4: Search for title
     Q: Quit
             """
     while True:
           print(k)
           c = input()
           if c == '2':
                   print(month_range())
           elif c == '3':
                   print(str_range())
           elif c == 'Q' or c == 'q':
                   break       
if_range()
