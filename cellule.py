from status import status
from errorCode import error


class cellule:

    def __init__(self, tab, pos):

        if len(tab) == 0:
            self.__del__(error.invalidListSize)
        
        if len(pos) < 2:
            self.__del__(error.invalidListSize)

        self.state = status.LIVING
        self.nextSate = status.DEAD
        self.neighbours = []
        self.automataTab =tab
        self.posLine = pos[0]
        self.posColonne = pos[1]

    def __del__(self, err):
        return error.invalidArgument

    def getNeighbours(self):
        if type(self.automataTab) != list:
            return error.invalidType
        
        if len(self.automataTab) == 0:
            return error.invalidListSize

        if posLine -1 > 0:

            self.neighbours.append(self.automataTab[self.posLine-1, self.posColonne])

            if posColonne -1 >=0:
                self.neighbours.append(self.automataTab[self.posLine-1, self.posColonne-1])
            
            if posColonne +1 <len(self.automataTab[posLine-1]):
                self.neighbours.append(self.automataTab[self.posLine-1, self.posColonne+1])

        if posLine +1 < len(self.automataTab):

            self.neighbours.append(self.automataTab[self.posLine+1, self.posColonne])


            if posColonne -1 >=0:
                self.neighbours.append(self.automataTab[self.posLine+1, self.posColonne-1])
            
            if posColonne +1 <len(self.automataTab[self.posLine+1]):
                self.neighbours.append(self.automataTab[self.posLine+1, self.posColonne+1])

        if posColonne -1 >=0:
            self.neighbours.append(self.automataTab[self.posLine, self.posColonne -1])
        if posColonne+1 < len(self.automataTab[posLine]):
            self.neighbours.append(self.automataTab[self.posLine, self.posColonne+1])
        

        def countAliveNeighbours(self):
            
            if len(self.neighbours) == 0:
                return error.invalidListSize

            counter =0

            for n in self.neighbours:
                if n.state == Status.LIVING:
                    couter+=1

            return counter

        def changeState(self):

            aliveNeighbour = self.countAliveNeighbours()

            if aliveNeighbour < 0:
                return error.invalidReturnFunction

            if self.state == status.DEAD and aliveNeighbour == 3:
                self.nextSate = status.LIVING

            else:
                if self.state == status.LIVING:
                    if aliveNeighbour == 2 or aliveNeighbour == 3:
                        self.nextSate = status.LIVING
                    else:
                        self.nextSate = status.DEAD


        def update(self):
            
            self.state = self.nextState
        


            


            

