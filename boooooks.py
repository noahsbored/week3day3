class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print("Author:", self.author)



my_book = Book("123", "diary of a wimpy kid rodricks rules", 1000000000, "jeff kinney")
my_book.display_info()
