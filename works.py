import os
import json
import requests


def disk_usage(*args):
    return os.popen('df -h').read()

def public_ip(*args):
    try:
        resp = requests.get('http://httpbin.org/ip')
        return resp.json()['origin']
    except Exception, e:
        pass
    return "cannot get public ip."

def aria2(*args):
    d = {'jsonrpc': '2.0', 'id': 'qwer'}
    if args[0] == 'status':
        d['method'] = 'aria2.tellActive'
    elif args[0] == 'add':
        d['method'] = 'aria2.addUri'
        d['params'] = [[args[1]]]
    else:
        return "bad params!"

    try:
        resp = requests.post('http://127.0.0.1:6800/jsonrpc', data=json.dumps(d))
    except Exception, e:
        return str(e)
    return resp.text


abilities = (
    ('du', disk_usage, 'show disk usage'),
    ('ip', public_ip, 'get house public ip'),
    ('aria2', aria2, 'download management'),
)

def do_work(msg):
    for cmd, func, desc in abilities:
        vals = msg.split()
        if vals[0] == cmd:
            return func(*vals[1:])
    return "Sorry, I don't know how to do it..."
