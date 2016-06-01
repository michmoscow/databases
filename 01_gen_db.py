# encoding: utf-8
import sqlite3
from random import randint

db = sqlite3.connect('hw4_task1.db')
cur = db.cursor()

# Конференция без указания года проведения
cur.execute("CREATE TABLE Conference(id INT PRIMARY KEY, name TEXT)")

# Конференция, проведенная в какой-то год, со статистикой о принятии статей
cur.execute('''
CREATE TABLE ConferenceEvent(
    id INT PRIMARY KEY,
	conference_id INT REFERENCES Conference,
	year INT,
	total_papers INT,
	accepted_papers INT,
	acceptance_ratio NUMERIC(3,2),
	UNIQUE(conference_id, year))
''')

# Представление, показывающее конференции с высоким процентом принятия
cur.execute('''
CREATE VIEW HighPaperAcceptance AS
SELECT C.name, CE.year, CE.total_papers, CE.acceptance_ratio
FROM ConferenceEvent CE JOIN Conference C ON C.id = CE.conference_id
WHERE CE.total_papers > 5 AND CE.acceptance_ratio > 0.75''')
db.commit()

# Вставляем в таблицу Conference 10 конференций
cur = db.cursor()
for i in range(1,11):
	cur.execute(
	    "INSERT INTO Conference(id, name) VALUES (?, ?)",
	    (i, "Conf%d" % i))
db.commit()

# Вставляем в таблицу ConferenceEvent 100 событий
cur = db.cursor()
for i in range(1,101):
	conf_id = randint(1, 10)
	year = 2000 + randint(1, 15)
	while True:
		cur.execute("SELECT COUNT(*) FROM ConferenceEvent WHERE conference_id=? AND year=?", (conf_id, year))
		if cur.fetchone()[0] == 0:
			break
		year = year + 1
	total_papers = randint(1, 100)
	accepted_papers = randint(1, total_papers)
	acceptance_ratio = float(accepted_papers)/total_papers
	cmd = '''INSERT INTO ConferenceEvent(id, conference_id, year, total_papers, accepted_papers, acceptance_ratio)
	VALUES (?, ?, ?, ?, ?, ?)''';
	cur.execute(cmd, (i, conf_id, year, total_papers, accepted_papers, acceptance_ratio))
db.commit()
