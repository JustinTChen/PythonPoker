from card import *
from player import *
from pokerhands import *
import time

start = time.time()

def run():
    f = open('poker.txt')

    lplayer1=Player()
    lplayer2=Player()

    pokerHands=PokerHands()

    wins1 = 0

    for line in f.readlines():
        lhands=[]
        cardsString=line.split(" ")

        for lcardString in cardsString:
            lhands.append(Card(lcardString))

        lplayer1.sethand(lhands[0:5])
        lplayer2.sethand(lhands[5:10])

        if getWinner(lplayer1, lplayer2) == "Player 1 wins!":
            wins1 += 1
    
    f.close()
    return wins1

    #print("Player 1")
    #print(pokerHands.getplayerHandScore(lplayer1))
    #print(lplayer1.gethand()[0].getsuit())
    

# testcards=[Card("JD"), Card("TS"), Card("QD"), Card("KC"), Card("AC")]
# lplayer=Player()
# lplayer.sethand(testcards)
# poker=PokerHands()


# testcards2=[Card("JD"), Card("TS"), Card("QD"), Card("KC"), Card("AC")]
# lplayer2=Player()
# lplayer2.sethand(testcards2)


def getWinner(player1, player2):
    poker = PokerHands()
    hand1, hand2 = poker.getplayerHandScore(player1), poker.getplayerHandScore(player2)
    if hand1[0] > hand2[0]:
        return "Player 1 wins!"
    elif hand1[0] == hand2[0]:
        if hand1[1] > hand2[1]:
            return "Player 1 wins!"
        elif hand1[1] == hand2[1]:
            temp1, temp2 = player1.getranking(), player2.getranking()
            for i in [4, 3, 2, 1, 0]:
                if temp1[i] > temp2[i]:
                    return "Player 1 wins!"
                    break
                if temp1[i] < temp2[i]:
                    return "Player 2 wins!"
                    break
                if i == 0:
                    return "Tie!"
        else:
            return "Player 2 wins!"
    else:
        return "Player 2 wins!"


print(run())

end = time.time()

print(end - start)


#print(poker.checkStraightFlush(testcards))

