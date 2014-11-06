import os


def disk_usage():
    return os.popen('df -h').read()
