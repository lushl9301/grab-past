###Grab Past

>What am I doing just now?

>Did I just keep watching YouTube for 2 hours?

Grab Past is a simple idea to solve this.
It will grab your screenshot, and set it to your desktop background.

It's easy for you to ```monitor``` yourself! :D

#####Environment
    Linux dabian 3.2.0-4-amd64 #1 SMP Debian 3.2.63-2+deb7u2 x86_64 GNU/Linux
    python 2.7.3
    Gnome Version 3.4.2

#####Settings
**Important**

    mkdir <your directory>grab_past
    cp grab_past.py <your directory>grab_past
    sudo gsettings set org.gnome.desktop.background picture-uri "file:/<your directory>/grab_past/wallpaper.jpg"

#####Dependencies
[pyscreenshot](https://pypi.python.org/pypi/pyscreenshot)

    pip install pyscreenshot

#####Example
python grab_past.py

>It will grab screenshot with 5min interval

python grab_past.py 180

>It will grab screenshot with 3min interval