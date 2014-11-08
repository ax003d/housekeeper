import os
import requests


def disk_usage():
    return os.popen('df -h').read()

def public_ip():
    try:
        resp = requests.get('http://httpbin.org/ip')
        return resp.json()['origin']
    except Exception, e:
        pass
    return "cannot get public ip."


abilities = (
    ('du', disk_usage, 'show disk usage'),
    ('ip', public_ip, 'get house public ip'),
)

def do_work(msg):
    for cmd, func, desc in abilities:
        if msg == cmd:
            return func()
    return "Sorry, I don't know how to do it..."
