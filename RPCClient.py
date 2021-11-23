import xmlrpc.client
import csv
import os
rpc = xmlrpc.client.ServerProxy('http://localhost:8000')


def insert(name):
    try:
        print("Sending csv file to the server")
        with open("C:\\Users\\Phobo\\Desktop\\IS\\234.csv", "rb") as handle:
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
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getProductsFromOutletById(id):
    try:
        print("Getting all products from outlet by id from the server")
        data = rpc.getProductsFromOutletById(id)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getSellsByAmmount(ammount):
    try:
        print("Getting all sells by ammount from the server")
        data = rpc.getProductsFromOutletById(ammount)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getProductsBetweenIds(id1, id2):
    try:
        print("Getting all products between ids from the server")
        data = rpc.getProductsBetweenIds(id1, id2)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getAllSellsByProductId(id):
    try:
        print("Getting all sells by product id from the server")
        data = rpc.getAllSellsByProductId(id)
        print(data)

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


insert("qwer")
# getAllProducts()
# getProductsFromOutletById("OUT035")
# getSellsByAmmount(6000)
# getProductsBetweenIds(13, 16)
# getAllSellsByProductId(1)
delete("qwer")
