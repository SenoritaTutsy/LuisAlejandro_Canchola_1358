from juegodelavida import juegodelavida
import time
import os
def main():
    
    print("--------------------JUEGO DE LA VIDA--------------------------")
    cuad=int(input("-Introduzca el valor del cuadro a generar-"))
    gen=int(input("-cuantas generaciones quieres?-"))+1
    live=int(input("-Celulas vivas?-"))
    inicio=[]
   
    for i in range(live):
        tmp=i+1
        Fil = int(input(f"Fila para celula ({tmp}):"))
        Col = int(input(f"Columna para celula ({tmp}):"))
        inicio.append([(Fil-1), (Col-1)])
        os.system ("cls") 
    partida= juegodelavida(cuad,cuad,gen,inicio)
    print("Iniciando Juego.....")
    time.sleep(2)
    print("       Generacion 1      ")
    partida.to_string()
    print("Celulas vivas:", len(inicio))
    print("--------------------------------------------------------")
    for i in range(2,gen):
        nueva = []
        print(f"       Generacion {i}       ")
        for fila in range(cuad):
            for columna in range(cuad):
                vivos = partida.get_num_live_neighbors(fila, columna)
                if partida.is_live_cell(fila, columna):
                    if vivos == 3 or vivos == 2:
                        nueva.append([fila, columna])
                else:
                    if vivos == 3:
                        nueva.append([fila, columna])         
        partida.configure_next_generation(nueva)
        partida.to_string()
        print("Celulas Vivas:", len(nueva))
        print("--------------------------------------------------------")
    print("_______________________________Generación",i+1," ____________________________")

            
main()
