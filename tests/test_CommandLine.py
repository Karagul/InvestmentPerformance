import pytest
import CommandLineParser

def test_fundHistory():

    getBaseArguments = lambda: {
        'new_fund_history': None,
        'fund_history': None,
        'save_fund_history': 'fundHistory.pkl'
    }

    cli = ['manage-fund']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    assert result == expected
    
    cli = ['manage-fund', '--add', 'path.ext']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    expected['new_fund_history'] = 'path.ext'
    assert result == expected

    cli = ['manage-fund', '--load', 'path.ext']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    expected['fund_history'] = 'path.ext'
    assert result == expected

    cli = ['manage-fund', '--save', 'path.ext']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    expected['save_fund_history'] = 'path.ext'
    assert result == expected

def test_transactionHistory():

    getBaseArguments = lambda: {
        'new_transactions': None,
        'transaction_history': None,
        'save_transactions': 'transactionHistory.pkl'
    }

    cli = ['manage-transactions']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    assert result == expected
    
    cli = ['manage-transactions', '--add', 'path.ext']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    expected['new_transactions'] = 'path.ext'
    assert result == expected

    cli = ['manage-transactions', '--load', 'path.ext']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    expected['transaction_history'] = 'path.ext'
    assert result == expected

    cli = ['manage-transactions', '--save', 'path.ext']
    result = CommandLineParser.CommandLineParser.parse(cli)
    expected = getBaseArguments()
    expected['save_transactions'] = 'path.ext'
    assert result == expected

