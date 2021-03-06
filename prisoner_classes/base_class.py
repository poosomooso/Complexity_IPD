# Create a class that extends this one
# Make sure to use Python 3 syntax since I built the tournament system in 3
class Prisoner:
    def __init__(self):
        self.history = []
        # TODO: Give your class a name for me to refer to it by
        self.name = 'Default'
        
    def getHistory(self):
        return self.history
    
    def addToHistory(self, decision):
        self.history.append(decision)
        return
    
    def makeDecision(self, history):
        '''
        Input: List containing the history of the opposing agent's decisions throughout previous games
        
        Output: The character 'C' or 'D', to represent the agent's choice to either cooperate or defect
        '''
        # TODO: Overwrite this function yourself!
        return 'D'
    
    def playDilemma(self, opponent):
        decision = self.makeDecision(opponent.getHistory())
        self.addToHistory(decision)
        return decision

class Snail(Prisoner):
    def __init__(self):
        self.name = 'Snail'

    def makeDecision(self, history):
        lag = 5
        if len(history) > lag:
            return 'C' if history[-lag] == 'C' else 'D'
        return 'D'