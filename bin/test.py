import mysql.connector
from random import choice
def connection(Query):
    config = {
        'user': 'root',
        'password': 'admin',
        'host': 'localhost',
        'database': 'administration_agricole',
        'raise_on_warnings': True
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(Query)
    connection.commit()
    connection.close
name = ['Christensen', 'Brian' , 'Montgomery', 'Monet', 'Mcneil', 'Yousif', 'Flower', 'Aliya', 'Warner', 'Nate',
        'Thornton', 'Melvin', 'Salazar', 'Bhavik', 'Currie', 'Mia-Rose', 'Forbes', 'Khadeeja', 'Parrish', 'Farhan', 'Thompson', 'Raees',
        'Pitt', 'Cinar', 'York', 'Cadence', 'Davidson', 'Sarah-Jayne', 'Beech', 'Steffan' , 'Baxter', 'Nigel','Lucer',
        'Mahno','Santo','Zoe B','roadh','Matia','s Cal','Aleez','a Joy','Shuai','b Mez','Karso','n Mcl','Ritch','ie Ah',
        'Idris',' Cole','Amaya',' Rich','Dewey',' Hump','Abdur','rahma','Rober','to Mo','Summe','r Gre','Brad ','Doher',
        'Baran',' Hurs','Isra ','Parke','Rafe ','Horto','Shayl','a Pat','Derry',' Colo','Tasni','m Joy','Jade ','Holdi',
        'Carin','a Del','Sheil','a Slo','Alba ','Field','Clayt','on Fa','Mae K','ay','Riley',' Finc','Akram',' Drap',
        'Ioan ','Koch','Isla-','Mae M','Lily-','Mai A','Lucin','da He','Danie','la Co','Jerry',' Mark','Deen ','Marti',
        'Emyr ','Pross','Stell','a Bou','Travi','s Squ','Jett ','Lynch','Elli ','Randa','Dylan',' Bost','Emmie',
        ' Moha','Ameer','a Sey','Aayat',' Phan','Zavie','r Stu','Jax G','allag','Lilli','a Dun','Levis','on Mc','Greg ',
        'Lee','Ada H','errin','Huma ','Vasqu','Tonic','ha Wi','Alesh','a Car','Artur',' Wild','Terre','nce P','Aurel',
        'ia Wa','Kimbe','rly W','Primr','ose V','Joe B','ailey','Olivi','a Tur','Cain ','Harri','Aisli','ng Mo','Myles',
        ' Sher','Kourt','ney G','Saman','tha P','Layla','-Rose','Euan ','Rando','Bella',' Rahm','Aran ','Mejia','Sohai',
        'l Ste','Marth','a Swa','Kaira',' Watt','Charl','y Cai','Tamik','a Sni','Roan ','Knott','Levi ','Dudle','Darry',
        'l Blo','Ellis',' Barr','Warwi','ck Go','Kodi ','Moss','Mica ','Wilso','Gianl','uca R','Riyad',' Cast','Krist',
        'ina C','Deann','a Huf','Umar ','James',]
for i in range(2000):
    for idNumber, name, lastName, Deanship, phoneNumber, headsNumber:
        connection(f"INSERT INTO FARMERS VALUES('{idNumber.}','{name}',"
            f"'{lastName}', '{Deanship}', "
            f"'{phoneNumber}', '{headsNumber}')