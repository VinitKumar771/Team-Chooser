from random import choice
#players=['A','B','C','D','E','F','G','H','I','J']
players=[]
file=open('players.txt','r')
players=file.read().splitlines()


teamA=[]
teamB=[]


while len(players)>0:
    playerA=choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

print('TEAM A:',teamA)
print('TEAM B:',teamB)
