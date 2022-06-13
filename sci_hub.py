import html
import requests
import urllib


def get_whole_html(url):
    response = requests.get(url)
    html_string = response.text
    return html_string

def getSciHubResponse(url):
    ## get the div content
    string = url
    response = requests.get(string)
    html_string = response.text
    #<div id = "citation"'
    temp = '<div id = "citation" onclick = "clip(this)">'
    div_start = html_string.find('<div id = "citation" onclick = "clip(this)">')
    div_end = html_string.find('</div>', div_start)
    div_content = html_string[div_start+len(temp):div_end]
    return div_content

pdf_path = ""
def save_file(download_url, filename):
    response = urllib.request.urlopen(download_url)  
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()

def extract_download_url(url):
    temp= get_whole_html(url)
    if "/downloads/" in temp:
        substr = temp[temp.find("/downloads/"):(temp.find(".pdf")+4)]
        return substr
        
 