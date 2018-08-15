def solve(meal_cost, tip_percent, tax_percent):
    tip=(meal_cost*tip_percent/100)
    tax=(meal_cost*tax_percent/100)
    total = int(round(meal_cost+tip+tax, 0))
    print('The total meal cost is',total,'dollars.')

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)