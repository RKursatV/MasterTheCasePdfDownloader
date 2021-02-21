MasterTheCasePdfDownloader
==============================

What Is This?
-------------

A silly script that helps to download pdf files from https://masterthecase.com where all the pdf files are protected by a WordPress plugin called "Pdfembedder Premium Secure", http://wp-pdf.com/

I wanted to share this script because it can easily be manipulated to download pdf files from other websites protected by the same plugin. 

### Installing

First, get the script codes, by either [downloading the zip](https://github.com/RKursatV/MasterTheCasePdfDownloader/archive/main.zip) and extracting files or using git:

```
git@github.com:RKursatV/MasterTheCasePdfDownloader.git
```

And run the command below to get required Python libraries

```
pip3 -r requirements.txt
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
