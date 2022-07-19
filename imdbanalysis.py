# Step 1: Connect your Database (or create a connection) -> sqlite3.connect(database_name)
# Step 2: Use the cursor function -> database_variable.cursor()

# # Workflow

# 1. You need to establish a connection to the SQLite Database by creating a connection object
# 2. Then, you need to create a cursor object using cursor() method
# 3. Then, execute the query -> cursor_variable.execute('query')
# 4. To fetch the data, then use fetchall() method of the cursor variable/object
# 5. You have to create a DataFrame w.r.t. the SQLite Database
# 6. Data Exploration, Data Manipulation, Data Cleaning, Data Visualisation
# 7. Conclusion at every step
from unittest.util import three_way_cmp
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import sqlite3 
database=sqlite3.connect("movies.sqlite")
cur=database.cursor()
movies=cur.execute("select * from movies")
df=pd.DataFrame(movies,columns=['id', 'original_title', 'budget', 'popularity', 'release_date',
                                          'revenue', 'title', 'vote_average', 'vote_count', 'overview', 'tagline',
                                           'uid', 'director_id'])
directors=cur.execute("select * from directors")
directors_data=cur.fetchall()
directors_df=pd.DataFrame(directors_data)
# no of movies in the database
cur.execute("select count(original_title) from movies")
count=cur.fetchall()
print(count)
# select these three directors in the table James Cameron, Luc Besson, John Woo
cur.execute("select * from directors where name in ('James Cameron', 'Luc Besson' , 'John Woo')")
three_directors=cur.fetchall() 
print(three_directors)
# Find all the directors with the name starting with 'Steven'
cur.execute("select * from directors where name like 'Steven%' ")
steven=cur.fetchall()
print(steven)
# Count all the Female directors
cur.execute("select count(name) from directors where gender==1 ")
female=cur.fetchall()
print(female)
# Find the name of the 10th First female director
cur.execute("select name from directors where gender==1")
female_10=cur.fetchall()
print(female_10)
# Find the Top 3 most popular movies
cur.execute("select original_title from movies order by popularity desc limit '3'")
popular=cur.fetchall()
print(popular)
# Find the Top 3 most bankable(Budget) movie
cur.execute("select original_title from movies order by budget desc limit '3'")
bankable=cur.fetchall()
print(bankable)
#  Find out the most awarded average rated movie since Jan 1st, 2000
cur.execute("select original_title from movies where release_date > '2000-01-01' order by vote_average desc limit '1'")
most_average_rated=cur.fetchall()
print(most_average_rated)
# Find all the movie(s) that has been directed by Brenda Chapman
cur.execute("select original_title from movies join directors on movies.director_id=directors.id where name='Brenda Chapman'")
moviesbybrenda=cur.fetchall()
print(moviesbybrenda)
# Find out the director who has made the most movies?
cur.execute("select name from directors join movies on directors.id=movies.director_id  group by director_id order by count('directo_id') desc limit 1")
most_movies=cur.fetchall()
print(most_movies)
# Find out the director who is most bankable
cur.execute("select name from directors join movies on directors.id=movies.director_id  group by director_id order by sum(budget) desc limit 1")
most_bankable=cur.fetchall()
print(most_bankable)
# Find out the Top 10 highest budget making movies
cur.execute("select original_title from movies  order by budget desc limit 10")
top10_budget=cur.fetchall()
print(top10_budget)
# Find out the Top 10 most popular movies with the highest rating (vote_average)
cur.execute("select original_title from movies  order by vote_average desc limit 10")
high_rating=cur.fetchall()
print(top10_budget)
# Find the Top 10 directors with the number of movies and revenue where Revenue should be taken into account for doing thew analysis.
# Output: The directors who has got the highest revenue should comes at the Top and so on so forth.
cur.execute("select name from directors join movies on directors.id=movies.director_id group by director_id order by revenue desc limit 10")
x=cur.fetchall()
print(x)
