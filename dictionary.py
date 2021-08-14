def create_dictionary(list1,list2):
    dictionary = {}
    for i in range((len(list1))):
        dictionary[list1[i]] = list2[i]
    return dictionary
    

list1 = list(input("Enter the words: ").strip().split())
list2 = list(map(int,input("Enter the numbers: ").strip().split())) 
create_dictionary(list1,list2)
def my_dictionary(list1,list2):
    dict1 = create_dictionary(list1,list2)
    a = int(input('Enter the integer: '))
    index = 0
    for k,v in dict1.items():
        if a == v:
            return index
        index+=1
            

my_dictionary(list1,list2)
    