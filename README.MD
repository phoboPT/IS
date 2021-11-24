#### Implementação de um servidor/cliente em python utilizando o RPC

##### Objetivo do projeto

Este projeto implementa um servidor e cliente em RPC utilizando python com o objetivo de utilizar os métodos RPC para enviar arquivos csv para serem processados.

O cliente envia um arquivo csv para o servidor, que é responsável por dar parse e criar um arquivo xml com a informação retirada do csv. Os dados do xml são depois inseridos numa database. Todos os ficheiros xml são validados para garantir que estão corretos. 

São implementas alguns metodos para pesquisas utilizando o xpath e xquery para otimizar as pesquisas na BD.

##### Instalar dependencias

1.   pip install xmlrpc
2.   pip install psycopg2
3.   pip install xmlschema



##### Garantir que o PostgreSQL está instalado e a rodar

######  Configurar database.ini  

```
  [postgresql]

​    host=localhost

​    database=xml

​    user=postgres

​    password=root
```



##### Correr servidor 

```
 python3 RPCServer.py
```



##### Correr cliente  

```
python3 RPCClient.py
```

