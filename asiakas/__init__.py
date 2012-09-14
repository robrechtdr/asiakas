from __future__ import with_statement
import requests
import html2text
import os.path

def get_request(url):
    req_get = requests.get(url)
    cont = unicode(req_get.content, "utf-8")
    if len(cont) == 0:
        if req_get.status_code == 200:
            print html2text.html2text(cont)
        elif req_get.status_code == 404:
            print "Error 404, Not Found!"
        elif req_get.status_code == 500:
            print "Error 500, Internal server error!"
        else:
            print html2text.html2text(cont)

    # If non-empty content is detected, print it.
    # This is to allow customised html error messages.
    else:
        print html2text.html2text(cont)

def main():
    init_path = os.path.abspath(__file__)
    if init_path.endswith(".pyc"):
        acii_path = init_path.replace("/__init__.pyc", "/ascii-art.txt")
    else:
        acii_path = init_path.replace("/__init__.py", "/ascii-art.txt")

    with open(acii_path, 'r') as f:
        print f.read()
    print "Asiakas - A tiny python text-based web browser\n".center(78)
    print "Type 'quit' to shut down the browser.".center(78)

    while True:
        link = raw_input("URL: ")
        if link == "quit":
            break
        else:
            pass
        get_request(link)

if __name__ == "__main__":
    main()
