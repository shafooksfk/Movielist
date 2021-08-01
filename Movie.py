import sqlite3
con = sqlite3.connect('Movies.db')
cur = con.cursor()
# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS Movies
               (ID INT PRIMARY KEY NOT NULL, 
               MNAME TEXT NOT NULL,
               ACTOR TEXT NOT NULL,
               ACTRESS TEXT NOT NULL,
               DIRECTOR TEXT NOT NULL,
               YEAR_OF_RELEASE INT NOT NULL)''')

# Inserting datas
cur.execute("INSERT INTO Movies VALUES (1,'Yeh Jawaani Hai Deewani','Ranbir Kapoor','Deepika Padukone',"
            "'Ayan Mukerji',2013)")
cur.execute("INSERT INTO Movies VALUES (2,'Ae Dil Hai Mushkil','Ranbir Kapoor','Anushka Sharma',"
            "'Karan Johar',2016)")
cur.execute("INSERT INTO Movies VALUES (3,'Malik','Fahadh Faasil','Nimisha Sajayan',"
            "'Mahesh Narayanan',2021)")
cur.execute("INSERT INTO Movies VALUES (4,'Kumbalangi Nights', 'Fahadh Faasil', 'Anna Ben', 'Madhu C. Narayanan' , 2019)")
cur.execute("INSERT INTO Movies VALUES (5,'Varathan', 'Fahadh Faasil', 'Aiswarya Lekshmi', 'Amal Neerad' , 2018)")
cur.execute("INSERT INTO Movies VALUES (6, 'Drishyam 2', 'Mohanlal', 'Meena', 'Jeethu Joseph' , 2021)")
cur.execute("INSERT INTO Movies VALUES (7, 'Drishyam', 'Mohanlal', 'Meena', 'Jeethu Joseph'  , 2013)")
cur.execute("INSERT INTO Movies VALUES (8, 'Pathemari', 'Mammootty', 'Jewel Mary', 'Salim Ahmed' , 2015)")

cur = con.execute("SELECT ID, MNAME, ACTOR, ACTRESS,DIRECTOR,YEAR_OF_RELEASE from MOVIES ")
for row in cur:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ACTOR = ", row[2])
    print("ACTRESS = ", row[3])
    print("DIRECTOR = ", row[4])
    print("YEAR OF RELEASE = ", row[5], "\n")
con.close()
