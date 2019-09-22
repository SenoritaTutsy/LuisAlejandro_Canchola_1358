'''
Reglas del juego de la vida

Regla 1: si una celula que se encuentra viva tiene 0 o un vecino muere
por soledad para la siguiente generacion. Donde los vecinos son las
8 celulas que lo rodean inmediatamente

Regla 2: Una celula viva que tienen 2 o 3 vecinos sobrevive para la siguiente
generacion

Regla 3: Una celula viva que tiene 4 o mas vecinos mueren por sobrepoblacion
para la siguiente generacion

Regla 4: Una celula muerta con exactamente con 3 vecinos vivos resulta en un
nacimiento cuya vida empieza en la siguiente generacion. Todas las
demas celular muertas permanecen muertas para la siguiente  generacion


-Juego de la vida(rows, cols, generacion, poblacion_inicial)
-get_num_rows()
-get_num_cols()
-configure_next_gen(nueva_poblacion)
-set_cell_death_(rows,col)
-set_cell_alive(row,col)
-is_live_cell(row,col)->boolean
-get_num_live_neighbors(row,col)
'''
from Array2D import Array2D

class juegodelavida:

    def __init__(self,rows,cols,generaciones,poblacion_inicial):
        self.__cuadro=Array2D(rows,cols)
        self.__filas=rows
        self.__columnas = cols
        self.__generaciones = generaciones
        '''
        poblacion_inicial = [[1,3],[2,2],[2,3],[2,4]]
        '''
        self.__cuadro.clearing(0)
        for cell in poblacion_inicial:
            self.__cuadro.set_item(cell[0],cell[1],1)

    def to_string(self):
        self.__cuadro.to_string()

    def configure_next_generation(self,nueva_generacion): #Nueva Generacion = [[][][][]]
        self.__cuadro.clearing(0)
        for cell in nueva_generacion:
            self.__cuadro.set_item(cell[0],cell[1],1)

    def set_cell_death(self,rows,col):
        self.__cuadro._set_item(row,col,0)

    def set_cell_alive(self,row,col):
        self.__cuadro.set_item(row,col,1)

    def is_live_cell(self,row,col):
        return self.__cuadro.get_item(row,col) ==1

    def get_num_live_neighbors(self,row,col):
        limites = self.calcula_vecinos(row,col)
        cont=0
        for fila in range(limites[0],limites[2]+1,1):
            for cols in range(limites[1],limites[3]+1,1):
                if fila == row and cols == col:
                    pass
                else:
                    if self.is_live_cell(fila,cols)==1:
                        cont+=1
        return cont
                    
    def calcula_vecinos(self,y ,x ):
        #[y_ini, x_ini, y_fin, x_fin]
        vecinos=[y-1,x-1,y+1,x+1]
        if vecinos[0]==-1:
            vecinos[0] = 0
        if vecinos[1]== -1:
            vecinos[1] = 0
        if vecinos[2] == self.__columnas:
            vecinos[2] = self.__columnas -1
        if vecinos[3]== self.__filas:
            vecinos[3] = self.__filas -1
        return vecinos

#pruebas
'''def main():
    inicial= [[1,3],[2,2],[2,3],[2,4]]
    juego = JuegoDeLaVida(5,5,4,inicial)
    juego.to_string()
    vivos = juego.get_num_live_neighbors(4,4)
    for r in range(5):
        for c in range(5):
            print(f'[{r}][{c}] = {juego.get_num_live_neighbors( r, c)}')

main()'''
