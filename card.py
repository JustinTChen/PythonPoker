class Card:
    # attributes
    __fsuit=""
    __fvalue=""

    # method
    def __init__(self, acard):
        self.__fsuit=acard[1]
        self.__fvalue=acard[0]

    def getvalue(self):
        return self.__fvalue

    def getsuit(self):
        return self.__fsuit
