import xmlrpc.client
import os
rpc = xmlrpc.client.ServerProxy('http://localhost:8000')


def saveToFile(name, data, extension="xml"):
    try:
        f = open(
            f"{os.path.dirname(os.path.realpath(__file__))}/client/{name}.{extension}", "w")
        f.write(" ".join(map(str, data)))
        f.close()
    except (Exception) as error:
        print(error)


def insert(name):
    try:
        print("Sending csv file to the server")
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/{name}.csv", "rb") as handle:
            binary_data = xmlrpc.client.Binary(handle.read())

            data = rpc.insert(name, binary_data)
            print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getAllProducts():
    try:
        print("Getting all products from the server")
        data = rpc.getAllProducts()
        saveToFile("allProducts", data, "txt")

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getProductsFromOutletById(id):
    try:
        print("Getting all products from outlet by id from the server")
        data = rpc.getProductsFromOutletById(id)
        saveToFile("productsFromOutletById", data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getSellsByAmmount(ammount):
    try:
        print("Getting all sells by ammount from the server")
        data = rpc.getSellsByAmmount(ammount)
        print(data)
        saveToFile("sellsByAmmount", data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getProductsBetweenIds(id1, id2):
    try:
        print("Getting all products between ids from the server")
        data = rpc.getProductsBetweenIds(id1, id2)
        saveToFile("productsBetweenIds", data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getAllSellsByProductId(id):
    try:
        print("Getting all sells by product id from the server")
        data = rpc.getAllSellsByProductId(id)

        saveToFile("allSellsByProductId", data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def delete(name):
    try:
        print("Deleting files from the server")
        data = rpc.delete(name)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


insert("234")
getAllProducts()
getProductsFromOutletById("OUT035")
getSellsByAmmount(1000)
getProductsBetweenIds(13, 16)
getAllSellsByProductId(1)
delete("234")
