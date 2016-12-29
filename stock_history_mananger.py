from stock_history_dao import StockHistoryDAO
from stock_info_crawl import StockInfoCrawl
from util.event_hook import EventHook

from datetime import datetime

class StockHistoryMananger:

    def __init__(self):
        print('start StockHistoryManager')
        self. __stockOriginData = datetime(2002, 12, 7)

        self.__stockInfoCrawl = StockInfoCrawl()
        self.__stockHistoryDAO = StockHistoryDAO()

        self.onProgressChanged = EventHook()

    def update_stock_history(self):
        list_history = []
        list_unknown_turn = []

        turn = self.__get_recent_turn()

        for index in range(1, turn + 1):
            if not self.__check_turn_data(index):
                list_unknown_turn.append(index)

        for unknown in list_unknown_turn:
            info = self.__stockInfoCrawl.get_stock_info(unknown)
            list_history.append(info)
            progress = (list_unknown_turn.index(unknown) + 1) / len(list_unknown_turn) * 100
            self.onProgressChanged.fire(progress)
            print('### Crawling progress : %d%% ###' % progress)

        self.__stockHistoryDAO.insert_data_many(list_history)

        data_all = self.__stockHistoryDAO.select_data_all()
        first_turn = data_all[0][0]
        data_all.reverse()
        last_turn = data_all[0][0]
        if data_all != None and len(data_all) > 0:
            return first_turn, last_turn
        else:
            return None

    def __get_today_string(self):
        datetime.today().weekday()

    def __get_recent_turn(self):
        return (datetime.today() - self.__stockOriginData).days // 7 + 1

    def __check_turn_data(self, _turn):
        res = self.__stockHistoryDAO.check_turn_data((_turn,))
        if res == None:
            return False
        else:
            return True

author = 'chris-hong'

if __name__ == '__main__':
    shm = StockHistoryMananger()
    shm.update_stock_history()
    # print(shm.check_turn_data(700))
