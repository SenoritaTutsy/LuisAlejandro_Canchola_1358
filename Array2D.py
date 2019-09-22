class Array2D:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__data = []
        for r in range(rows):
            tmp = []
            for c in range(cols):
                tmp.append(None)
            self.__data.append(tmp)

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def clearing(self, value):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.__data[r][c] = value

    def set_item(self, row, col, value):
        if (row >= 0 and row < self.__rows) and (col >= 0 and col < self.__cols):
            self.__data[row][col] = value               

    def get_item(self, row, col):
        if (row >= 0 and row < self.__rows) and (col >= 0 and col < self.__cols):
            return self.__data[row][col]
        
def main():
   """ Array = Array2D(5,5)
    Array.to_string()
    print(f"El numero de renglones", Array.get_num_rows())
    print(f"El numero de columnas", Array.get_num_cols())"""

main()
