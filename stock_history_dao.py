import sqlite3


class StockHistoryDAO:

    con = None

    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        cursor = self.con.cursor()
        cursor.execute('SELECT * FROM record_data')
        for row in cursor:
            print(row)

# pls = StockHistoryDAO('analysis_data/history_data_20160726.db')

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
