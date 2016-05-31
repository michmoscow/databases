import sys
import sqlite3
from random import randint

db = sqlite3.connect('m3_hw_task2.db')
cur = db.cursor()

cur.execute("SELECT university_id FROM University WHERE name=?", (sys.argv[1],))
university_id = cur.fetchone()[0]

researchers = {}
cur.execute("SELECT researcher_id FROM Researcher WHERE university_id=?", (university_id,))
for row in cur.fetchall():
    researchers[row[0]] = True

conferences = {}
cur.execute("SELECT conference_id, researcher_id FROM Participant")
for row in cur.fetchall():
    if row[1] in researchers:
        conferences[row[0]] = True

result = []
cur.execute("SELECT conference_id, name FROM Conference")
for row in cur.fetchall():
    if row[0] not in conferences:
        result.append(row[1])

for c in sorted(result):
    print c
