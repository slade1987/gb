import requests

def cur_cut(curren,str):
    find1 = str.find(curren)
    if find1 > -1:
        find2 = str.find('ue>',find1)
        result = str[find2 + 3:find2 + 8]
        return result.replace(',','.')
    else:
        return None

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
res = cur_cut(input("Введите валюту:").upper(),str(response.content))

if res is not None:
  print(float(res))
else:
    print(res)
