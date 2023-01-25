import requests
def get(url):
    response = requests.get(url)
    print(url)
    print(response.status_code)
    print(response.text)
def post(url, data):
    response = requests.post(url, data=data)
    print(url)
    print(response.status_code)
    print(response.text)
if __name__ == '__main__':
    # helloパラメータなし
    url = 'http://localhost:9000/api/hello'
    get(url)
    # helloパラメータあり
    url = 'http://localhost:9000/api/hello?name=Truefly'
    get(url)
    # articles 全件取得
    url = 'http://localhost:9000/api/articles'
    get(url)
    # articles ID1取得
    url = 'http://localhost:9000/api/articles/1'
    get(url)
    # articles ID7取得
    url = 'http://localhost:9000/api/articles/7'
    get(url)
    # ariticles 登録
    url = 'http://localhost:9000/api/articles'
    data = {
        'title': 'TypeScriptはじめました',
        'link': 'https://www.true-fly.com/entry/2022/03/09/073000',
    }
    post(url, data)