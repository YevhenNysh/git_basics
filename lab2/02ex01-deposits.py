#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.
Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...
Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.
Let's implement this.
A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.
Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""

def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)

    if(initial_sum != -1):
        return initial_sum * growth
    else:
        return growth

def main(args):
    """Gets called when run as a script."""

    # Check the number of arguments and show usage if incorrect
    if len(args) not in [4, 5]:
        print(f"USAGE: {args[0]} initial_sum percent fixed_period set_period")
        print(f"USAGE: {args[0]} percent fixed_period set_period -p")
        return

    initial_sum = float(args[1])
    percent = float(args[2])
    fixed_period = float(args[3])
    set_period = 0

    if len(args) == 5:
        if args[4] == "-p":
            # Calculate the 1-year percent yield
            set_period = 365
            total = deposit(initial_sum, percent, fixed_period, set_period)
            one_year_percent_yield = ((total / initial_sum) ** (1 / set_period)) - 1
            print(f"One-year percent yield: {one_year_percent_yield:.2%}")
            return
        else:
            print(f"Unrecognized option: {args[4]}")
            return

    # Calculate the total equivalent of money in various periods of time
    periods = [31, 91, 182, 365, 730, 1825, 3650, 7300]
    for period in periods:
        set_period = period
        total = deposit(initial_sum, percent, fixed_period, set_period)
        print(f"{period}-day period: {total:,.2f}")

if __name__ == '__main__':
    import sys

    main(sys.argv)