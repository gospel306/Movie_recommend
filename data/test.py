f = open("movies.txt", 'w')
movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
head = ""
for movie in movie_data.readlines():
    break