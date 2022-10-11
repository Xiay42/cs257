import csv

def convert (sourceName, playersCsvName, gamesCsvName, linksCsvName):
    myPlayersList = []
    myPlayersCountList = []
    myGamesList = []
    myLinksList = []
    with open(sourceName) as sourcefile:
        source = csv.reader(sourcefile)
        with open(playersCsvName, 'w', newline='') as playersCsv:
            playersWriter = csv.writer(playersCsv)
            with open(gamesCsvName, 'w', newline='') as gamesCsv:
                gamesWriter = csv.writer(gamesCsv)
                with open(linksCsvName, 'w', newline='') as linksCsv:
                    linksWriter = csv.writer(linksCsv)
                    for x, line in enumerate(source):
                        print(line[0])
                        playersData = [line[1], line[2], line[3], line[4], line[5], line[6], line[14]]
                        gamesData = [len(myGamesList), line[7], line[8], line[9], line[10], line[11], line[12], line[13]]
                        if playersData not in myPlayersCountList:
                            myPlayersCountList.append(playersData)
                            sortedPlayersData = [len(myPlayersList)] + playersData
                            myPlayersList.append(sortedPlayersData)
                        myGamesList.append(gamesData)
                        myLinksList.append([len(myPlayersList)-1, len(myGamesList)-1])
                    for p in myPlayersList:
                        playersWriter.writerow(p)
                    for g in myGamesList:
                        gamesWriter.writerow(g)
                    for l in myLinksList:
                        linksWriter.writerow(l)

# convertGames('apple.csv', 'grape.csv')
convert('apple.csv', 'pear.csv', 'grape.csv', 'lemon.csv')
# makeLinks('pear.csv', 'grape.csv', 'lemon.csv')