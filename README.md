# GNOME Keyring Dumper

This little script dumps all passwords stored in the GNOME keyring to standard output.

I created it to access my saved chromium-browser passwords from remote via SSH.

## Usage

locally (e.g. in gnome-terminal):
```python gnome-keyring-dumper.py```

remote (e.g. when connected via SSH and GNOME and its daemons are not running):
```bash gnome-keyring-dumper.sh```



## Example

```
user@localhost:~$ ssh localhost
Welcome to Ubuntu 12.04.1 LTS (GNU/Linux 3.2.0-33-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

Last login: Fri Nov 16 23:19:00 2012 from localhost
user@localhost:~$ cd gnome-keyring-dumper 
user@localhost:gnome-keyring-dumper$ bash gnome-keyring-dumper.sh
Password: 
[session] --empty--
[login] https://www.foobar.com/login: myname = *****
[login] https://www.example.com/user: userid = *****
[login] https://www.barfoo.com/admin: admin2 = *****
[login] Network secret for Auto WLAN/802-11-wireless-security/wep-key0 = 11111111111111111111111111
[login] Network secret for Auto net/802-11-wireless-security/wep-key0 = 11111111111111111111111111
[login] Network secret for othernet/802-11-wireless-security/wep-key1 = 11111111111111111111111111
user@localhost:gnome-keyring-dumper$ exit
Connection to localhost closed.
user@localhost:~$ 
```

## Python 3

* sudo apt-get install python3-secretstorage
* python3 gnome-keyring-dumper-ng.py

## Links

* http://blog.schmichael.com/2008/10/30/listing-all-passwords-stored-in-gnome-keyring/
* https://launchpad.net/gkeyring
* https://answers.launchpad.net/gkeyring/+question/209138
* https://answers.launchpad.net/gkeyring/+question/211046
* https://bitbucket.org/kang/python-keyring-lib/issue/151/how-is-it-possible-to-list-keyrings-keys