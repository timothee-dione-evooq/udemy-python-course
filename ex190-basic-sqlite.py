import sqlite3

# Se connecter à la base de données (ou la créer si elle n'existe pas)
conn = sqlite3.connect("library.db")

# Créer un curseur pour interagir avec la base de données
cursor = conn.cursor()


def create_books_table(conn, cursor):
    # Créer la table "books"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
    """)
    conn.commit()

def insert_books(conn, cursor):
    cursor.execute( """
    INSERT INTO books (title, author)
    VALUES 
        ('1984', 'George Orwell'),
        (Brave New World', 'Aldous Huxley'),
        ('Fahrenheit 451', 'Ray Bradbury')
    """
    )
    # Sauvegarder les changements
    conn.commit()

# Obtenir les noms des colonnes via PRAGMA
#cursor.execute("PRAGMA table_info(books)")
#columns = cursor.fetchall()
# Afficher les noms des colonnes
#for column in columns:
#    print(column[1])  # column[1] contient le nom de la colonne

def get_all_books_data(conn, cursor):
    cursor.execute("""
        select id,author,title from books
    """)
    books = cursor.fetchall()
    for book in books:
        print(book)

get_all_books_data(conn, cursor)

# Fermer la connexion
conn.close()
