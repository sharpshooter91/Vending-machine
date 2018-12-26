sodas = ['Pepsi', 'Chery', 'Coce Zero', 'Sprite']
chips = ['Duritos', 'Fritos']
candy = ['Snikers', 'M&Ms', 'Twizlers']

while True:
    choice = input('Whould you like soda, some chips or candy?  ').lower()
    try:
        if choice == 'soda':
            snack = soda.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorru, I didn't understand that." )
            continue
    except IndexError:
        print("We are all out of {}! Sorry!".format(choice))
    else:
        print("Here is yours {}: {}".format(choice, snack))
