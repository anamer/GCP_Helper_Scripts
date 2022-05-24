# Simple script to download all GCP docs per topic into one html file
# Usage: gcp_docs_all_in_one <paste one doc links from the topic
# Example: Do download DLP docs, go to DLP docs in your browser and paste a link
#         pyton3 parse_gcp_dos_by_topic.py https://cloud.google.com/dlp/docs/inspect-sensitive-text-api
# 
# Docs are not consistent and thus, in some cases not all will be downloaded
# Not all figure will be downloaded
# Text format may vary
# Authur: namera@

import requests
from bs4 import BeautifulSoup
import sys
import re

 
if (len(sys.argv)) !=2 :
    print ("Please include doc topic to parse. e.g.: python3 parse_all_doc_urls.py certificate-authority-service")
    exit(1)
print(sys.argv[1])

url = sys.argv[1]
doc_topic = (sys.argv[1].split("/"))[3]

base_url = 'https://cloud.google.com/'

print ("Collecting links from: " + url)


reqs = requests.get(url)

soup = BeautifulSoup(reqs.text, 'html.parser')


urls = []
for link in soup.find_all('a'):
    _link = link.get('href')
    #print (_link)
    if _link != None and doc_topic in _link:
        if base_url not in _link:
            _link = base_url + _link
            #print(_link)
            urls.append(_link)

print ("There are %2d urls in the topic's docs" % (len(urls)))
output_file = "./"+doc_topic+"_gcp_doc_all_in-one.html"
doc_file = open(output_file , "w")
print ("Output file "+ output_file + "is  ready, coping docs to file...")

for url in urls:
    print("Processing: " + url)

    result = requests.get(url).text

    doc = BeautifulSoup(result, "html.parser")
    tag = doc.find(class_="devsite-article-body clearfix devsite-no-page-title")
    if tag == None:
        #print ("Url is " + url + "tag is None")
        tag = doc.find(class_="devsite-article-body clearfix")
        
    # write content to a file
    doc_file.write('<p style="background-color:lightgray;"<H1>[ Page URL:' + url + ']</H1></p>')
    doc_file.write(str(tag) )
    doc_file.write("<hr>")

doc_file.close()

print("Script Completed !!! Output file - " + output_file)