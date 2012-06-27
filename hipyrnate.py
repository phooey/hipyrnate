# A simple script to hibernate a Windows computer after a certain time.
# Author: phooey (http://www.phooey.se)

import argparse
import os
import sys
import threading

def hibernate():
    print("now")
    os.system("shutdown /h /f")
    os._exit(0)

parser = argparse.ArgumentParser(description='Hibernate the computer after a given time.')
parser.add_argument('minutes', type=int, nargs=1, help='the number of minutes to wait before hibernating')
args = parser.parse_args()

minutes = args.minutes[0]
seconds = float(minutes * 60)
t = threading.Timer(seconds, hibernate)
t.start()
message = "Hibernating computer in {} minute(s), press Enter to cancel... ".format(minutes)
input(message)
t.cancel()
