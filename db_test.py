import sqlite3

con = sqlite3.connect('analysis_data/history_data_20160726.db')
cursor = con.cursor()
cursor.execute('SELECT * FROM record_data')

for row in cursor:
    print(row)

