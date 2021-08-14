def open_file():
    ''' Remember the docstring'''
    file_name = input("Please enter a filename")
    while(True):
        try:
            f = open(file_name, "r")
            print("Success")
            return f.read()
            break
        except:
            print("Please enter a valid file name")
            file_name = input("Please enter a filename").strip()
            continue
open_file()            
            
            