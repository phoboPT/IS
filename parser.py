import csv

f = open('C:\\Users\\Phobo\\Desktop\\data.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
	data.append(row)
f.close()

#print (data[1:])
string="<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?> <Products>"
def convert_row(row):
    return """<Item>
	<Item_ID>%s</Item_ID>
    <Item_W>%s</Item_W>
    <Item_Type>%s</Item_Type>
    <Item_MRP>%s</Item_MRP>
    <Outlet_ID>%s</Outlet_ID>
    <Outlet_Year>%s</Outlet_Year>
    <Otlet_Size>%s</Otlet_Size>
	<Outlet_Lotation_Type>%s</Outlet_Lotation_Type>
	<Sales>%s</Sales>
	
</Item>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

string=string+ ('\n'.join([convert_row(row) for row in data[1:]]))+"</Products>"

f = open('C:\\Users\\Phobo\\Desktop\\parsedData.xml',"w")
f.write(string)