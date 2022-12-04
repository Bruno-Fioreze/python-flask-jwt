from tinymongo import TinyMongoClient


def get_db():
    conn = TinyMongoClient()
    db = conn.my_database
    return db


def configure(app):
    # não fazer isso, sempre pegar a extensão para correta para cada banco
    app.db = get_db()
