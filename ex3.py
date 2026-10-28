movies = [ 
    ("The Matrix", 1999), 
    ("Avatar", 2009), 
    ("Jurassic Park", 1993), 
    ("Avengers: Endgame", 2019), 
    ("Inception", 2010), 
    ("Titanic", 1997) 
]
 
def get_year(movie):
    return movie[1]
    
movies.sort(key=get_year, reverse=True)
for title, year in movies:
    print(f"{title}: {year}")