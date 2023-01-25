def get(id: int = None):
    data = [
        {
            'id': '1',
            'title': 'Cloud FunctionsでGoogle Search Consoleのデータ収集を完全自動化する',
            'link': 'https://www.true-fly.com/entry/2022/04/18/080000',
        },
        {
            'id': '2',
            'title': 'PythonでGoogle Search ConsoleのデータをBigQueryにロードする',
            'link': 'https://www.true-fly.com/entry/2022/04/11/073000',
        },
        {
            'id': '3',
            'title': '【TypeScript超入門】TypeScript + webpackでWebアプリケーション開発環境を構築する',
            'link': 'https://www.true-fly.com/entry/2022/03/14/080000',
        },
    ]
    if id:
        for row in data:
            if row['id'] == id:
                return row
        return {}
    else:
        return data
def post(title:str, link:str):
    print(title)
    print(link)
    return {
        'id': '4',
        'title': title,
        'link': link,
    }