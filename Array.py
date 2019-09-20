#ADT Array
class Array:
    def __init__(self, n):
        self.__data = []
        for i in range(n):
            self.__data.append(None)

    def to_string(self):
        print(self.__data)

    def get_length(self):
        return len(self.__data)

    def set_item(self, index, value):
        if index >= 0 and index <= len(self._data):
            self.__data[index] = value
        else:
            print("Elige otro numero")

    def get_item(self, index):
        if index >= 0 and index <= len(self.__data):
            return self.__data[index]
        else:
            print("elige otro numero")

    def clearing(self, valor):
        for i in range(len(self.__data)):
            self.__data[i] = valor

def main():
    arreglo = Array(5)
    arreglo.to_string()
    print(f"El tamaño es de: {arreglo.get_length()}")
    arreglo.set_item(1,10)
    arreglo.to_string()
    print(f"El elemento 1 es {arreglo.get_item(1)}")
    arreglo.get_item(20)
    arreglo.clearing(10)
    arreglo.to_string()

main()
