import xmlParser
import psycopg2
from config import config
# buscar os dados
xmlData = xmlParser.parser()
# BD
params = config()

# connect to the PostgreSQL server
print('Connecting to the PostgreSQL database...')

conn = psycopg2.connect(**params)


def insert():
    try:
        cur = conn.cursor()
        # insert
        cur.execute("""INSERT INTO xml(xml, name, "createdAt") VALUES ('%s','%s','%s');""" %
                    (xmlData, "teste", "2021-11-19",)
                    )
        conn.commit()
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# chama insert
insert()
