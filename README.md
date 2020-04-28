# win-acme Python Scripts to Update acme-dns TXT Records

win-acme acme-dns Python 2 Scripts

These python scripts can be modified and used to request SSL certificates using win-acme <https://www.win-acme.com/> on a Windows client using DNS-01 validation with a Linux server running acme-dns <https://github.com/joohoi/acme-dns>

## Guide to Running acme-dns Server

Detailed Guide:  https://community.letsencrypt.org/t/help-me-understand-acme-dns/58892
Official Docs:  https://github.com/joohoi/acme-dns

## Requirements

1. Download and install the latest version of Python 2.7.x for Windows <https://www.python.org/downloads/release/python-2718/>
2. Be sure to configure the installer to add Python to your PATH and install pip with Python.
3. After the installation is complete, launch cmd, and run this command to install requests (a dependency for this script): `pip install requests`

## Usage and Instructions

1. Copy both the acme-dns-create.py and acme-dns-wacs-update.bat files to your desired directory (or even copy them into the win-acme WACS directory)
2. Update the variables in the acme-dns-create.py script with the values obtained from your register endpoint on the acme-dns server:

```
acmeUsername = '{acme-dns-api-username}'  # example: c32612bc-d42c-4abf-ab2d-0e133c184221
acmePassword = '{acme-dns-api-password}'  # example: nbBlgGUXnRExc237BxyoOZ8qmXCs44Y17OAWH8d7
acmeUpdateURL = '{acme-dns-update-url}'   # example:  https://acme.mydomain.com/update
acmeSubdomain = '{acme-dns-api-subdomain}' # example:  97ff4239-ae11-4849-c224-3f5e1ff1abc9
```

3. View the contents in the acme-dns-wacs-win-acme-sample-command file, copy the command, modify it for your usage, and use it to have win-acme obtain SSL certificates using your acme-dns server. 

Command:

```
wacs.exe --target manual --host {DomainToAdd} --webroot {root_to_web_files} --emailaddress {Your_EMAIL} --accepttos --validationmode dns-01 --validation script --dnscreatescript {PATH-TO-acme-dns-wacs-update.bat} --store pemfiles --pemfilespath {PATH_PUT_CERTS}
```

Modified example:

```
wacs.exe --target manual --host test.mydomain.com --webroot C:\httdocs --emailaddress test@mydomain.com --accepttos --validationmode dns-01 --validation script --dnscreatescript C:\Scripts\acme-dns-wacs-update.bat --store pemfiles --pemfilespath C:\certs
```
