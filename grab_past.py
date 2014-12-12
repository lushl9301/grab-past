#gsettings set org.gnome.desktop.background picture-uri "file:/home/lu/PycharmProjects/grab_past/wallpaper.jpg"

import os

_picpath_ = ".tmp/"
_wallpaper_ = "wallpaper.png"
_interval_ = 300
from time import sleep


def grab_and_save():
    if not os.path.exists(_picpath_):
        os.makedirs(_picpath_)

    import datetime as dt
    from pyscreenshot import grab_to_file

    stored_grabbed_pic = _picpath_ + "." + str(dt.datetime.now()) + ".png"
    grab_to_file(stored_grabbed_pic)
    return stored_grabbed_pic

from sys import argv
if len(argv) > 1:
    arg = argv[1] #argv[0] is grab_past.py
    try:
        _interval_ = int(arg)
    except:
        print("not an integer, default using 5min")
        pass
else:
    print("Default using 5min as interval.")
    print("     If you want to change, please try: python grab_past.py 180")
    print("     It will set the interval to 3min.")

while 1 != 0:
    filename = grab_and_save()
    print(filename)
    from shutil import copyfile
    copyfile(filename, _wallpaper_)
    sleep(_interval_)