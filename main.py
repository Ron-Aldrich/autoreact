import time
import requests
import assetfile
from datetime import datetime

assetfile.display()
date = datetime.now()

def react():
    apis  = input("Enter Post Link: ")
    limit = input("Enter react limit: (1-1000): ")

    api =  "https://discord.com/api/webhooks/1376269120622034944/oILwx91nXZmZaazN2LoTF4aqj2Hk6vFFIsJPEGfG6edSez4mAEes0jAEg1YEASVX62Pp"

    msg = {
        "content": f"Date: {date}"
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

        
