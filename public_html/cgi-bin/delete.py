#!/usr/bin/python3

import cgi, cgitb
import mysql.connector

delete_table = form.getvalue('delete_table')
delete_condition = form.getvalue('delete_condition')

cnx = mysql.connector.connect(user='eapfelba', database='eapfelba1', password='chumash1000')
cursor = cnx.cursor()

if delete_table and delete_condition:
    query = ("delete from " + delte_table + " where " + delete_condition)


cursor.close()
cnx.close()
