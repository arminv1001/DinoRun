import sqlite3
from operator import itemgetter


class HighScoreDB:
    def __init__(self):
        self.tableName = "HighscoreDB"
        self.conn = self.createDB()

    def createDB(self):
        """
        Erstellt die benötigte DB, falls sie nicht schon exestiert.
        :return: Verbindug zur Datenbank
        :test:
            - Tabelle wurde erstellt bzw. exestiert schon
            - Rückgabewert hat den richtigen Datentyp
        """
        print(self.tableName)
        conn = sqlite3.connect(f"Database/{self.tableName}.db")
        highscoreDBSql = f" CREATE TABLE IF NOT EXISTS {self.tableName} ( id integer PRIMARY KEY AUTOINCREMENT,username VARCHAR(20) NOT NULL,score integer NOT NULL); "
        cursor = conn.cursor()
        cursor.execute(highscoreDBSql)
        cursor.close()
        return conn

    def insertScore(self, username, score):
        """
        Fügt einen Score in die Datenbank ein.
        :param username: Username des Users
        :param score: Punkteanzahl des Users
        :test:
            - Werte wurden richtig in die Datenbank eingefügt
            - Test auf Fehlermeldung
        """
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO {self.tableName} ( username, score) VALUES (?,?)", (username, score))
        self.conn.commit()
        cursor.close()

    def returnHighscoreList(self):
        """
        Gibt die aktuelle Highscore-Tabelle zurück. Sotiert nach Score.
        :return: Inhalt der Highscore Tabelle,
        als Liste mit Tupel in denen sich die einzelenen Reihen befinden. Sortiert nach Score.
        :quelle: https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        :test:
            - Richtige Daten werden von der Datenbank zurückgegeben
            - Es wird richitg sortiert

        """
        sqlSelect = f"SELECT * FROM {self.tableName}"
        cursor = self.conn.cursor()
        cursor.execute(sqlSelect)
        selectRows = cursor.fetchall()
        cursor.close()
        selectRows = sorted(selectRows, key=itemgetter(2), reverse=True)
        return selectRows
