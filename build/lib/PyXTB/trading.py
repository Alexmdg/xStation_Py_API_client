from PyXTB.api_access import AccessAPI, QuerySet
from PyXTB.settings import log
import time


class ActiveWallet():

    def __init__(self, id, password):
        self.session = AccessAPI(id, password)
        self.session.streamListeningStart()
        self.session.streamBalance()
        time.sleep(2)
        self.session.stopBalance()
        self.session.streamListeningStop()
        qs = QuerySet('wallet_init')
        qs.getUserData()
        qs.getAllSymbols()
        self.session.staticDataRequest(qs)
        log.dataIO.debug(self.session.static_datas['wallet_init_AllSymbols']['returnData'])
        self.symbols = []
        with log.cbugCheck(log.main):
            for symbol in self.session.static_datas['wallet_init_AllSymbols']['returnData']:
                log.dataProc.debug(f'{symbol}')
                self.symbols.append({'symbol': symbol['symbol'],
                                     'currency': symbol['currency'],
                                     'category': symbol['categoryName'],
                                     'pip': symbol['tickValue'],
                                     'lot': symbol['contractSize']
                                 })
        log.main.cmn_dbg(self.symbols)
        self.balance = self.session.stream_datas['balance']['data']['balance']
        self.margin = self.session.stream_datas['balance']['data']['margin']
        self.leverage = self.session.static_datas['wallet_init_UserData']['returnData']['leverageMultiplier']
        self.currency = self.session.static_datas['wallet_init_UserData']['returnData']['currency']

    def newSubWallet(self, name, percentage, symbols):
        pass









if __name__ == '__main__':
    trading = ActiveWallet('11360828', 'A00000000')





