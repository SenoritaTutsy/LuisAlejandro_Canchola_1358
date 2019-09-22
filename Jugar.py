from juegodelavida import juegodelavida

def main():
    fil=5
    col=5
    
    print("--------------------JUEGO DE LA VIDA--------------------------")
    inicio= [[1,3],[2,2],[2,3],[2,4]]
    for i in range (5):
        partida= juegodelavida(fil,col,i,inicio)
        partida.to_string()
    
        for i in range(2,5):
            nueva = []
            for fila in range(fil):
                for columna in range(col):
                    vivos = partida.get_num_live_neighbors(fila, columna)
                    if partida.is_live_cell(fila, columna):
                        if vivos == 3 or vivos == 2:
                            nueva.append([fila, columna])
                    else:
                        if vivos == 3:
                            nueva.append([fila, columna])         
            partida.configure_next_generation(nueva)
            partida.to_string()
        print("Las celulas vivas son",vivos)
        print("_______________________________Generación",i+1," ____________________________")

            
main()
