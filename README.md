masterthecase.com Protected Pdf Downloader
==============================


A silly script that helps to download pdf files from https://masterthecase.com where all the pdf files are protected by a WordPress plugin called "Pdf Embedder Premium Secure", http://wp-pdf.com/

I wanted to share this script because it can easily be manipulated to download pdf files from other websites protected by the same plugin. 

### How It Works

Pdf Embedder Premium Secure plugin stores pdf files that are encrypted by using RC4 cipher with a randomly generated 256 bit key. The plugin decrypts pdf files on the fly while showing pdf files to the user. This script gets the key from the page and converts crypted data into pdf file and saves it.

### Installing

First, get the script codes, by either [downloading the zip](https://github.com/RKursatV/MasterTheCasePdfDownloader/archive/main.zip) and extracting files or using git:

```
git clone git@github.com:RKursatV/MasterTheCasePdfDownloader.git
```

And run the command below to get required Python libraries

```
pip3 install -r requirements.txt
```

That's it.

### How To Use
Run the script and type the link of the page that consists the protected pdf file. 

Example run:
```
└─[$]> python3 masterthecase.py 
URL: https://masterthecase.com/case-interview-casebook-mccombs-2007/
Yeeey! Case-Interview-Casebook-MasterTheCase-McCombs-2007.pdf has successfully been downloaded and decrypted.
```
