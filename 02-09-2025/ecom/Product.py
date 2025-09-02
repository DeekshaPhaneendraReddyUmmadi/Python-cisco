class Product:
    def __init__(self, id, name, description, category, tags, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price

    def __str__(self):
        return f'[id={self.id}, name={self.name}, description={self.description}, catergory={self.category}, tags={self.tags}, stock={self.stock}, price={self.price}]'
    def __repr__(self):
        return self.__str__()
    

# prd = Product(101, "nothing phone 3", "flagship", "electronic", "mobile phone", 20, 80000)

# print(prd)

