#! /bin/bash

eval $(dbus-launch "--sh-syntax")
eval $(/usr/bin/gnome-keyring-daemon "--start" "--components=gpg,pkcs11,secrets,ssh")
export $(gnome-keyring-daemon)

python -c "import gnomekeyring;import getpass;p=getpass.getpass();gnomekeyring.unlock_sync(None,p);"
CODE=$?

if [ $CODE -eq 0 ];then
   python "$(dirname $0)/gnome-keyring-dumper.py"
else
   echo "unlocking the keyring failed for some reason" >&2
fi


