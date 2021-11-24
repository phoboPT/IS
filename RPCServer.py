from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import dbUtil
import os
import shutil


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class Methods:
    def __init__(self):
        self = self

    def insert(self, name, file):
        print("getting the csv and saving it")
        curDir = os.path.dirname(os.path.realpath(__file__))
        output_file_path = f"{curDir}/CSV/{name}.csv"
        print('output_file_path -> ({})'.format(output_file_path))
        with open(output_file_path, "wb") as handle:
            handle.write(file.data)
            print('Output file: {}'.format(output_file_path))

        return dbUtil.insert(name, output_file_path)

    def getAllProducts(self):
        print("getting all products")
        return dbUtil.getAllProductsName()

    def getProductsFromOutletById(self, id):
        print("getting products from outlet by id")
        return dbUtil.getProductsFromOutletById(id)

    def getSellsByAmmount(self, ammount):
        print("getting sells by ammount", ammount)
        return dbUtil.getSellsByAmmount(ammount)

    def getProductsBetweenIds(self, id1, id2):
        print("getting products between ids")
        return dbUtil.getProductsBetweenIds(id1, id2)

    def getAllSellsByProductId(self, id):
        print("getting all sells by product id")
        return dbUtil.getAllSellsByProductId(id)

    def delete(self, name):
        print("deleting the csv")
        shutil.move(f"{os.path.dirname(os.path.realpath(__file__))}/CSV/{name}.csv",
                    f"{os.path.dirname(os.path.realpath(__file__))}/deleted/CSV/{name}.csv")
        shutil.move(f"{os.path.dirname(os.path.realpath(__file__))}/XML/{name}.xml",
                    f"{os.path.dirname(os.path.realpath(__file__))}/deleted/XML/{name}.xml")
        return dbUtil.deleteByName(name)


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()
    server.register_instance(Methods())
    # Run the server's main loop
    server.serve_forever()
