class Book:
    def __init__(self, title, author, publisher, publication_year, genre, summary, contents, serial_number, current_location, checkout_time):
        self.title = title
        """"""
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre
        self.summary = summary
        self.contents = contents
        self.serial_number = serial_number
        self.current_location = current_location
        self.checkout_time = checkout_time
        """"""

    def __str__(self):
        return (f"Title: {self.title}\n"
                """)"""
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Publication Year: {self.publication_year}\n"
                f"Genre: {self.genre}\n"
                f"Summary: {self.summary}\n"
                f"Contents: {self.contents}\n"
                f"Serial Number: {self.serial_number}\n"
                f"Current Location: {self.current_location}\n"
                f"Checkout Time: {self.checkout_time}")
    
    def __repr__(self):
        return self.__str__()