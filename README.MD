Instalar dependencias
    pip install xmlrpc
    pip install psycopg2
    pip install xmlschema
    pip install csv

Garantir que o PostgreSQL está instalado e a rodar
    Configurar database.ini
        [postgresql]
        host=localhost
        database=xml
        user=postgres
        password=root

Correr servidor
    python3 RPCServer.py

Correr cliente
    python3 RPCClient.py
    