# coding:utf-8
import psycopg2


class Postgresql:
    def __init__(self, host, port, db, usr, pwd):
        self.conn = psycopg2.connect(host=host, port=port, dbname=db, user=usr, password=pwd)

    def select(self, sql, func):
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            func(row)
        cur.close()

    def execute(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        cur.close()

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def insert(self, sql, data):
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        cur.close()


def format_res(row):
    print(row[0])


if __name__ == '__main__':
    postgresql = Postgresql("172.16.3.180", 5432, "a210", "postgres", "baifendian")
    postgresql.insert("INSERT INTO lang values (%s, %s)", ("t1", "t2"))
    postgresql.select("SELECT * FROM lang", format_res)
    postgresql.close()
