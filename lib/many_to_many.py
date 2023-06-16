class Author:
    def __init__(self, name):
        self.name = name
        self.contract_list = []
        self.book_list = []

    def contracts(self):
        return [contract for contract in self.contract_list]
    
    def books(self):
        return [book for book in self.book_list]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contract_list])


class Book:
    def __init__(self, title):
        self.title = title
        self.contract_list = []
        self.author_list = []

    def contracts(self):
        return [contract for contract in self.contract_list]
    
    def authors(self):
        return [author for author in self.author_list]


class Contract:
    all = []

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book 
        self.date = date
        self.royalties = royalties
        self.author.contract_list.append(self)
        self.author.book_list.append(self.book)
        self.book.contract_list.append(self)
        self.book.author_list.append(self.author)
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('invalid author type')
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception('invalid book type')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception('invalid date')
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception('invalid royalty')
        
author = Author("Name")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
contract1 = Contract(author, book1, "02/01/2001", 10)
contract2 = Contract(author, book2, "01/01/2001", 20)
contract3 = Contract(author, book3, "03/01/2001", 30)