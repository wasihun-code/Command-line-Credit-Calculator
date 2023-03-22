import sys
import argparse
from math import ceil, log, floor


def calc_loan_interest(loan_interest):
    return float(loan_interest) / 1200.0


def calc_loan_principal(annuity, period, loan_interest):
    return floor(
        (
            annuity
            / (
                (loan_interest * ((1 + loan_interest) ** period))
                / (((1 + loan_interest) ** period) - 1)
            )
        )
    )


def calc_monthly_payment(loan_principal, annuity, loan_interest):

    denum = annuity - (loan_interest * loan_principal)
    period = ceil((log(((annuity) / denum), 1 + loan_interest)))

    return (int(period / 12), period % 12)


def calc_annuity_payment(loan_principal, period, loan_interest):
    return ceil(
        loan_principal
        * (
            (loan_interest * ((1 + loan_interest) ** period))
            / (((1 + loan_interest) ** period) - 1)
        )
    )


def calc_diff_payment(principal, periods, interest, month):
    return ceil(
        (principal / periods)
        + interest * (principal - ((principal * (month - 1)) / periods))
    )

def calc_over_payment(principal, payment, periods, interest):
    return ceil((payment * int(periods)) - (principal + interest))


def print_num_period(year, month):
    if year and month:
        print(f"It will take {year} years and {month} month to repay this loan!")
    elif year:
        print(f"It will take {year} years to repay the loan!")
    elif month:
        print(f"It will take {month} month to repay the loan!")
    else:
        print(f"No need to pay anything!")


def positive_value(value):

    try:
        float_value = float(value)
        assert float_value >= 0
    except:
        print("Incorrect parameters")
        sys.exit(1)

    return float_value


def prepare_command_line():
    parser = argparse.ArgumentParser(
        description="This program calculates differentiate or annuity payment based on user input"
    )

    parser.add_argument("--type", choices=["annuity", "diff"], help=argparse.SUPPRESS)

    parser.add_argument("--principal", type=positive_value, help=argparse.SUPPRESS)
    parser.add_argument("--interest", type=positive_value, help=argparse.SUPPRESS)
    parser.add_argument("--periods", type=positive_value, help=argparse.SUPPRESS)
    parser.add_argument("--payment", type=positive_value, help=argparse.SUPPRESS)

    return parser
