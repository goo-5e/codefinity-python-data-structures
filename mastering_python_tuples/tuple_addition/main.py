animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here

# Using both methods to add elements to a tuple
new_movies = list(animal_movies)
new_movies.append('Dumbo')
animal_movies = tuple(new_movies)
del new_movies

new_movies = ('Zootopia',)

animal_movies += new_movies

print("Updated animal movies:", animal_movies)