import xmlrpc.client
import csv

rpc = xmlrpc.client.ServerProxy('http://localhost:8000')


def insert(name):
    try:
        f = open('C:\\Users\\Phobo\\Desktop\\IS\\234.csv')
        csv_f = csv.reader(f)
        data = []
        for row in csv_f:
            data.append(row)
        f.close()
        data = rpc.insert(name, data)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getAllProducts():
    try:
        data = rpc.getAllProducts()
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getProductsFromOutletById(id):
    try:
        data = rpc.getProductsFromOutletById(id)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getSellsByAmmount(ammount):
    try:
        data = rpc.getProductsFromOutletById(ammount)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getProductsBetweenIds(id1, id2):
    try:
        data = rpc.getProductsFromOutletById(id1, id2)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


def getAllSellsByProductId(id):
    try:
        data = rpc.getProductsFromOutletById(id)
        print(data)

    except (Exception) as error:
        print(error)
    finally:
        print('exit')


insert("teste")
getProductsFromOutletById()
