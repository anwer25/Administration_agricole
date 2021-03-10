from docxtpl import DocxTemplate
import mysql.connector


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
    try:
       cursor.execute(Query)
       return cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)


def writerTest(words: list) -> None:
    context = {
        'l': words
    }
    docx = 'test1.docx'
    doc = DocxTemplate(docx)

    doc.render(context)
    doc.save('test2.docx')


writerTest(connection('SELECT * FROM farmers'))
