import os
ip_range = input("Veuillez rentrer la plage d'IP en notation CIDR: ")
port = input("Veuillez rentrer le port: ")
os.system("sudo zmap -r 200 -o output.csv -p "+port+" "+ip_range)
with open("output.csv") as file:
    while (line := file.readline().rstrip()):
        os.system("curl -vv --silent http://"+line+":"+port+" 2>&1 |grep host")
        os.system("curl -vv --silent http://"+line+":"+port+" 2>&1 |grep etic")