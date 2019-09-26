class Array3D:
    def __init__(self, rows, cols, depth):
        self.__data = []
        self.__rows = rows
        self.__cols = cols
        self.__depth = depth
        for d in range(depth):
            tmp1 = []
            for r in range(rows):
                tmp2 = []
                for c in range(cols):
                    tmp2.append(None)
                tmp1.append(tmp2)
            self.__data.append(tmp1)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_num_depth(self):
        return self.__depth

    def set_item(self, row, col, depth, value):
        if (row >= 0 and row < self.__rows) and (col >= 0 and col < self.__cols) and (depth >= 0 and depth < self.__depth):
            self.__data[depth][row][col] = value
        else:
            print("Los valores de r, c y d no están en el rango")

    def get_item(self, row, col, depth):
        if (row >= 0 and row < self.__rows) and (col >= 0 and col < self.__cols) and (depth >= 0 and depth < self.__depth):
            print(self.__data[depth][row][col])
        else:
            print("Los valores de r, c y d no están en el rango")

    def clearing(self, value):
        for d in range(self.__depth):
            for r in range(self.__rows):
                for c in range(self.__cols):
                    self.__data[d][r][c] = value

    def to_string(self):
        print(self.__data)

#Pruebas
"""def main():
    Array = Array3D(3,3,3)
    Array.to_string()
    Array.clearing(0)
    Array.to_string()
    Array.get_num_rows()
    Array.get_num_cols()
    Array.get_num_depth()
    Array.set_item(2,2,2,20)
    Array.get_item(2,2,2)
    Array.to_string()
   
main()"""
