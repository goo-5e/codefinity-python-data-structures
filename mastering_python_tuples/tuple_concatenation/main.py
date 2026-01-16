space_movies = ('2001: A Space Odyssey', 'Interstellar', 'Star Wars: Episode IV - A New Hope', 'Gravity', 'The Martian')

new_movies = ['The Lion King', 'Jurassic Park', 'Finding Nemo']

# Write your code here
animal_movies = tuple(new_movies)

movie_poster = space_movies + animal_movies

# Testing
print("Now playing in theaters:", movie_poster)