def format_price(price):
    formatted_price = int(price)
    return f'Цена: {formatted_price} руб.'

if __name__ == '__main__':
    print(format_price(56.24))

