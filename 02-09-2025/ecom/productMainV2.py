from product_manager import  createProduct, readProduct, readByProductId, readByProductId, updateByProductByPythonWay, deleteByProductId
from Product import Product
def menu():
    message = '''
1 - Create Product
2 - Read All Products
3 - Read by Product
4 - Update
5 - Delete
6 - Exit/ Logout
select option: 
'''
    choice = int(input(message))
    if choice == 1:
        name = input("Name : ")
        description = input("Description : ")
        category = input("Category : ")
        tags = input("Tags : ")
        stock = input("Stock : ")
        price = input("Price : ")
        id = -1
        product = Product(id, name, description, category, tags, stock, price)
        createProduct(product)
        
    elif choice == 2:
        result_prod = readProduct()       
        print('All Products')
        for i in result_prod:
            print(i)
    elif choice == 3:
        id = int(input('Id : '))
        product = readByProductId(id)
        if product == None:
            print("product not found!!")
        print(product)
    elif choice == 4:
        name = None
        description = None
        category = None
        tags = None
        stock = None
        price = None
        id = int(input("Enter id : "))
        product = readByProductId(id)
        if product == None:
            print("product not found")
        else:
            # if(bool(input(f"Want to update the Name({product.name}): (T|F)")) != "f"):
            #     name = input("Name : ")
            user_input = input(f"Want to update the Name({product.name}): (T|F) ").strip().lower()
            if user_input != "f":
                name = input("Name: ")
            else:
                name = product.name
            # if(bool(input(f"Want to update the Description({product.description}): (T|F)")) != "f"):
            user_input = input(f"Want to update the Description({product.description}): (T|F) ").strip().lower()
            if user_input != "f":
                description = input("Description : ")
            else:
                description = product.description
            # if(bool(input(f"Want to update the Category({product.category}): (T|F)")) != "f"):
            user_input = input(f"Want to update the Category({product.category}): (T|F) ").strip().lower()
            if user_input != "f":
                category = input("Category : ")
            else:
                category = product.category
            # if(bool(input(f"Want to update the Tags({product.tags}): (T|F)")) != "f"):
            user_input = input(f"Want to update the Tag({product.tags}): (T|F) ").strip().lower()
            if user_input != "f":
                tags = input("Tags : ")
            else:
                tags = product.tags
            # if(bool(input(f"Want to update the Stock({product.stock}): (T|F)")) != "f"):
            user_input = input(f"Want to update the Stock({product.stock}): (T|F) ").strip().lower()
            if user_input != "f":
                stock = id(input("Stock : "))
            else:
                stock = product.stock
            # if(bool(input(f"Want to update the Price({product.price}): (T|F)")) != "f"):
            user_input = input(f"Want to update the Price({product.price}): (T|F) ").strip().lower()
            if user_input != "f":
                price = int(input("Price : "))
            else:
                price = product.price

            id = product.id
            updateByProductByPythonWay(Product(id, name, description, category, tags, stock, price))
    elif choice == 5:
        id = int(input('Id of the product that need to be deleted : '))
        product = readByProductId(id)
        if product == None:
            print("product not found!!")
        deleteByProductId(id)
    return choice

def menus():
    print('Salary Management App')
    choice = menu()
    while choice != 6:
        choice = menu()
    print('Thank you for using --Product Management App--')

menus()