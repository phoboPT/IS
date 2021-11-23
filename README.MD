Instalar dependencias

1.   pip install xmlrpc
2.   pip install psycopg2
3.   pip install xmlschema
4.   pip install csv



Garantir que o PostgreSQL está instalado e a rodar

  Configurar database.ini

  

```
  [postgresql]

​    host=localhost

​    database=xml

​    user=postgres

​    password=root
```



Correr servidor

 

```
 python3 RPCServer.py
```



Correr cliente

  

```
python3 RPCClient.py
```

