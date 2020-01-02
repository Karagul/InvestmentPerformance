from InvestmentAnalysis import FundPerformance
from InvestmentAnalysis import CommandLineParser

class InvestmentAnalyzer():

    @staticmethod
    def run():
        cli_arguments = CommandLineParser.CommandLineParser.parse()
        
        if cli_arguments['subparser_name'] == 'manage_fund':
            pass
        elif cli_arguments['subparser_name'] == 'manage-transactions':
            pass
        else:
            performance = FundPerformance.FundPerformance()
            performance.processCLI(cli_arguments)
            performance.calculateBalance()