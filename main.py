import stock_history_dao
import stock_info_crawl

stock_history_dao.StockHistoryDAO('analysis_data/history_data_20160726.db')
stock_info_crawl.StockInfoCrawl().get_stock_info(1)
