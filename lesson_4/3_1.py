#import datetime
from datetime import datetime
import requests

def cur_cut(curren,str):
    find_date = str.find('Date')
    result = [datetime.strptime(str[find_date + 6:find_date + 16].replace('.','-'),'%d-%m-%Y')]
    find1 = str.find(curren)
    if find1 > -1:
        find2 = str.find('ue>',find1)
        result.append(str[find2 + 3:find2 + 8].replace(',','.'))
        return result
    else:
        return None

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
res = cur_cut(input("Введите валюту:").upper(),str(response.content))

if res[1] is not None:
    print('Курс валюты на ',res[0],' ',float(res[1]))
else:
    print(res[1])
