#! /bin/bash

eval $(dbus-launch "--sh-syntax")
eval $(/usr/bin/gnome-keyring-daemon "--start" "--components=gpg,pkcs11,secrets,ssh")
export $(gnome-keyring-daemon)

python -c "import gnomekeyring;import getpass;p=getpass.getpass();gnomekeyring.unlock_sync(None,p);"

python "$(dirname $0)/gnome-keyring-dumper.py"
