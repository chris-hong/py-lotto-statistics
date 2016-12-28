import requests
from htmldom import htmldom


class StockInfoCrawl:
    urlBase = 'http://m.nlotto.co.kr/lotto645Confirm.do?method=byWin&drwNo='

    def __init__(self):
        print('StockInfoCrawl is loaded')

    def get_stock_info(self, turn):
        url = self.urlBase + str(turn)
        source_code = requests.get(url)
        plain_text = source_code.text

        dom = htmldom.HtmlDom().createDom(plain_text)

        # 당첨번호
        img_num = dom.find('p.number').children()

        # 1st
        num1 = img_num[0].attr('alt')
        d_num1 = int(num1)
        # print(d_num1)

        # 2nd
        num2 = img_num[1].attr('alt')
        d_num2 = int(num2)
        # print(d_num2)

        # 3rd
        num3 = img_num[2].attr('alt')
        d_num3 = int(num3)
        # print(d_num3)

        # 4th
        num4 = img_num[3].attr('alt')
        d_num4 = int(num4)
        # print(d_num4)

        # 5th
        num5 = img_num[4].attr('alt')
        d_num5 = int(num5)
        # print(d_num5)

        # 6th
        num6 = img_num[5].attr('alt')
        d_num6 = int(num6)
        # print(d_num6)

        # 보너스 번호
        img_bonus = dom.find('p.number_bonus').children()
        bonus = img_bonus[0].attr('alt')
        d_bonus = int(bonus)
        # print(d_bonus)

        tr_rank = dom.find('table > tbody > tr')[1:6]

        # 1등
        rank1 = tr_rank[0].children()[2].text().replace(',', '')
        d_rank1 = int(rank1)
        # print(d_rank1)

        # 2등
        rank2 = tr_rank[1].children()[2].text().replace(',', '')
        d_rank2 = int(rank2)
        # print(d_rank2)

        # 3등
        rank3 = tr_rank[2].children()[2].text().replace(',', '')
        d_rank3 = int(rank3)
        # print(d_rank3)

        # 4등
        rank4 = tr_rank[3].children()[2].text().replace(',', '')
        d_rank4 = int(rank4)
        # print(d_rank4)

        # 5등
        rank5 = tr_rank[4].children()[2].text().replace(',', '')
        d_rank5 = int(rank5)
        # print(d_rank5)

        # 총 매출액
        total_sales = dom.find('span.f_blue').text().replace('원', '').replace(',', '')
        d_total_sales = int(total_sales) / 1000
        # print(d_total_sales)

        return (turn,           #1 회차
                d_num1,         #2 당첨번호(1)
                d_num2,         #3 당첨번호(2)
                d_num3,         #4 당첨번호(3)
                d_num4,         #5 당첨번호(4)
                d_num5,         #6 당첨번호(5)
                d_num6,         #7 당첨번호(6)
                d_bonus,        #8 당첨번호(보너스)
                d_rank1,        #9 당첨자수(1등)
                d_rank2,        #10 당첨자수(2등)
                d_rank3,        #11 당첨자수(3등)
                d_rank4,        #12 당첨자수(4등)
                d_rank5,        #13 당첨자수(5등)
                d_total_sales)  #14 총매출


author = 'chris-hong'
