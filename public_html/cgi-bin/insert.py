#!/usr/bin/python3                                     
                                
import cgi, cgitb
import mysql.connector

form = cgi.FieldStorage()
insert_table = form.getvalue('insert_table')
values = form.getvalue('values').split(',')

svalues = ""
for value in values:
    # concatenate them into the appropriate syntax, removing any unnecessary whitespace
    svalues += '"' + value.strip() + '", '
svalues = svalues[:-2]

cnx = mysql.connector.connect(user='eapfelba', host = 'localhost',
                              database='eapfelba1', password='chumash1000')

cursor = cnx.cursor()

# inserting into a table
# need to also check if not the right form... right amount of attributes for that table
if insert_table and values:
    query = ("insert into " + insert_table + " values (" + svalues + ");")

cursor.execute(query)
#data = cursor.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body background='../biochem.png'>")
print("<center>")
print("<h1>~BioBase~</h1>")
print("<h2>Home of Biochemical Processes</h2>")
print("<h3>Inserted " + svalues + " into " + insert_table + "!</h3>")
print("<h3>with " + query + " error<h3>")
print("</center>")
print("</body>")
print("</html>")

cursor.close()
cnx.close()