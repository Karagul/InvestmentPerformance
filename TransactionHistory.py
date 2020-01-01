import os
import pickle

class TransactionHistory():

    def __init__(self):
        self.transactions = self.loadHistory()

    def readTransactionsfromCSV(self):
        transactions = {}

        transactions['ExtendedMarketUnits'] = []

        with open( os.path.join(os.getcwd(), "TransactionHistory.csv")) as f:
            reader = csv.reader(f)

            # Skip the header
            next(reader)

            for row in reader:
                transactions['ExtendedMarketUnits'].append( ( datetime.datetime.strptime(row[0], '%m/%d/%Y'), float(row[4]) ) )

        return transactions

    def saveHistory(self):
        with open(os.path.join(os.getcwd(), "transactionHistory.pkl"), 'wb') as f:
            pickle.dump(self.transactions, f)

    def loadHistory(self):
        with open(os.path.join(os.getcwd(), "transactionHistory.pkl"), 'rb') as f:
            history = pickle.load(f)

        return history

    def getTransactions(self, fundName = None):
        if fundName is None:
            return []

        return self.transactions[fundName]

    def printHistory(self, name = None):
        if name is None:
            return

        for item in self.transactions[name]:
            print("{0:s}: ${1:.2f}".format(item[0].strftime("%B %d, %Y"), item[1]) )