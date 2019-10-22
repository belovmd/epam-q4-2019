dollars, cents, items = (int(i) for i in input('Price and items: ').split())
cents_in_dollars = dollars * 100
total_cents = (cents_in_dollars + cents) * items
cost_dollars, cost_cents = total_cents // 100, total_cents % 100
print('Total cost: {} dollars {} cents'.format(cost_dollars, cost_cents))
