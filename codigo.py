import csv

import MySQLdb

mydb =  MySQLdb.connect(host="127.0.0.1",user="root" ,password="root", database="registro")

with open ('Reporte_Tiempos_Geocercas.csv') as csv_file:
    csv_file = csv.reader(csv_file, delimiter=',')
    all_value = []
    for row in csv_file:
        value =(row[0],row[1],row[2],row[3],row[4],row[5])
        all_value.append(value)

query = "insert into guardar (veiculo,rastra,nombre,geocerca,fecha_Entrada,fecha_salida,dif_tiempo) values (%s,%s,%s,%s,%s,%s)"
     
mycursor = mydb.cursor()
mycursor.executemany(query,all_value)
mydb.commit()