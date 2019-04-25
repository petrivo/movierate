def insert(arr, el):

    if len(arr) == 0:
        arr.append(el)
        return arr

    def binary_insert(arr, el, init):
        midpoint = len(arr) // 2
        print("realmidpoint", midpoint)
        print("midpoint", arr[midpoint])
        print("init", init)
        if arr[midpoint] > el:
            print(arr)
            if len(arr) == 1:
                index = init.index(arr[0])
                if index < 0:
                    index = 0
                init.insert(index, el)
                return ("1", init)
            binary_insert(arr[:midpoint], el, init)
            return ("2", init)
        elif arr[midpoint] < el:
            print(arr)

            if len(arr) == 1:
                index = init.index(arr[0]) + 1
                init.insert(index, el)
                return ("3", init)
            if len(arr) <= midpoint+1:
                binary_insert(arr[midpoint:], el, init)            
            else:
                binary_insert(arr[midpoint+1:], el, init)
            # except IndexError:
            #     binary_insert(arr[midpoint:], el, init)
            return ("4", init)
        else:
            return "5"

    return binary_insert(arr, el, arr)


arr = [1]

print(insert(arr, 2))
print(insert(arr, 0))
print(insert(arr, 8))
print(insert(arr, 3))
print(insert(arr, 324))
print(insert(arr, 31))
print(insert(arr, -3))
print(insert(arr, 2))
print(insert(arr, 12))