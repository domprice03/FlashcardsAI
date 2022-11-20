import sqlite3
from flashcard import Flashcard


def cursor():
    return sqlite3.connect('flashcards.db').cursor()


c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS flashcards (topic  TEXT, content TEXT, keywords TEXT, leitner INTEGER)')
c.connection.close()


def add_flashcard(flashcard):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO flashcards VALUES (?, ?, ?, ?)',
                  (flashcard.topic, flashcard.content, flashcard.keywords, int(flashcard.leitner)))
    c.connection.close()
    return c.lastrowid


def get_flashcards():
    c = cursor()
    flashcards = []
    with c.connection:
        for flashcard in c.execute('SELECT * FROM flashcards'):
            flashcards.append(Flashcard(flashcard[0], flashcard[1], flashcard[2], flashcard[3]))
    c.connection.close()
    return flashcards


def get_flashcard_by_topic(topic):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM flashcards WHERE topic=?', (topic,))
    data = c.fetchone()
    c.connection.close()
    if not data:
        return None
    return Flashcard(data[0], data[1], data[2], data[3])


def get_flashcards_by_leitner(leitner):
    c = cursor()
    flashcards = []
    with c.connection:
        for flashcard in c.execute('SELECT * FROM flashcards WHERE leitner=?', (leitner, )):
            flashcards.append(Flashcard(flashcard[0], flashcard[1], flashcard[2], flashcard[3]))
    c.connection.close()
    return flashcards


def delete_flashcard(flashcard):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM flashcards WHERE topic=?', (flashcard.topic, ))
    rows = c.rowcount
    c.connection.close()
    return rows


def update_leitner(new_leitner, topic):
    c = cursor()
    with c.connection:
        c.execute('UPDATE flashcards SET leitner=? WHERE topic=?',
                  (new_leitner, topic))
    flashcard = get_flashcard_by_topic(topic)
    c.connection.close()
    return flashcard
