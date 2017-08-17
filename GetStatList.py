#coding utf-8
import pprint
import requests
import json
import sys
import traceback

def main():

    estatAppId       = '取得したappIdを';
    statListFilePath = 'estat_StatList.json'

    #e-Statの統計表情報取得のリクエストURLを呼び出す
    response = requests.get(
        'http://api.e-stat.go.jp/rest/2.1/app/json/getStatsList',
        params={'appId': estatAppId}
        )
    # ファイル出力
    fw = open(statListFilePath, 'w')
    json.dump(response.json(), fw, sort_keys=True, ensure_ascii=False, indent=2)

if __name__=='__main__':
    main()