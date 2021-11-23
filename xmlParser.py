import csv
import xmlschema


def parser(name, path):
    print("parsing started")
    f = open(path)
    csv_f = csv.reader(f)
    data = []
    for row in csv_f:
        data.append(row)
    f.close()

    xmlData = {}
    # criar o objeto que vai guardar os items,types e outletSize
    print("Creating the xmlData")
    for item in data[0]:
        xmlData[item] = {}
    # correr o arquivo csv e guardar os valores no xmlData
    for row in data[1:]:
        item = ''
        item_type = ""
        outlet_size = ''
        try:
            item = xmlData[data[0][0]].get(row[0])
            item_type = xmlData[data[0][2]].get(row[2])
            outlet_size = xmlData[data[0][6]].get(row[6])

        except:
            pass
        if item is None:
            xmlData[data[0][0]][row[0]] = {
                'name': row[0], 'id': len(xmlData[data[0][0]])}
        if item_type is None:
            xmlData[data[0][2]][row[2]] = {
                'name': row[2], 'id': len(xmlData[data[0][2]])}
        if outlet_size is None:
            xmlData[data[0][6]][row[6]] = {
                'name': row[6], 'id': len(xmlData[data[0][6]])}

    print("Start creating the string")
    # criar a string que sera o xml final
    string = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?> <File>\n"

    string += "<Items>\n"
    print("Adding items")
    # adcionar os items na string a partir do xmlData
    for item in xmlData[data[0][0]]:
        string += f"""    <Item name=\"{xmlData[data[0][0]][item]['name']}\" id=\"{xmlData[data[0][0]][item]['id']}\"></Item>\n"""

    string += "</Items>\n"

    print('Addind types')
    string += "<Types>\n"
    # adcionar os tipos na string a partir do xmlData
    for a in xmlData[data[0][2]]:
        try:
            string += f"""    <Type name=\"{xmlData[data[0][2]][a]['name']}\" id=\"{xmlData[data[0][2]][a]['id']}\"></Type>\n"""
        except:
            pass
    string += "</Types>\n"
    print('Adding outlet sizes')
    string += "<OutletSizes>\n"
    # adcionar os tipos na string a partir do xmlData
    for a in xmlData[data[0][6]]:
        try:
            string += f"""    <OutletSize name=\"{xmlData[data[0][6]][a]['name']}\" id=\"{xmlData[data[0][6]][a]['id']}\"></OutletSize>\n"""
        except:
            pass
    string += "</OutletSizes>\n"

    print('Adding products')
    string += "<Products>\n"
    # corre o arquivo csv e adciona os produtos na string
    for row in data[1:]:
        try:
            format_float = "{:.2f}".format(float(row[8]))
            string += f"""<Item id=\"{xmlData[data[0][0]].get(row[0])['id']}\" type_id=\"{xmlData[data[0][2]].get(row[2])['id']}\" outlet_size_id=\"{xmlData[data[0][6]][row[6]]['id']}\">
                <Item_W > {row[1]} </Item_W >
                <Item_MRP>{row[3]}</Item_MRP>
                <Outlet_ID>{row[4]}</Outlet_ID>
                <Outlet_Year>{row[5]}</Outlet_Year>
                <Outlet_Lotation_Type>{row[7]}</Outlet_Lotation_Type>
                <Sales>{format_float}</Sales>\n</Item>\n"""

        except:
            pass
    # tags para fechar o xml
    string += "</Products></File>"
    print("Done")
    # grava o xml
    f = open(f'C:\\Users\\Phobo\\Desktop\\IS\\XML\\{name}.xml', "w")
    f.write(string)
    f.close()
    # validar o xml
    print("testing")
    my_schema = xmlschema.XMLSchema(
        'C:\\Users\\Phobo\\Desktop\\IS\\schema.xsd')
    is_valid = my_schema.is_valid(
        f'C:\\Users\\Phobo\\Desktop\\IS\\XML\\{name}.xml')
    text = '' if (is_valid) else 'in'
    print(f'The XML is {text}valid')
    return string
