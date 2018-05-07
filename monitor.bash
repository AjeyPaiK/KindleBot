#!/bin/bash

python emaillistener.py

for file in ~/Documents/Saved_PDFs/*;
do
	loc=~/Documents/Conv_PDFs/
	nname=${file##*/}
	name=${file/.pdf/.mobi}
	nfile=$loc$name
	ebook-convert $file $nfile
	rm $file
done

python sendemail.py

for file in ~/Documents/Conv_PDFs/*;
do
	rm $file
done
