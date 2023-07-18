#Taylor Donlea, Module 7.2 Assignment, 7/11/23

#Connect to the MySQL server and store everything in the variable 'cnx'
import mysql.connector
cnx = mysql.connector.connect(user='movies_user', password='popcorn',
                              host='localhost',
                              database='movies')

#Create a new cursor on the connection
cursor = cnx.cursor()

#Store the SELECT statement in the variable query
query = "SELECT * from studio"

#Execute the operation stored in the query variable using the execute() method
cursor.execute(query)

#Use the fetchall() method to get all of the rows from the last executed statement onto the cursor
result=cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")

#Loop through the rows and print out the columns
for row in result:
    print("Studio ID:",row[0])
    print("Studio Name:",row[1])
    print(" ")

#Display the Genre Records
query = "SELECT * from genre"
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for row in result:
    print("Genre ID:",row[0])
    print("Genre Name:",row[1])
    print(" ")

#Display the films that have a 'short film' runtime of less than 120 minutes/2 hours
query = "SELECT film_name,film_runtime from film where film_runtime<120 "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
for row in result:
    print("Film Name:",row[0])
    print("Runtime:",row[1])
    print(" ")

#Display the directors' information grouped by director
query = "SELECT film_name,film_director from film order by film_director "
cursor.execute(query)
result=cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
for row in result:
    print("Film Name:",row[0])
    print("Director:",row[1])
    print(" ")

#Close out the cursor
cursor.close()

#Close out the connection
cnx.close()