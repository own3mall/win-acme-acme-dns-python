# win-acme Python Scripts to Update acme-dns TXT Records

win-acme acme-dns Python 2 Scripts

These python scripts show you how to request SSL certificates using win-acme <https://www.win-acme.com/> on a Windows client using DNS-01 validation with a Linux server running acme-dns <https://github.com/joohoi/acme-dns>

## Requirements

1. Download and install the latest version of Python 2.7.x for Windows <https://www.python.org/downloads/release/python-2718/>
2. Be sure to configure the installer to add Python to your PATH and install pip with Python.
3. After the installation is complete, launch cmd, and run this command to install requests (a dependency for this script): `pip install requests`

## Usage and Instructions

1. Copy both the acme-dns-create.py and acme-dns-wacs-update.bat files to your desired directory (or even copy them into the win-acme WACS directory)
2. Update the variables in the acme-dns-create.py script with the values obtained from your register endpoint on the acme-dns server:

```
acmeUsername = '{acme-dns-api-username}'
acmePassword = '{acme-dns-api-password}'
acmeUpdateURL = '{acme-dns-update-url}'
acmeSubdomain = '{acme-dns-api-subdomain}'
```

3. View the contents in the acme-dns-wacs-win-acme-sample-command file, copy the command, modify it for your usage, and use it to have win-acme obtain SSL certificates using your acme-dns server. 
