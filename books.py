class books:
    def __init__(self,name,author,ageRating):
        self.name=name
        self.author=author
        self.ageRating=ageRating
        
    def book_info(self):
        print("name: "+self.name)
        print("author: "+self.author)
        print("ageRating: "+self.ageRating)
        print("\n")
        
        
book1=books("harry potter","J.K. Rowling","for children")
book1.book_info()
book2=books("The school boy","Ruskin Bond","for children")
book2.book_info()