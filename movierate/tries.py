movies = list('ab')

for i in range(len(movies)):
    curr = movies[i]
    for e in movies[i+1:]:  
        print(curr + e)
# print(movies[1:])