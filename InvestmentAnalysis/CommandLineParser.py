import argparse

class CommandLineParser():

    @staticmethod
    def parse(cli=None):

        parser = argparse.ArgumentParser(description="Manage investment performance")
        sub_parsers = parser.add_subparsers(dest='subparser_name')

        fund_parser = sub_parsers.add_parser('manage-fund', description='Manages fund history')
        fund_parser.add_argument('--add', dest='new_fund_history', help='Adds history to fund performance')
        fund_parser.add_argument('--load', dest='fund_history', help='Database of fund history')
        fund_parser.add_argument('--save', dest='save_fund_history', help='Where to save fund history', default='fundHistory.pkl')

        trans_parser = sub_parsers.add_parser('manage-transactions', description='Manages transaction history')
        trans_parser.add_argument('--add', dest='new_transactions', help='Adds to transaction history')
        trans_parser.add_argument('--load', dest='transaction_history', help='Database of transaction history')
        trans_parser.add_argument('--save', dest='save_transactions', help='Where to save transaction history', default='transactionHistory.pkl')

        args = parser.parse_args(cli)

        return vars(args)