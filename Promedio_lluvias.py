

import xlrd
switch=False
arreglo=[]
while switch == False:
    print("\t-----Programa que busca dentro de un archivo excel-----\t")
    print("\t-------------------------------------------------------")
    estado=int(input('\tQue estado(1-32)?:'))
    anio=int(input("\taño(1985-2019)?:"))
    mes=int(input("\tmes(1-12)?:"))
    año=anio
    meses=mes
    est=estado
    if año >= 1985 and año <= 2019:
        for anio in range(1985,2019):
            anio_lista=[]
            archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
            hoja=archivo.sheet_by_index(0)
        if est >= 1 and est < 34:
            for estado in range(2,34):
                mes_lista=[]
                if meses > 0 and meses < 14:
                    for mes in range(1,13):
                        mes_lista.append("%.2f" % hoja.cell_value(estado,mes))
                    anio_lista.append(mes_lista)
            arreglo.append(anio_lista)
        print(f"\tel promedio mensual es:{arreglo[año-1985][est-1][meses-1]}")
    else:
        print("\tLos parametros introducidos no son validos")

    if input("\tDeseas consultar otra fecha? (S/N)") == "N":
        print("\tGracias por ejecutar")
        switch = True
    else:
        switch=False
        
