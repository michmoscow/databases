# encoding: utf-8
import sqlite3
from random import randint

db = sqlite3.connect('hw4_task1.db')
cur = db.cursor()

# Удаляем из ConferenceEvent столбцы total_papers, accepted_papers и acceptance_ratio
# В SQLite не поддерживается DROP COLUMN
cur.execute('''
CREATE TABLE ConferenceEventv2(
    id INT PRIMARY KEY,
	conference_id INT REFERENCES Conference,
	year INT,
	UNIQUE(conference_id, year))
''')
cur.execute('''
INSERT INTO ConferenceEventv2 SELECT id, conference_id, year FROM ConferenceEvent
''')
cur.execute('''
DROP TABLE ConferenceEvent
''')
cur.execute('''
ALTER TABLE ConferenceEventv2 RENAME TO ConferenceEvent
''')
db.commit()

# Таблица Paper
cur = db.cursor()
cur.execute('''
CREATE TABLE Paper(
    id INT PRIMARY KEY,
	event_id INT REFERENCES ConferenceEvent,
	title TEXT,
	accepted BOOLEAN)''')

# Удалаем представление
cur.execute('''DROP VIEW HighPaperAcceptance''')
db.commit()

cur = db.cursor()
# Вставляем в таблицу Paper 1000 статей
cur = db.cursor()
for i in range(1,1001):
	cur.execute(
	    '''INSERT INTO Paper(id, event_id, title, accepted)
        VALUES (?, ?, ?, ?)''',
	    (i, randint(1, 100), "Paper%d" % i, True if randint(1, 2) == 2 else False))
db.commit()
