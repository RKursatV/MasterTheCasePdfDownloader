import re
import urllib.parse

import requests

from rc4 import *

iNeed = input("URL: ")
response = requests.get(iNeed.strip())

# Get the download url from the page
r1 = re.search(r'<a href="\/\?(pdfemb.*\.pdf)"', str(response.content))

# Get the key needed for RC4 decryption from the page
r2 = re.search(r'pdfemb_trans.*"k":(".*"),"is', str(response.content))

if r1 is None or r2 is None:
	print("cannot find an embedded pdf in this page. bye!")
	exit(1)
key = r2.group(1)[1:-1]
url = r1.group(1)
getPdf = requests.post('https://masterthecase.com/?' + url)
filename = urllib.parse.unquote(url).split('/')[-1]

decryptedFile = (RC4(bytes(key, 'utf-8')).crypt(getPdf.content))

with open(filename, 'wb') as f:
	f.write(decryptedFile)
print('Yeeey! ' + filename + ' has successfully been downloaded and decrypted.')
