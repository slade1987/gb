def cur_cut(curren,str):
    find1 = str.find(curren)
    if find1 > -1:
        find2 = str.find('ue>',find1)
        result = str[find2 + 3:find2 + 8]
        return result.replace(',','.')
    else:
        return None

if __name__ == "__main__":
    print("I'm file")
else:
    print("Module")

