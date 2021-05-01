import sqlite3

# TODO OOB Ansatz besprechen

class HighScoreDB:
    def __init__(self):
        self.conn = self.createDB()
        self.tableName = "Highscore"

    def createDB(self):
        """
        Erstellt die benötigte DB, falls sie nicht schon exestiert.
        :return: connection
        """
        conn = sqlite3.connect(f"Resources/{self.tableName}.db")
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
        :return: -
        """
        cursor = self.conn.cursor()
        cursor.execute(f"INSERT INTO {self.tableName} ( username, score) VALUES (?,?)", (username, score))
        self.conn.commit()
        cursor.close()

    def returnHighscoreList(self):
        # TODO Return Kommentar vergewissern
        """
        Gibt die aktuelle Highscore-Tabelle zurück
        :return: Inhalt der Highscore Tabelle, als Liste mit Tupeln
        """
        sqlSelect = f"SELECT * FROM {self.tableName}"
        cursor = self.conn.cursor()
        selectReturn = cursor.execute(sqlSelect)
        cursor.close()
        return selectReturn
