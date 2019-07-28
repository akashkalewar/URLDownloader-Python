import os
import requests
from sys import *
from urllib import *
from urllib.parse import urlparse
from urllib.error import URLError

#To check whether connection is established or not
def isConnection():
    try:
      request.urlopen(url = 'http://216.58.192.142',timeout = 4)
      return True

    except error.URLError as E:
        return False

#To check whether URL is downloadable or not
def is_downloadable(url):
    h = requests.head(url,allow_redirects=True)
    header = h.headers
    content_type = header.get('content_type')  
    return True        

#We parse thr URL then we return the path of URL
def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

#Traverse through the file line by line
def fileData(path):
    connection = isConnection()
    if connection:
        with open(path) as fp:
            for url in fp:
                print(url)
                result = AutoDownload(url)
                if result:
                    print("File Successfully Downloaded")
                else:
                    print("File Failed to Download")
    else:
        print("Connection not established")
        exit()
    
def AutoDownload(url):
        allowed = is_downloadable(url)
        if allowed:
            try:
                filename = get_filename_from_cd(url)
                res = requests.get(url, stream = True)
                with open(filename , "wb") as fd:
                    for chunk in res.iter_content(chunk_size=1024): 
                        if chunk:
                            fd.write(chunk)    
                fd.close()
                return True
         
            except Exception as E:
                return False
            
        else:
            return False
        
def main():
        print("-----Auto Downloader-----")
        
        print("Application name: "+argv[0])
        
        if(len(argv)==2):
            
            #Help
            if(argv[1]=="-h") or (argv[1]=="-H"):
                print("The Script is used to download file")
                exit()
            #Usage 
            if(argv[1]=="-u") or (argv[1]=="-U"):
                print("Downloader_Usage: {sys.argv[0]}  FileName ")
                print("FileName: File which contains list of URL's")
                exit()
                
        if(len(argv)>2):
            print("Invalid Arguments")
            exit()
        
        result = fileData(os.path.abspath(argv[1]))
       

if __name__=="__main__":
    main()
    