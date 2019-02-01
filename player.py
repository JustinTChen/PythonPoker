class Player:
    # attributes
    __fhand = [None] * 5
    ranking = [None] * 5
    lcardsRankAsscending=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    

    # method
    def __init__(self):
        self.__fhand=[None] * 5

    def sethand(self, acards):
    	self.__fhand = acards
    	self.ranking = [2 + self.lcardsRankAsscending.index(lcard.getvalue()) for lcard in acards]
    	self.ranking.sort()
        

    def gethand(self):
        return self.__fhand 

    def getranking(self):
    	return self.ranking
