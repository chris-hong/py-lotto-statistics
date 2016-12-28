import sqlite3


class StockHistoryDAO:

    db_path = '../analysis_data/history_data.db'
    sql_insert = '''INSERT INTO record_data(turn, num1, num2, num3, num4, num5, num6, bonus, rank1, rank2, rank3, rank4, rank5, total_sales) ''' \
                 '''VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        # cursor.execute('SELECT * FROM record_data')
        # for row in cursor:
        #     print(row)

    def __del__(self):
        self.conn.close()

    def insert_data(self, _data):
        with self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(self.sql_insert, _data)
                self.conn.commit()
            except sqlite3.Error as e:
                print('[SQLITE ERR]: ', e.args[0])



    def insert_data_many(self, _data_many):
        with self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.executemany(self.sql_insert, _data_many)
                self.conn.commit()
            except sqlite3.Error as e:
                print('[SQLITE ERR]: ', e.args[0])

    def select_data(self):
        with self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(self.sql_select)
                return cursor.fetchall()
            except sqlite3.Error as e:
                print('[SQLITE ERR]: ', e.args[0])


author = 'chris-hong'


# con = sqlite3.connect('analysis_data/history_data_20160726.db')
# cursor = con.cursor()
#
# cursor.execute("INSERT INTO record_data VALUES(46, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 3000)")
# con.commit()
#
# cursor.execute('SELECT * FROM record_data')
#
# for row in cursor:
#     print(row)

if __name__ == '__main__':
    # 테스트
    shDao = StockHistoryDAO()
    shDao.insert_data((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
