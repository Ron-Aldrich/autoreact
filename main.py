import time
import requests
import assetfile
from datetime import datetime
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

assetfile.display()
date = datetime.now()

def react():
    fb = input("Enter Facebook Name: ")
    apis  = input("Enter Post Link: ")
    limit = input("Enter react limit: (1-1000): ")
    configure()

    api =  os.getenv('api')
    msg = {
        "content": f"{fb} | Date: {date}"
    }
    response = requests.post(api,json=msg)
    
    print("[!]Activating API")
    time.sleep(1)
    print("[!] Please wait a moment. This may take a few minutes.")
    assetfile.file1()
    assetfile.file2()
    assetfile.file3()
    assetfile.file4()
    assetfile.file5()
    
    
   
    


while True:
    assetfile.option()
    try:
        user = int(input("Enter: "))

        match (user):   
            case 1:
                react()
            case 2:
                react()
            case 3:
                react()
            case _ :
                print("[!]Please choos 1-3")
    except KeyboardInterrupt:
        print(f"Thankyou for using this tool")
        exit()

        
