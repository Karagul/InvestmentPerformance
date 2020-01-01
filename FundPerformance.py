import FundHistory
import TransactionHistory
import datetime
import matplotlib.pyplot as plt
import numpy

class FundPerformance():
    def __init__(self):
        self.fundHistory = FundHistory.FundHistory()
        self.transactions = TransactionHistory.TransactionHistory()

    def processCLI(self, cli_args=None):
        pass

    def calculateBalance(self):
        time = [self.fundHistory.getStartingDate()-datetime.timedelta(1)]
        sharesHeld = []
        sharesHeld.append( 0.0 )
        dailyContributionBalance = []
        dailyContributionBalance.append( 0.0 )

        # Gather contributions and corresponding balances
        for fund_item in self.fundHistory.getHistory('ExtendedMarketUnits'):
            time.append( fund_item[0] )
            newSharesAmount = sharesHeld[-1]
            newContribution = dailyContributionBalance[-1]

            transactions_found = [item[1] for item in self.transactions.getTransactions('ExtendedMarketUnits') if item[0] == fund_item[0] ]
            for trans in transactions_found:
                newSharesAmount = newSharesAmount + trans
                newContribution = newContribution + trans * fund_item[1]

            sharesHeld.append( newSharesAmount )
            dailyContributionBalance.append( newContribution )

        # Remove first entry for shares and contributions
        time.pop(0)
        sharesHeld.pop(0)
        dailyContributionBalance.pop(0)

        # Calculate daily balance
        dailyBalance = []
        for fund_item, shares in zip(self.fundHistory.getHistory('ExtendedMarketUnits'), sharesHeld):
            dailyBalance.append( shares * fund_item[1] )

        print("Ending Number of Shares: {0:.4f}".format(sharesHeld[-1]))
        print("Ending Contribution Balance: ${0:.2f}".format(dailyContributionBalance[-1]))

        # Conversion to Numpy array
        time = numpy.array(time)
        dailyContributionBalance = numpy.array(dailyContributionBalance)
        dailyBalance = numpy.array(dailyBalance)

        plt.figure()
        plt.plot(time, dailyContributionBalance, color='gray')
        plt.plot(time, dailyBalance, color='blue', alpha=0.6)
        plt.fill_between(time, dailyContributionBalance, dailyBalance, where=dailyContributionBalance<=dailyBalance, facecolor='green', alpha=0.4, interpolate=True)
        plt.fill_between(time, dailyContributionBalance, dailyBalance, where=dailyContributionBalance>=dailyBalance, facecolor='red', alpha=0.4, interpolate=True)
        
        plt.figure()
        plt.plot(time, [item[1] for item in self.fundHistory.getHistory('ExtendedMarketUnits')])

        plt.show()