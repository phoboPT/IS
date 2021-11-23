import xmlParser
import psycopg2
from datetime import date
from config import config
# buscar os dados
xmlData = None
# BD
params = config()
conn = None


def insert(name, file):
    try:
        populateData(file)
        connect()
        cur = conn.cursor()
        # insert
        print('Inserting...')
        cur.execute("""INSERT INTO xml(xml, name, "createdAt") VALUES ('%s','%s','%s');""" %
                    (xmlData, name, date.today(),))
        conn.commit()
        cur.close()
        return("Successfully inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            close()


def getAllProductsName():
    try:
        connect()
        cur = conn.cursor()
        # insert
        cur.execute(
            """select xpath('//File/Items/Item/@name' , xml) from xml;""")
        data = cur.fetchall()

        cur.close()
        return data

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            close()


def getProductsFromOutletById(id):

    try:
        connect()
        cur = conn.cursor()
        # insert
        cur.execute(
            f"""select xpath('//File/Products/Item[Outlet_ID=\"{id}\"]' , xml) from xml;""")
        data = cur.fetchall()

        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            close()


def getSellsByAmmount(ammount):
    try:
        connect()
        cur = conn.cursor()
        # insert
        cur.execute(
            f"""select xpath('//File/Products/Item[Sales>\"{ammount}\"]/Outlet_Year/text()' , xml) from xml;""")
        data = cur.fetchall()

        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            close()


def getProductsBetweenIds(id1, id2):
    try:
        connect()
        cur = conn.cursor()
        # insert
        cur.execute(
            f"""select xpath('//File/Products/Item[@id>=\"{id1}\" and @id<\"{id2}\"]' , xml) from xml;""")
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            close()


def getAllSellsByProductId(id):
    try:
        connect()
        cur = conn.cursor()
        # insert
        cur.execute(
            f"""select xpath('//File/Types/Type[@id={id}]/@name', xml) tipo, xpath('sum(//File/Products/Item[@type_id={id}]/Sales)', xml) from xml """)
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            close()


def connect():
    # connect to the PostgreSQL server
    global conn
    conn = psycopg2.connect(**params)
    print('Connecting to the PostgreSQL database...')


def close():
    conn.close()
    print('Database connection closed.')


def populateData(file):
    global xmlData
    xmlData = xmlParser.parser(file)
