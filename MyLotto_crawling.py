import pandas as pd
import bs4
import re
import urllib
# from urllib.request import urlopen

df_train = pd.read_csv('input/lotto_data_train.csv', encoding='euc-kr')


def find_end_round():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
    result_data = urllib.request.urlopen(url)
    lotto_data = result_data.read()
    soup = bs4.BeautifulSoup(lotto_data, 'html.parser')
    ret = []
    newret = []
    for numbers in soup.findAll('div', attrs={'class': 'win_result'}):
        num = numbers.findAll('h4')
        ret.append(num)

    ret = ret[0]
    for idx in ret:
        string = str(idx)
        onlynum = re.sub('<.+?>', '', string, 0, re.I | re.S)
        newret.append(onlynum)

    newret = newret[0]
    newret = newret[:3]
    return int(newret)


start_round = df_train.shape[0]
end_round = find_end_round()

if start_round == end_round:
    print('A')

else:
    start_round += 1
    end_round += 1
    for i in range(start_round, end_round):
        url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
        result_data = urlopen(url)
        lotto_data = result_data.read()

        soup = bs4.BeautifulSoup(lotto_data, 'html.parser')

        ret = []
        newret = []
        newret.append(i)
        for numbers in soup.findAll('div', attrs={'class': 'nums'}):
            num = numbers.findAll('span')
            ret.append(num)

        ret = ret[0]
        for idx in ret:
            string = str(idx)
            onlynum = re.sub('<.+?>', '', string, 0, re.I | re.S)
            newret.append(onlynum)
            newret = list(map(int, newret))

        num_dict = {}
        for idx, col_name in enumerate(df_train):
            num_dict.update({col_name: newret[idx]})

        print(num_dict)
        df_train = df_train.append(num_dict, ignore_index=True)

df_train.to_csv('input/lotto_data_train.csv', index=False, encoding='euc-kr')
