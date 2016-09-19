#!/usr/bin/env python

import sys;
import requests;
from lxml import etree;
import unicodedata;

if(len(sys.argv) != 3):
	print("\n\tUsage: "+sys.argv[0]+" <URL> <xpath expression>\n");
	exit(0);

try:
    temp = list()
    req = requests.request('GET', sys.argv[1]);
    document = etree.HTML(str(req.content));
    data = document.xpath(sys.argv[2]);
    for word in sorted(data):
        if(len(word)>2):
            word = unicodedata.normalize("NFKD", unicode(word));
            word = word.encode("ascii", "ignore");
            word = word.strip();
            temp.append(word);
    for word in sorted(temp):
        print word;
except requests.exceptions.MissingSchema:
    print("\n\tMissing protocol. Specify http or https.\n");
    exit(0);
