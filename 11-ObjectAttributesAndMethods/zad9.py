import random
class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def konstruktor(number_of_array_elements, value_of_array_elements):
        arr=[]
        for i in range(number_of_array_elements):
            arr.append(value_of_array_elements)
        print(arr)

    @staticmethod
    def zakres(number_of_array_elements, value_from, value_to):
        arr=[]
        for i in range(number_of_array_elements):
            arr.append(random.randint(value_from,value_to))
        print(arr)

    @staticmethod
    def determinator(array, value_from, value_to):
        xd=0


my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.konstruktor(3,4)
Arrays.zakres(5,4,22)