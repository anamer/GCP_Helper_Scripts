Simple script to download all GCP docs per topic into one html file

Usage: gcp_docs_all_in_one <paste one doc links from the topic>
                                  
Example: Do download DLP docs, go to DLP docs in your browser and paste a any doc URI, then run:
                                  
         pyton3 parse_gcp_dos_by_topic.py https://cloud.google.com/dlp/docs/inspect-sensitive-text-api
  
Sample files:
  
  [DLP docs](https://link-url-here.org](https://github.com/anamer/GCP_Helper_Scripts/blob/main/GCP_simple_docs_scraper/SampleFile-dlp_gcp_doc_all_in-one.html))
  [Cloud Armor docs](https://github.com/anamer/GCP_Helper_Scripts/blob/main/GCP_simple_docs_scraper/armor_gcp_doc_all_in-one.html)
  
  [Certificate Authority Service](https://github.com/anamer/GCP_Helper_Scripts/blob/main/GCP_simple_docs_scraper/certificate-authority-service_gcp_doc_all_in-one.html)
 
Known Issue:
* Docs are not consistent and thus, in some cases not all will be downloaded
* Not all figure will be downloaded
* Text format may vary
