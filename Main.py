import FundPerformance
import CommandLineParser

def main():
    cli_arguments = CommandLineParser.CommandLineParser.parse()

    performance = FundPerformance.FundPerformance()
    performance.processCLI(cli_arguments)
    performance.calculateBalance()


if __name__ == "__main__":
    main()