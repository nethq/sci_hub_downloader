from dataclasses import replace
from gettext import find
from itertools import count
from msilib.schema import Directory
from multiprocessing.connection import wait
from operator import concat, contains
import os
from posixpath import split

from pkg_resources import register_finder
import sci_hub
import re

def sci_hub_download(url):
    if url != "exit":
        temp =sci_hub.getSciHubResponse(url)
        print(temp)
        temp = sci_hub.extract_download_url(url)
        if temp == None:
            return print("No download url found")
        print("Download File ?")
        if input("y/n: ") == "y":
            dw_url= sci_hub.extract_download_url(url)
            #create subdirectory
            dir_name = "sci_hub_downloads"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            #save file        
            # "https://sci-hub.se"
            if contains(url,"//"):
                temp = url[url.find("//")+2:]
            temp = temp[:temp.find("/")]
            site_url = "https://"+temp
            print("Site url ->" + site_url)
            sci_hub.save_file(site_url+dw_url,"sci_hub_downloads/"+dw_url[dw_url.rfind("/")+1:])
            print("Saving file to :"+ dw_url[dw_url.rfind("/")+1:])


print("1.Infinite loop [input url -> download file]\n2.Infinite loop [check url -> enumerate numbers -> download file]")
temp = input("Enter your choice: ")
if temp == "1":
    while True:
        url = input("Enter a url: ")
        sci_hub_download(url)
elif temp == "2":
    while True:
        url = input("Enter a url: ")
        mask = input("Enter mask ($$$$) for all (0000) for none :")
        count_updates = input("Enter range <num> (count of ++): ")#this is integer
        for i in range(int(count_updates)):
            extractedNums = re.findall(r'\d+', url)
            replacementNums = [] 
            for num in extractedNums:
                original = num
                numeric = int(num) 
                num = int(num)
                num = num + 1
                cnt = len(original)
                replacementNums.append(f'{num:0{cnt}d}')
            print(extractedNums)
            #traverse extractednums from end to front
            for i in range(len(extractedNums)):
                if(mask[i]=="$"):
                    url = url.replace(extractedNums[i], replacementNums[i],1)
            print("Testing :" +  url)
            input("Press Enter to continue...")
            sci_hub_download(url)
        