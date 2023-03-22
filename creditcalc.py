import sys
from utilities import (
    calc_annuity_payment, calc_diff_payment, 
    calc_loan_interest, calc_loan_principal,
    calc_monthly_payment, calc_over_payment,
    prepare_command_line, print_num_period
)
from math import ceil

def main():

    parser = prepare_command_line()

    args = parser.parse_args()

    try:
        assert len(vars(args)) >= 5
        assert args.interest is not None
        assert args.type is not None
    except:
        print("Incorrect parameters")
        sys.exit(1)

    interest = calc_loan_interest(args.interest)

    if args.type == "annuity":

        if not args.payment:
            annuity_payment = calc_annuity_payment(
                args.principal, int(args.periods), interest
            )
            print(f"Your annuity payment  = {annuity_payment}!")
            print(
                f"Overpayment = {calc_over_payment(args.principal, annuity_payment, args.periods, interest)}"
            )

        elif not args.principal:
            loan_principal = calc_loan_principal(
                args.payment, int(args.periods), interest
            )
            print(f"Your loan principal = {loan_principal}")
            print(
                f"Overpayment = {calc_over_payment(loan_principal, args.payment, int(args.periods), interest)}"
            )

        elif not args.periods:
            year, month = calc_monthly_payment(args.principal, args.payment, interest)
            print_num_period(year, month)
            print(
                f"Overpayment = {calc_over_payment(args.principal, args.payment, int(year * 12), interest)}"
            )

    else:

        try:
            if args.payment is not None:
                assert args.principal is None
                assert args.periods is None
        except:
            print("Incorrect parameters: diff combination")
            sys.exit(1)

        total_payment = 0
        for month in range(1, int(args.periods) + 1):
            diff_payment = calc_diff_payment(
                args.principal, int(args.periods), interest, month
            )
            total_payment += diff_payment
            print(f"Month {month}: payment is {diff_payment}")

        print()
        print(f"Overpayment = {ceil(total_payment - args.principal)}")


if __name__ == "__main__":
    main()
