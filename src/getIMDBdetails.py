import imdb

ia=imdb.IMDb()
m = ia.search_movie('$x')
print(m[0]['MovieId'])
