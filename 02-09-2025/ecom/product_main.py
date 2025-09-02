import product_manager
from Product import Product

product = Product(101, "nothing phone 3", "flagship", "electronic", "mobile phone", 20, 80000)
product_manager.createProduct(product)
product_manager.readProduct()

# # initializing the seed data with the help of createSalary function
# product = Product(101, "nothing phone 3", "flagship", "electronic", "mobile phone", 20, 80000)
# product_manager.createProduct(product)
# product = Product(102, "nothing phone 2", "mid-range", "electronic", "mobile phone", 40, 30000)
# product_manager.createProduct(product)
# product = Product(103, "nothing phone 1", "mid-range", "electronic", "mobile phone", 40, 25000)
# product_manager.createProduct(product)

# # print all data in salaries list
# resultProducts = product_manager.readProduct()
# for i in resultProducts:
#     print(i)

# # checking the salaries index by using linear search
# print("Salary found at index : ", 101, " : " , product_manager.readByProductId())
# print("Salary found at index : ", 102, " : " , product_manager.readByProductId())
# print("Salary found at index : ", 103, " : " , product_manager.readByProductId())

# # printing the salary by findint the index and print the salary on the index
# # print(product_manager.salaries[product_manager.readBySalary(3000)])

# # checking the update function
# product_manager.updateByProductByPythonWay(101, "nothing phone 3", "flagship", "electronic smart phone", "mobile phone", 10, 90000)
# print(product_manager.readSalary())

# # checking the delete function
# product_manager.deleteByProductId(101)
# print(product_manager.readSalary())