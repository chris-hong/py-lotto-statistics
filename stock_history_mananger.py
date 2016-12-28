from stock_history_dao import StockHistoryDAO
from stock_info_crawl import StockInfoCrawl

from datetime import datetime

class StockHistoryMananger:

    def __init__(self):
        print('start StockHistoryManager')
        self. __stockOriginData = datetime(2002, 12, 7)

        self.stockInfoCrawl = StockInfoCrawl()
        self.stockHistoryDAO = StockHistoryDAO()

    def update_stock_history(self):
        historyList = []
        turn = self.__get_recent_turn()

        print('\n### Crawling stock information is started!!')
        for index in range(1, turn+1):
            info = self.stockInfoCrawl.get_stock_info(index)
            historyList.append(info)
            progress = index / turn * 100
            print('### Crawling progress : %d%% ###' % progress)
        print('### Crawling stock information is completed!!')
        print(historyList)

        self.stockHistoryDAO.insert_data_many(historyList)

    def __get_today_string(self):
        datetime.today().weekday()

    def __get_recent_turn(self):
        return (datetime.today() - self.__stockOriginData).days // 7 + 1

author = 'chris-hong'

if __name__ == '__main__':
    shm = StockHistoryMananger()
    shm.update_stock_history()