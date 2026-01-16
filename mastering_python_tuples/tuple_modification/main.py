movie_genres = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi")

# Write your code here
temp_list = list(movie_genres)

temp_list[2] = "Thriller"  
temp_list[3] = "Adventure"  

movie_genres = tuple(temp_list)

del temp_list

# Testing
print("Updated genres:", movie_genres)