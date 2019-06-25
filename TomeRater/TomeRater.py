class User(object):
    def __init__(self, name, email):
        self.name = name #name is a string
        self.email = email #email is a string
        self.books = {} #books is a dictionary that will map a book object
    def get_email(self):
        return self.email
    def change_email(self, new_email):
        self.email = new_email
        return "Thanks for updating your email! Your new email is: " + self.email
    def __repr__(self):
        return_statement = "Username: " + self.name + ". Email Address: " + self.email + ". Books Read: " + str(list(self.books.values()))
        return return_statement
        #make sure the self.books is what is needed
    def __eq__(self, other_user):
        if (other_user == self.name):
            other_user == self
    def read_book(self, book, rating=None):
        self.books[book] = rating
    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for rating in self.books.values():
            print(rating)
            ratings_total += rating
        average_rating = ratings_total / len(self.books)
        return average_rating

class Book:
    def __init__(self, title, isbn):
        self.title = title #title is a string
        self.isbn = isbn #isbn is a number
        self.rating = []
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been updated. It is now: " + str(new_isbn)
    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.rating.append(rating)
        else:
            print("Invalid Rating")
    def __eq__(self, book_object):
        if book_object.title == self.title and book_object.isbn == self.isbn:
            book_object = self
    def get_average_rating(self):
        average_rating = 0
        ratings_totals = 0
        for rating in self.ratings:
            ratings_totals += rating
        average_rating = ratings_totals / len(self.ratings)
        return average_rating
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author = self.author)

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject # subject will be a string, like 'Geology'
        self.level = level # level will be a string like "advanced"
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{title}, a {level} book on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
    #"""
    # dictionaries: self.users, self.books
    #"""
    def __init__(self):
        self.users = {} # dictionary maps email to user object
        self.books = {} # dictionary maps book object to num of users that have read it
    def create_book(self, title, isbn):
        return Book(title, isbn)
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    def create_non_fiction(self, title, subject, level, isbn):
        nonfiction_object = NonFiction(title, subject, level, isbn)
        return nonfiction_object
        # Institutionalized by Suicidal Tendencies

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))
    def add_user(self, name, email, user_books = None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
                #_-- saucy girl <-- <-
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    def print_users(self):
        for value in self.users.keys():
            print(value)
    def most_read_book(self):
        read_most = None
        read_count = 0
        for book in self.books.keys():
            if self.books[book] > read_count:
                read_count = self.books[book]
            if self.books[book] == read_count:
                read_most = book
        return read_most
        #------
    def highest_rated_book(self):
        book_best = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                book_best = book
        return book_best
                #---
        #book_best = ""
        #for book in self.books.keys():
        #    book_object = Book.get_average_rating(self)
        #    if book_object > book_best:
        #        book_object = book_best
        #return book_best
    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_user = user
        return highest_user
        #------------
        #user_best = 0
        #for user in self.users.values():
        #    user_object = User.get_average_rating()
        #    print(user_best)
        #    print(user_object)
        #    if user_object > float(user_best):
        #        user_best = user_object
        #return user_best

def hi():
    return 'hi'

#TomeRater = TomeRater()
#test_users = TomeRater.add_user("ClaireBookworm", "myemail@gmail.com", ["Hello"])
#test_books = TomeRater.most_read_book()
#TomeRater.add_user("Marvin Minsky", "marvin@mit.edu", ["Books", "novel1", "nonfiction1"])

#--- populate
#from TomeRater import *
#import TomeRater as TR

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
#print(book1.title)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
print(novel1.isbn)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
print(Tome_Rater.print_users())
#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])

print(Tome_Rater.print_users())
#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

print(Tome_Rater.books)
#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print(Tome_Rater.books)
print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
