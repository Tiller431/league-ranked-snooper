import os as o
import requests as r
import psutil as u 
import json as j
import base64 as b
import time 

riotCertPath = 'C:\\riotgames.pem'


def getHiddenNames():
    # returns a list of all the names of the players in the ranked queue
    [x]=[[i.cmdline()[2].split('=')[1],i.cmdline()[1].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient.exe']
    e=list(r.get(url=f'https://127.0.0.1:{x[0]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[1]}'.encode()).decode()}",'Accept': 'application/json'},verify=riotCertPath))
    return [ i['name'] for i in j.loads(''.join(s.decode() for s in e))['participants']]

def openUgg(name):
    # opens the u.gg page of the player with the given name
    print(f'Opening u.gg page for {name}')
    o.startfile(f'https://u.gg/lol/profile/na1/{name}/overview')

def main():
    global summonerNames
    #check if LeagueClient is running
    if not any(i.name() == 'LeagueClient.exe' for i in u.process_iter()):
        return

    # opens the u.gg page of the player with the given name
    for username in getHiddenNames():
        if username not in summonerNames:
            summonerNames.append(username)
            openUgg(username)
        else:   
            break

if __name__ == '__main__':
    print('Press Ctrl-C or the X button to quit.')
    global summonerNames
    summonerNames = []

    # check if the riotgames.pem file exists
    if not o.path.exists(riotCertPath):
        cert = r.get('https://github.com/Tiller431/league-ranked-snooper/raw/main/riotgames.pem')
        with open(riotCertPath,'wb') as f:
            f.write(cert.content)

    else:
        # check if the riotgames.pem file is valid
        try:
            cert = r.get(url='https://github.com/Tiller431/league-ranked-snooper/raw/main/riotgames.pem')

            # Check file
            with open(riotCertPath,'rb') as f:
                if f.read() != cert.content:
                    f.write(cert.content)
        except:
            print('Error: The riotgames.pem file is invalid and could not be replaced.\nTry deleting the file and restarting the program.\nC:\\riotgames.pem')
            pass
    while True:
        main()
        time.sleep(1)