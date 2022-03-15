# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("logindemo-239b8-firebase-adminsdk-yrokn-f527ac27ba.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://logindemo-239b8.firebaseio.com/'})

root = db.reference()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    gpsCoordinate = db.reference('appusers/opLCMhzkgTULMti9dp5X4sywGDw1/gps')
    while True:
        time.sleep(1)
        value = gpsCoordinate.get()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
