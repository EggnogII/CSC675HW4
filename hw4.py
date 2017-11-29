#Imran Irfan
#CSC675 HW4
#This assignment was done in Python 3

import sqlite3

#Note that this implies the database we are looking for exists in the
#working directory

#Connect to database
conn = sqlite3.connect("chinook.db")

print ("Opened database successfully\n")
print ("Welcome to this program. Here are the following options")
print ("Option 1: Obtain Album title based on Artists Name (Enter 1)")
print ("Option 2: Obtain Purchase history for a Customer (Enter 2)")
print ("Option 3: Update Individual Track Price\n")

x = input("Decision:")

#Determine User action

if x == "1":
    # User wants to select an album title based on a particular artists name
    print("Option 1 has been selected\n")
    name = input("Enter the Artist Name: ")
    cursor = conn.execute("SELECT A.Title, A.AlbumId FROM album A, artist AB WHERE A.ArtistId=AB.ArtistId AND AB.name=?", (name,))
    for row in cursor:
        print (row)

    print("-------------------------------")

elif x == "2":
    print("Option 2 has been selected")
    customerId = input("Enter your Customer ID: ")
    #Output should consist of Track name, Album Name, Quantity, and Invoice Date
    cursor = conn.execute("SELECT T.Name, A.Title, IL.Quantity, I.InvoiceDate FROM track T, album A, invoiceline IL, invoice I WHERE I.InvoiceId=IL.InvoiceId AND IL.TrackId=T.TrackId AND T.AlbumId=A.AlbumId AND I.CustomerId=?", (customerId,))
    for row in cursor:
        print("Track Name = ", row[0])
        print("Album Title = ", row[1])
        print ("Quantity= ", row[2])
        print ("Invoice Date: ", row[3], "\n")

    print("-------------------------------")

elif x == "3":
    print("Option 3 has been selected")
    #User should be prompted for a Track ID. The current unit price for this track should be displayed.
    #Then prompt the user for the new price, update the appropriate record, and display the updated record

    trackId=input("Enter a Track Id: ")
    #Search for Track and its price
    cursor = conn.execute("SELECT T.UnitPrice FROM track T WHERE T.TrackId=?", (trackId,))
    for row in cursor:
        print (row)
    newPrice = input("Enter a new Price for this track: ")

    #Update and display record
    conn.execute("UPDATE track SET UnitPrice=? WHERE TrackId=?", (newPrice, trackId))
    conn.commit()

    cursor = conn.execute("SELECT TrackId, Name, UnitPrice FROM track WHERE TrackId=?", (trackId))
    for row in cursor:
        print ("TrackId = ", row[0])
        print ("Name = " , row[1])
        print ("UnitPrice = ", row[2], "\n")

else:
    print ("Invalid option. Exiting ...")



