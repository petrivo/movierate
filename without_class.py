from movierate.movie import Movie

movie_list = list("ABCD")
movies = []

for movie in movie_list:
    mov = Movie(title=movie)
    movies.append(mov)

preferences = []

def insert(arr, el):

    if len(arr) == 0:
        arr.append(el)
        return arr

    def binary_insert(arr, el, init):
        midpoint = len(arr) // 2
        print("realmidpoint", midpoint)
        print("midpoint", arr[midpoint])
        print("init", init)
        userpick(arr[midpoint], el)
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


def userpick(mov, other):
    preferred = input('Which movie you like better, 0:{0} or 1:{1}? ' \
                      .format(mov.title, other.title))
    if int(preferred):
        other.like_more_than(mov)
    else:
        mov.like_more_than(other)

# # arr = [1, 3, 4, 7, 9, 11, 22]
# arr = [1]
# print(insert(arr, 0))
# print(insert(arr, 3))

# print(insert(arr, 2))

for mov in movies:
    insert(preferences, mov)

for pref in preferences:
    print(pref.title)