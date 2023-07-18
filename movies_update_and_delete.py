# Taylor Donlea, 7/15/2023, Module 8 Assignment

import mysql.connector

# Creating a display for the films 
def show_films(cursor, title):
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    print ("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Defining main method and connecting to the database
def main():
    connection = mysql.connector.connect(
    user='movies_user',
    password='popcorn',
    host='localhost',
    database='movies'
    )
    
    # Create cursor
    cursor = connection.cursor()

    # Displaying existing records in database
    initialQuery = "SELECT * from studio"
    cursor.execute(initialQuery)
    result = cursor.fetchall()
    show_films(cursor, "DISPLAYING FILMS")

    # Inserting the new movie
    insertQuery = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Star Wars', '2000', '155', 'George Lucas', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );"
    connection.commit()
    cursor.execute(insertQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Updating the Alien movie
    updateQuery = "update film set genre_id = (select genre_id from genre where genre_name = 'Horror') where film_name = 'Alien';"
    connection.commit()
    cursor.execute(updateQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    # Deleting the Gladiator movie from the table
    deleteQuery = " delete from film where film_name = 'Gladiator';"
    connection.commit()
    cursor.execute(deleteQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Calling the main function
main()