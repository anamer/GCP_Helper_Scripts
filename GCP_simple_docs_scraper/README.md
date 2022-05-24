Simple script to download all GCP docs per topic into one html file

Usage: gcp_docs_all_in_one <paste one doc links from the topic
                                  
Example: Do download DLP docs, go to DLP docs in your browser and paste a link, then run:
                                  
         pyton3 parse_gcp_dos_by_topic.py https://cloud.google.com/dlp/docs/inspect-sensitive-text-api
 
Known Issue:
* Docs are not consistent and thus, in some cases not all will be downloaded
* Not all figure will be downloaded
* Text format may vary
