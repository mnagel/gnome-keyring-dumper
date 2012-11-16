#!/usr/bin/env python

# this is inspired by http://blog.schmichael.com/2008/10/30/listing-all-passwords-stored-in-gnome-keyring/
 
import pygtk
pygtk.require('2.0')
import gtk # sets app name
import gnomekeyring
 
def hack():
    for keyring in gnomekeyring.list_keyring_names_sync():
        for id in gnomekeyring.list_item_ids_sync(keyring):
            item = gnomekeyring.item_get_info_sync(keyring, id)
            print '[%s] %s = %s' % (
                    keyring, item.get_display_name(), item.get_secret()
            )
        else:
            if len(gnomekeyring.list_item_ids_sync(keyring)) == 0:
                print '[%s] --empty--' % keyring
 
if __name__ == '__main__':
    hack()
