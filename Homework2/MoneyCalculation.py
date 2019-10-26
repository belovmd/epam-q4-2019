if __name__ == '__main__':
    dollars = int(input('Enter dollars '))
    cents = int(input('Enter cents '))
    quantity = int(input('Enter quantity '))
    total_price = (dollars * 100 + cents) * quantity
    print('Total price: {} dollars '
          '{} cents'.format(total_price // 100, total_price % 100))
