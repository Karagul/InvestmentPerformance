import datetime
import os
import csv
import pickle

class FundHistory:

    def __init__(self):
        self.history = self.loadHistory()

    def readHistoryFromCSV(self):
        history = {}

        history['ExtendedMarketUnits'] = []

        with open( os.path.join(os.getcwd(), "History_2019_ExtendedMarketUnits.txt")) as f:
            reader = csv.reader(f)
            for row in reader:
                history['ExtendedMarketUnits'].append( ( datetime.datetime.strptime(row[0], '%m/%d/%Y'), float(row[2]) ) )

        return history

    def saveHistory(self):
        with open(os.path.join(os.getcwd(), "fundHistory.pkl"), 'wb') as f:
            pickle.dump(self.history, f)

    def loadHistory(self):
        with open(os.path.join(os.getcwd(), "fundHistory.pkl"), 'rb') as f:
            history = pickle.load(f)

        return history

    def getStartingDate(self):
        return self.history['ExtendedMarketUnits'][0][0]

    def getHistory(self, fundName = None):
        if fundName is None:
            return []

        return self.history[fundName]

    def printHistory(self, name = None):
        if name is None:
            return

        for item in self.history[name]:
            print("{0:s}: ${1:.2f}".format(item[0].strftime("%B %d, %Y"), item[1]) )