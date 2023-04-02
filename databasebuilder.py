import sqlite3
import os
import sys

def createdb(db):
    conn = sqlite3.connect(db)

    cur = conn.cursor()

    sql = """
            CREATE TABLE gemeinde('gdenr' integer, 'gde_bez' text, 'gde_typ' text, 'bm_name' text, 'bm_typ' text)

            """
    cur.execute(sql)



if os.path.exists("haushalt.db"):
    print("database already in place")
else:
    createdb("haushalt.db")

