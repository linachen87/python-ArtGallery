from tkinter import *
import sqlite3
from turtle import heading, width
with sqlite3.connect("gallery.db") as db:
    cursor = db.cursor()



# cursor.execute("DROP TABLE IF EXISTS ArtistsContactInfo")
# db.commit()

# cursor.execute("DROP TABLE IF EXISTS Pieces_of_Art")
# db.commit()

# cursor.execute("""CREATE TABLE ArtistsContactInfo(
#     ArtistID integer PRIMARY KEY,
#     Name text NOT NULL,
#     Address test NOT NULL,
#     Town text,
#     County text NOT NULL,
#     Postcode text NOT NULL
# );""")

# cursor.execute("""INSERT INTO ArtistsContactInfo (ArtistID,Name,Address,Town,County,Postcode) values(1,'Martin Leighton','5 Park Place','Peterborough','Cambridgeshire','PE32 5LP')""")
# cursor.execute("""INSERT INTO ArtistsContactInfo (ArtistID,Name,Address,Town,County,Postcode) values(2,'Eva Czarnniecka','77 Warner Close','Chelmsford','Essex','CM22 5FT')""")
# cursor.execute("""INSERT INTO ArtistsContactInfo (ArtistID,Name,Address,Town,County,Postcode) values(3,'Roxy Parkin','90 Hindhead Road','','London','SE12 6WM')""")
# cursor.execute("""INSERT INTO ArtistsContactInfo (ArtistID,Name,Address,Town,County,Postcode) values(4,'Nigel Farnworth','41 Whitby Road','Huntly','Aberdeenshire','AB54 5PN')""")
# cursor.execute("""INSERT INTO ArtistsContactInfo (ArtistID,Name,Address,Town,County,Postcode) values(5,'Teresa Tanner','70 Guilde Street','','London','SE12 6WM')""")
# db.commit()

# cursor.execute("""CREATE TABLE Pieces_of_Art(
#     PieceID integer PRIMARY KEY,
#     ArtistID integer,
#     Title text NOT NULL,
#     Medium text NOT NULL,
#     Price integer NOT NULL
# );""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(1,5,'Woman with black Labrador','Oil',220)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(2,5,'Bees & thistles','Watercolour',85)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(3,2,'A Stroll to Westminster','Ink',190)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(4,1,'African Giant','Oil',800)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(5,3,'Water Daemon','Acrylic',1700)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(6,4,'A seagull','Watercolour',35)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(7,1,'Tree friends','Oil',1800)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(8,2,'Summer breeze 1','Acrylic',1350)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(9,4,'Mr hamster','Watercolour',35)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(10,1,'Pulpit rock,Dorset','Oil',600)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(11,5,'Trawler Dungeness beach','Oil',35)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(12,2,'Dance in the snow','Oil',250)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(13,4,'St Tropez port','Ink',45)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(14,3,'Pirate assassin','Acrylic',420)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(15,1,'Morning walk','Oil',800)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(16,4,'A barn swallow','Watercolour',35)""")
# cursor.execute("""INSERT INTO Pieces_of_Art (PieceID,ArtistID,Title,Medium,Price) values(17,4,'The old working mills','Ink',395)""")
# db.commit()

def add_artist():
    name = nameEntry.get()
    address = addressEntry.get()
    town = townEntry.get()
    county = countyEntry.get()
    Postcode = PostEntry.get()
    cursor.execute("""INSERT INTO ArtistsContactInfo (Name,Address,Town,County,Postcode) values(?,?,?,?,?)""",(name,address,town,county,Postcode))
    db.commit()
    nameEntry.delete(0,END)
    addressEntry.delete(0,END)
    townEntry.delete(0,END)
    countyEntry.delete(0,END)
    PostEntry.delete(0,END)
    nameEntry.focus()

def cArtistInfo():
    nameEntry.delete(0,END)
    addressEntry.delete(0,END)
    townEntry.delete(0,END)
    countyEntry.delete(0,END)
    PostEntry.delete(0,END)
    nameEntry["justify"] = "left"
    nameEntry.focus()

def addArtInfo():
    name = artistNameEntry.get()

    title = artTitleEntry.get()
    mediuminfo = medium.get()
    price = artPriceEntry.get()
    cursor.execute("SELECT ArtistID FROM ArtistsContactInfo WHERE Name=?",[name])
    for id in cursor.fetchall():
        newid = str(id[0])
    
    cursor.execute("""INSERT INTO Pieces_of_Art(ArtistID,Title,Medium,Price) VALUES(?,?,?,?)""",(newid,title,mediuminfo,price))
    db.commit()
    artistNameEntry.delete(0,END)
    artTitleEntry.delete(0,END)
    medium.set("")
    artPriceEntry.delete(0,END)
    artistNameEntry.focus()

def clearArtInfo():
    artistNameEntry.delete(0,END)
    artTitleEntry.delete(0,END)
    medium.set("")
    artPriceEntry.delete(0,END)
    artistNameEntry.focus()

def ViewArtist():
    cursor.execute("SELECT * FROM ArtistsContactInfo")
    info = cursor.fetchall()
    for x in info:
        record = str(x[0])+","+str(x[1])+","+str(x[2])+","+str(x[3])+","+str(x[4])+","+str(x[5])
        outputwindow.insert(END,record)

def ViewArt():
    cursor.execute("SELECT * FROM Pieces_of_Art")
    info = cursor.fetchall()
    for line in info:
        record = str(line[0])+","+str(line[1])+","+str(line[2])+","+str(line[3])+","+str(line[4])
        outputwindow.insert(END,record)

def clearOutput():
    outputwindow.delete(0,END)

def SearchArtist():
    artistID = searchArtistEntry.get()
    cursor.execute("SELECT Name FROM ArtistsContactInfo WHERE ArtistID = ?",[artistID])
    for line in cursor.fetchall():
        
        outputwindow.insert(END,line)
        cursor.execute("SELECT * FROM Pieces_of_Art WHERE ArtistID = ?",[artistID])
        for artdetail in cursor.fetchall():
            detail = str(artdetail[2])+","+str(artdetail[3]+","+str(artdetail[4])+"\n")
            outputwindow.insert(END,detail)
    searchArtistEntry.delete(0,END)
    searchArtistEntry.focus()

def searchByMedium():
    mediumchoice = searchMedium.get()
    cursor.execute("""SELECT ArtistsContactInfo.Name, Pieces_of_Art.ArtistID, Pieces_of_Art.Title, Pieces_of_Art.Medium, Pieces_of_Art.Price FROM Pieces_of_Art, ArtistsContactInfo WHERE Pieces_of_Art.ArtistID = ArtistsContactInfo.ArtistID AND Medium = ?""",[mediumchoice])
    for line in cursor.fetchall():
        record = str(line[0])+","+str(line[1])+","+str(line[2])+","+str(line[3])+","+str(line[4])+"\n"
        outputwindow.insert(END,record)
    searchMedium.set("Search by Medium")

def searchByPrice():
    minprice = searchPriceMin.get()
    minprice = int(minprice)
    maxprice = searchPriceMax.get()
    maxprice = int(maxprice)
    cursor.execute("""SELECT ArtistsContactInfo.Name, Pieces_of_Art.ArtistID, Pieces_of_Art.Title, Pieces_of_Art.Medium, Pieces_of_Art.Price FROM Pieces_of_Art, ArtistsContactInfo WHERE Pieces_of_Art.ArtistID = ArtistsContactInfo.ArtistID AND Pieces_of_Art.Price >=? AND Pieces_of_Art.Price <= ?""",(minprice,maxprice))
    for x in cursor.fetchall():
        record = str(x[0])+","+str(x[1])+","+str(x[2])+","+str(x[3])+","+str(x[4])+"\n"
        outputwindow.insert(END,record)
    searchPriceMin.delete(0,END)
    searchPriceMax.delete(0,END)

def thesoldArt():
    soldArtID = soldArt.get()
    file = open("soldArt.txt","a")
    cursor.execute("""SELECT * FROM Pieces_of_Art WHERE PieceID = ?""",[soldArtID])
    for x in cursor.fetchall():
        record = str(x[0])+","+str(x[1])+","+str(x[2])+","+str(x[3])+","+str(x[4])+"\n"
        file.write(record)
    file.close()
    cursor.execute("DELETE FROM Pieces_of_Art WHERE PieceID = ?",[soldArtID])
    db.commit()
    soldArt.delete(0,END)
    soldArt.focus()




root = Tk()
root.title("Art Gallery")
root.geometry("1000x800")

namelabel = Label(text = "Name:")
namelabel.place(x=20,y=20,width=50,height=25)
nameEntry = Entry(text = "")
nameEntry.place(x=90,y=20,width=100,height=25)

addresslabel = Label(text = "Address:")
addresslabel.place(x=200,y=20,width=50,height=25)
addressEntry = Entry(text = "")
addressEntry.place(x=260,y=20,width=100,height=25)

townlabel = Label(text = "Town:")
townlabel.place(x=370,y=20,width=50,height=25)
townEntry = Entry(text = "")
townEntry.place(x=430,y=20,width=100,height=25)

Countylabel = Label(text = "County:")
Countylabel.place(x=540,y=20,width=50,height=25)
countyEntry = Entry(text = "")
countyEntry.place(x=600,y=20,width=100,height=25)

Postcodelabel = Label(text = "Post Code:")
Postcodelabel.place(x=710,y=20,width=60,height=25)
PostEntry = Entry(text = "")
PostEntry.place(x=780,y=20,width=100,height=25)

addartistBtn = Button(text = "Add Artist",command=add_artist)
addartistBtn.place(x=90,y=70,width=80,height=25)

clearArtistBtn = Button(text = "Clear",command = cArtistInfo)
clearArtistBtn.place(x= 180,y=70, width=80,height=25)


artistNameLabel = Label(text = "Artist:")
artistNameLabel.place(x=20,y=105,width=50,height=25)
artistNameEntry = Entry(text = "")
artistNameEntry.place(x=90,y=105,width=100,height=25)

artTitleLabel = Label(text = "Title:")
artTitleLabel.place(x=200,y=105,width=50,height=25)
artTitleEntry = Entry(text = "")
artTitleEntry.place(x=260,y=105,width=200,height=25)

medium = StringVar(root)
medium.set("Select Medium")
mediumlist = OptionMenu(root,medium,"Ink","Watercolor","oil","Acrylic")
mediumlist.place(x=470,y=105,width=150,height=25)

artPriceLabel = Label(text = "Price:")
artPriceLabel.place(x=640,y=105,width=50,height=25)
artPriceEntry = Entry(text = "")
artPriceEntry.place(x=700,y=105,width=100,height=25)

artInfoAddBtn = Button(text = "Add",command=addArtInfo)
artInfoAddBtn.place(x=90,y=150,width=80,height=25)

artInfoClearBtn = Button(text = "Clear",command = clearArtInfo)
artInfoClearBtn.place(x=180,y=150,width=80,height=25)

viewAllArtist = Button(text = "View all Artist",command=ViewArtist)
viewAllArtist.place(x=790,y=180,width=90,height=25)

viewAllArt = Button(text = "View all Art",command = ViewArt)
viewAllArt.place(x=790,y=210,width=90,height=25)

clearOutputWindow = Button(text = "Clear Output",command=clearOutput)
clearOutputWindow.place(x=790,y=240,width=90,height=25)

outputwindow = Listbox()
outputwindow.place(x=20,y=180,width=750,height=200)

searchArtistEntry = Entry(text="")
searchArtistEntry.place(x=790,y=270,width=90,height=25)
searchArtistBtn = Button(text = "Search Artist",command=SearchArtist)
searchArtistBtn.place(x=900,y=270,width=75,height=25)

searchMedium = StringVar(root)
searchMedium.set("Select Medium")
mediumlist2 = OptionMenu(root,searchMedium,"Ink","Watercolor","Oil","Acrylic")
mediumlist2.place(x=790,y=300,width=100,height=30)
searchMediumBtn = Button(text = "Search Medium",command=searchByMedium)
searchMediumBtn.place(x=900,y=300,width=85,height=25)

searchPriceMin = Entry("")
searchPriceMin.place(x=790,y=335,width=50,height=25)
searchPriceMax = Entry("")
searchPriceMax.place(x=845,y=335,width=50,height=25)
searchPriceBtn = Button(text= "Search By Price",command=searchByPrice)
searchPriceBtn.place(x=900,y=335,width=85,height=25)

soldArt = Entry(text = "ArtID")
soldArt.place(x=790,y=370,width=105,height=25)
soldBtn = Button(text="Sold",command=thesoldArt)
soldBtn.place(x=900,y=370,width=80,height=25)


root.mainloop()