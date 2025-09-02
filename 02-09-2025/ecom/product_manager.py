products = []

def createProduct(product):
    global products
    if len(products) == 0:
        product.id = 1
    else:
        product.id = products[len(products)] + 1
    products.append(product)

def readProduct():
    global products
    return products

def readByProductTags(tag):
    for i in range(len(products)):
        if tag in products[i].tags:
            return products[i]
    return None

def readByProductId(id):
    for product in products:
        if id == product.id:
            return products
    return None

def readByProductTagsByPythonWay(tag):
    for product in products:
        if tag in product.tags:
            return product
    return None

def readByProductId(id):
    for product in products:
        if id == product.id:
            return product
    return None

def updateByProduct(updatedProduct):
    global products
    for i in range(len(products)):
        if products[i].id == updatedProduct.id:
            products[i].name = updatedProduct.name
            products[i].description = updatedProduct.description
            products[i].category = updatedProduct.category
            products[i].tags = updatedProduct.tags
            products[i].stock = updatedProduct.stock
            products[i].price = updatedProduct.price
            return 1
    return -1

def updateByProductByPythonWay(product):
    old_product = readByProductId(product.id)
    if old_product == None:
        return
    # createProduct(product)
    old_product.name = product.name
    old_product.description = product.description
    old_product.category = product.category
    old_product.tags = product.tags
    old_product.stock = product.stock
    old_product.price = product.price
    # return -1

def deleteByProductByTag(tag):
    global products
    for i in range(len(products)):
        if tag in products[i].tags:
            products.remove(products[i])
            return 1
    return -1

def deleteByProductId(id):
    products.remove(readByProductId(id))