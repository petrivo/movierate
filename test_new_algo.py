arr = [1, 3, 4, 7, 9, 11, 22]

class Bin():

    def __init__(self, arr):
        self.arr = arr

    def binary_insert(self, arr, el):

        midpoint = len(arr) // 2
        print(arr[midpoint])
        if arr[midpoint] > el:
            print(arr)
            if len(arr) == 1:
                index = self.arr.index(arr[0]) - 1
                if index < 0:
                    index = 0
                self.arr.insert(index, el)
                return "1"
            self.binary_insert(arr[:midpoint], el)
            return "2"
        elif arr[midpoint] < el:
            print(arr)

            if len(arr) == 1:
                index = self.arr.index(arr[0]) + 1
                self.arr.insert(index, el)
                return "3"
            self.binary_insert(arr[midpoint+1:], el)
            return "4"
        else:
            return "5"


bin = Bin(arr)
rv = bin.binary_insert(arr, -2)

print(bin.arr)

print(rv)

# test class variables
# bin2 = Bin()
# print("bin2rv",  bin2.rv)