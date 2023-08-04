import okx.BlockTrading
import time

api_key = "8290ad7a-197f-4e66-94f7-0dd260cc1a4b"
api_secret_key = "C615379DBDCF69B3FF17AF4497A03FF5"
passphrase = ""

obj = okx.BlockTrading.BlockTradingAPI(api_key, api_secret_key, passphrase, use_server_time=False, flag='1')

for i in range(100):
    print(obj.create_rfq(counterparties=['WAGMI'], anonymous='false', clRfqId='', tag='1234'
                   , allowPartialExecution='false', legs=[{'instId': "XRP-BTC", 'sz': '1700', 'side': 'sell'}]))
    time.sleep(1)
    res = obj.get_quotes()
    time.sleep(1)
    if float(res['data'][0]['legs'][0]['px']) < 9:
        break
    print(obj.execute_quote(rfqId=res['data'][0]['rfqId'], quoteId=res['data'][0]['quoteId']
                      , legs=[{'instId': "XRP-BTC", 'sz': '1700'}]))
    time.sleep(2)

