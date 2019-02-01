class PokerHands:


    def getplayerHandScore(self, aplayer):
        if self.checkRoyalFlush(aplayer.gethand())[0]:
            #print("Royal Flush")
            return [9, self.checkRoyalFlush(aplayer.gethand())[1]]
        elif self.checkStraightFlush(aplayer.gethand())[0]:
            #print("Straight Flush")
            return [8, self.checkStraightFlush(aplayer.gethand())[1]]
        elif self.checkFourOfAKind(aplayer.gethand())[0]:
            #print("Four Of a Kind")
            return [7, self.checkFourOfAKind(aplayer.gethand())[1]]
        elif self.checkFullHouse(aplayer.gethand())[0]:
            #print("Full House")
            return [6, self.checkFullHouse(aplayer.gethand())[1]]
        elif self.checkFlush(aplayer.gethand())[0]:
            #print("Flush")
            return [5, self.checkFlush(aplayer.gethand())[1]]
        elif self.checkStraight(aplayer.gethand())[0]:
            #print("Straight")
            return [4, self.checkStraight(aplayer.gethand())[1]]
        elif self.checkThreeOfAKind(aplayer.gethand())[0]:
            #print("Three of a kind")
            return [3, self.checkThreeOfAKind(aplayer.gethand())[1]]
        elif self.checkTwoPairs(aplayer.gethand())[0]:
            #print("Two pairs")
            return [2, self.checkTwoPairs(aplayer.gethand())[1]]
        elif self.checkOnePair(aplayer.gethand())[0]:
            #print("One pair")
            return [1, self.checkOnePair(aplayer.gethand())[1]]
        else:
            return [0, 0]

    def getHighCardValueInt(self, acards):
        lcardsRankAsscending=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        lcardsRankInt=[lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]
        return max(lcardsRankInt) + 2

    def checkOnePair(self, acards):
        lresult=False
        lcardsRankAsscending=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        lcardsRankInt=[lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]
        lcardsKind=[0]*13
        lcardPairs=0
        highest = 0

        for lcardRankInt in lcardsRankInt:
            lcardsKind[lcardRankInt]=lcardsKind[lcardRankInt]+1

        count = 2
        for lcardKind in lcardsKind:
            if lcardKind==2:
                lcardPairs=lcardPairs+1
                highest = count
            count += 2

        if lcardPairs==1:
            lresult=True

        return [lresult, highest]

    def checkTwoPairs(self, acards):
        lresult=False
        lcardsRankAsscending=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        lcardsRankInt=[lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]
        lcardsKind=[0]*13
        lcardPairs=0
        highest = 0

        for lcardRankInt in lcardsRankInt:
            lcardsKind[lcardRankInt]=lcardsKind[lcardRankInt]+1

        count = 2
        for lcardKind in lcardsKind:
            if lcardKind==2:
                lcardPairs, highest = lcardPairs+1, count
            count += 1

        if lcardPairs==2:
            lresult=True

        return [lresult, highest]

    def checkThreeOfAKind(self, acards):
        lresult=False
        lcardsRankAsscending=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        lcardsRankInt=[lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]
        lcardsKind=[0]*13
        val = 0

        for lcardRankInt in lcardsRankInt:
            lcardsKind[lcardRankInt]=lcardsKind[lcardRankInt]+1

        count = 2
        for lcardKind in lcardsKind:
            if lcardKind==3:
                lresult, val =True, count
                break
            count += 1

        return [lresult, val]


    def checkStraight(self, acards):

        lcardsRankAsscending=["A","2","3","4","5","6","7","8","9","T","J","Q","K"]

        lcardRankInt=[lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]

        lcardRankInt.sort()

        if lcardRankInt == [0, 9, 10, 11, 12]:
            return [True, 14]

        for i in range(len(lcardRankInt)-1):
            if lcardRankInt[i]!=lcardRankInt[i+1]-1:
                return [False]

        if len(set(lcardRankInt)) != 5:
            return [False]

        return [True, lcardRankInt[4] + 1]

    def checkFlush(self,acards):
        lresult=True

        lcardtest=acards[0]

        for lcard in acards:
            if lcard.getsuit()!=lcardtest.getsuit():
                lresult=False
                break

        return [lresult, self.getHighCardValueInt(acards)]

    def checkFullHouse(self,acards):
        return [self.checkThreeOfAKind(acards)[0] and self.checkOnePair(acards)[0], self.checkThreeOfAKind(acards)[1]]

    def checkFourOfAKind(self,acards):
        lresult=False
        lcardsRankAsscending=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        lcardsRankInt=[lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]
        lcardsKind=[0]*13
        val = 0

        for lcardRankInt in lcardsRankInt:
            lcardsKind[lcardRankInt]=lcardsKind[lcardRankInt]+1

        count = 2
        for lcardKind in lcardsKind:
            if lcardKind==4:
                lresult=True
                val = count
                break
            count += 1

        return [lresult, val]

    def checkStraightFlush(self,acards):
        return [self.checkStraight(acards)[0] and self.checkFlush(acards)[0], self.getHighCardValueInt(acards)]

    def checkRoyalFlush(self, acards):
        lresult=False
        lsamesuit=True
        lroyalflush=0

        lcardtest=acards[0]

        for lcard in acards:
            if lcard.getsuit()!=lcardtest.getsuit():
                lsamesuit=False
                break
            else:
                if lcard.getvalue()=="T":
                    lroyalflush=lroyalflush+1
                if lcard.getvalue()=="J":
                    lroyalflush=lroyalflush+1
                if lcard.getvalue()=="K":
                    lroyalflush=lroyalflush+1
                if lcard.getvalue()=="Q":
                    lroyalflush=lroyalflush+1
                if lcard.getvalue()=="A":
                    lroyalflush=lroyalflush+1

        if lroyalflush==5 and lsamesuit:
            lresult=True

        return [lresult, self.getHighCardValueInt(acards)]
