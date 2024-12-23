class Author:
    contracts = []  # Class variable to keep track of all contracts

    def __init__(self, name):
        self.name = name
        self.contracts_list = []  # Instance variable to keep track of contracts for this author

    def contracts(self):
        return self.contracts_list  # Return the author's contracts

    def books(self):
        return [contract.book for contract in self.contracts_list]  # Return books from contracts

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")
        
        contract = Contract(self, book, date, royalties)  # Create a new contract
        self.contracts_list.append(contract)  # Append to the author's contracts
        Author.contracts.append(contract)  # Append to the class variable contracts
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)  # Sum royalties from contracts


class Book:
    books = []  # Class variable to keep track of all books

    def __init__(self, title):
        self.title = title
        Book.books.append(self)  # Append the book to the class variable

    def contracts(self):
        return [contract for contract in Contract.contracts if contract.book == self]  # Return contracts for this book

    def authors(self):
        return [contract.author for contract in Contract.contracts if contract.book == self]  # Return authors for this book


class Contract:
    contracts = []  # Class variable to keep track of all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.contracts.append(self)  # Append the contract to the class variable

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.contracts if contract.date == date]  # Return contracts by date