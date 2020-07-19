import argparse
import math

pay_type = None
payment = None
principal = None
periods = None
interest = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', help='the type of payments: "annuity" or "diff" (differentiated)')
    parser.add_argument('--payment', help='monthly payment', type=int)
    parser.add_argument('--principal', help='to calculate payment', type=int)
    parser.add_argument('--periods', help='the number of months and/or years needed to repay the credit', type=int)
    parser.add_argument('--interest', help='is specified without a percent sign', type=float)

    if parse_args(parser.parse_args()):
        if pay_type == 'annuity':
            if payment is None:
                calculate_payment()
            elif principal is None:
                calculate_principal()
            elif periods is None:
                calculate_periods()
        elif pay_type == "diff":
            calculate_differentiated()
    else:
        print('Incorrect parameters')


def parse_args(args):
    global pay_type
    global payment
    global principal
    global periods
    global interest

    if args.principal and args.principal >= 0:
        principal = args.principal

    if args.periods and args.periods >= 0:
        periods = args.periods

    if args.interest and args.interest >= 0.0:
        interest = args.interest
        if args.type:
            pay_type = args.type

            if args.type == "annuity":
                if args.payment and args.payment >= 0:
                    payment = args.payment
                if (principal is None and periods is None) or \
                        (periods is None and payment is None) or \
                        (payment is None and principal is None):
                    return False
                return True
            elif args.type == "diff":
                if args.payment:
                    return False
                elif principal is not None and periods is not None:
                    return True

    return False


def calculate_payment():
    i = interest / 100 / 12
    annuity = principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    over = math.ceil(annuity) * periods - principal
    print(f'Your annuity payment = {math.ceil(annuity)}!')
    print(f'Overpayment = {over}')


def calculate_principal():
    i = interest / 100 / 12
    P = payment / ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    over = payment * periods - math.floor(P)
    print(f'Your credit principal = {math.floor(P)}!')
    print(f'Overpayment = {over}')


def calculate_periods():
    i = interest / 100 / 12
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    q, r = divmod(n, 12)
    year_str = 'year'
    if q > 1:
        year_str += 's'
    month_str = 'month'
    if r > 1:
        month_str += 's'
    over = payment * n - principal
    if r > 0:
        print(f'You need {q} {year_str} and {r} {month_str} to repay this credit!')
    else:
        print(f'You need {q} {year_str} to repay this credit!')
    print(f'Overpayment = {over}')


def calculate_differentiated():
    i = interest / 100 / 12
    total = 0
    for m in range(1, periods + 1):
        D = principal / periods + i * (principal - principal * (m - 1) / periods)
        total += math.ceil(D)
        print(f'Month {m}: paid out {math.ceil(D)}')
    print()
    over = total - principal
    print(f'Overpayment = {over}')


if __name__ == '__main__':
    main()