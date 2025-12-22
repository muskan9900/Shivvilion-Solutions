""" Design a library system with late fine calculation.
Requirements:
        Class Book → title, author, book_id
        Class Member → name, member_id
        Class Library containing list of Books & Members
Implement:
        Issue a book
        Return a book
        Calculate fine if returned late
Fine rule:
    ₹5 per extra day after 7 days
Track which member has borrowed which book. """

class Book:
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=int(book_id)

    def __str__(self):
        return f"{self.title}: {self.author}  by  {self.book_id}"
    

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=int(member_id)
        
    def __str__(self):
        return f"{self.member_id}: {self.name}"


class Library:

    def __init__(self):
    #  dict  to store the following
       self.books={} # stored book_id -> Book class
       self.members={} # member_id -> Members class
       self.issued={} 
       #  book_id -> {member_id,issue day}
       # member_id -> Members class


    # adding books
    def add_books(self,book):
        self.books[book.book_id]= book
        print(f"Book added: {book.title}")
        return True

    # adding members
    def add_members(self,member):
        self.members[member.member_id]= member
        print(f"Members added: {member.name}")
        return True

    
    # issue 
    def issue_book(self,book_id,member_id,issue_day):

        # checking for books
        if book_id not in self.books:
            print("book not found")
            return False
        
        # checking for members
        if member_id not in self.members:
            print("member not found")
            return False
        
        # book issue check
        if book_id in self.issued:
            print("Book already issued!")
            return False
        
        self.issued[book_id]=(member_id,issue_day)
        print(f" Issued {book_id} to {member_id} on  day {issue_day}")
        return True 
    
    #  fine for keeping the book more than 7 days 

    def fine(self,issue_day,return_day,):

        days_kept=return_day-issue_day
        extra=max(0,days_kept-7)
        return extra*5
    
    # returning a book 
    def retun_book(self,book_id,return_day):
        if book_id not in self.issued:
            print("the book was not published")
            return None
        
        member_id,issue_day=self.issued[book_id]
        amount=self.fine(issue_day,return_day)

        # after the returning the delete the book from issue list to make it available
        del self.issued[book_id]
        print(f"Returned {book_id} by {member_id}, Fine= INR {amount}")
        return amount
    
      
    #   tracking of who borrowed and who not
    def who_borrowed(self,book_id):
        if book_id not in self.issued:
            return 
        
        member_id,issue_day= self.issued[book_id]
        return print(f"the {book_id} is borrowed by {self.members[member_id]}")
        
    

    #  creating object

lib=Library()
lib.add_books(Book("THE ROSE","William Shakespeare",101))
lib.add_books(Book("THE GREEN","XYZ",102))
lib.add_members(Member("James",1))
lib.add_members(Member("Alex",2))
lib.issue_book(102,2,20) # day 10 , 101 book id , 1 member 1

# tracking of who borrowed the book 
borrower=lib.who_borrowed(102)
print( borrower)

# returning book (we have kept issue day as 10 so free days are 7 , 3 days extra , per day 5 rupess)
lib.retun_book(102,30)



         

    
