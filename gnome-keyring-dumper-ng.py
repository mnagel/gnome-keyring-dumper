#! /usr/bin/env python

# this is inspired by https://bitbucket.org/kang/python-keyring-lib/issue/151/how-is-it-possible-to-list-keyrings-keys

import secretstorage

def hackng():
    bus = secretstorage.dbus_init()
    for keyring in secretstorage.get_all_collections(bus):
        for item in keyring.get_all_items():
            if item.is_locked(): 
                item.unlock()
            attr = item.get_attributes()
            if attr and 'username_value' in attr:
                print('[%s] %s: %s = %s' % (
                    keyring.get_label(),
                    item.get_label(),
                    attr['username_value'],
                    item.get_secret()
                ))
            else:
                print('[%s] %s = %s' % (
                    keyring.get_label(),
                    item.get_label(),
                    item.get_secret()
                ))

if __name__ == '__main__':
    hackng()
