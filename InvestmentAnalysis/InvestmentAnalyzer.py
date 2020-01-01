from InvestmentAnalysis import FundPerformance
from InvestmentAnalysis import CommandLineParser

class InvestmentAnalyzer():

    @staticmethod
    def run():
        cli_arguments = CommandLineParser.CommandLineParser.parse()

        performance = FundPerformance.FundPerformance()
        performance.processCLI(cli_arguments)
        performance.calculateBalance()