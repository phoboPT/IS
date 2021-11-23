from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import dbUtil


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    def insert(name, file):
        return dbUtil.insert(name, file)

    def getAllProducts():
        return dbUtil.getAllProductsName()

    def getProductsFromOutletById(id):
        return dbUtil.getProductsFromOutletById(id)

    def getSellsByAmmount(ammount):
        return dbUtil.getSellsByAmmount(ammount)

    def getProductsBetweenIds(id1, id2):
        return dbUtil.getProductsBetweenIds(id1, id2)

    def getAllSellsByProductId(id):
        return dbUtil.getAllSellsByProductId(id)

    server.register_function(getAllProducts, 'getAllProducts')
    server.register_function(insert, 'insert')
    server.register_function(getProductsFromOutletById,
                             'getProductsFromOutletById')
    server.register_function(getSellsByAmmount, 'getSellsByAmmount')
    server.register_function(getProductsBetweenIds, 'getProductsBetweenIds')
    server.register_function(getAllSellsByProductId, 'getAllSellsByProductId')

    # Run the server's main loop
    server.serve_forever()
