class Library:
    def __init__(self):
        self.file=open("books.txt","a+")
        
    def __del__(self):
        print("Destructor")
        self.file.close()

    def list_book(self):
        self.file.seek(0)
        for line in self.file:
            line_lst=line.split(",")
            if len(line_lst)==1:    #Boş satır varsa bu satırı atla
                continue
            print("Book title:"+ line_lst[0]+", Author name: "+line_lst[1])


    
    def add_book(self):
        title=input("Enter the title of the book:")
        author=input("Enter the name of the author:")
        year=input("Enter the first release year:")
        pages=input("Enter the number of pages:")
        self.file.write("\n"+title+","+author+","+year+","+pages)
        
        
        
    def remove_book(self):
        lst_lines=[]
        title=input("Enter the title of the book you want to remove:")
        self.file.seek(0)
        for line in self.file:
            line_lst=line.split(",")
            if len(line_lst)==1:    #Boş satır varsa bu satırı atla
                continue
            if title in line_lst:
                continue
            lst_lines.append(line)
        self.file.truncate(0)
        for line in lst_lines:
                self.file.write(str(line) + "\n")
        self.list_book()
        
       
        
try:
    lib = Library()
    lib.add_book()
    lib.add_book()
    lib.list_book()
    lib.remove_book()
finally:
    del lib

