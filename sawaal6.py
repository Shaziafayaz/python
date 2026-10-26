movies = []
movie1 = input("enter your first movie name:")
movie2 = input("enter your second movie name:")
movie3 = input("enter your third movie name:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print("your favourite movies are:",movies)


#can do this also 
movieslist = []
movie = input("enter your first movie name:")
movieslist.append(movie)
movie = input("enter your second movie name:")
movieslist.append(movie)
movie = input("enter your third movie name:")
movieslist.append(movie)

print("your favourite movies are:",movieslist)


#other way
movs = []
movs.append(input("enter favourite movie name:"))
print("your favourite movies is:",movs)