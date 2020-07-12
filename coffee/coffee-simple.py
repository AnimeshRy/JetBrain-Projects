# water, milk, coffee beans, disposable cups, money
status = [400, 540, 120, 9, -550]

espresso = [250, 0, 16, 1, 4]
latte = [350, 75, 20, 1, 7]
cappuccino = [200, 100, 12, 1, 6]


def machine_status():
    print('\nThe coffee machine has:')
    print(f'{status[0]} of water')
    print(f'{status[1]} of milk')
    print(f'{status[2]} of coffee beans')
    print(f'{status[3]} of disposable cups')
    print(f'{abs(status[4])} of money')


machine_status()

action = input('Write action (buy, fill, take):\n> ')

if action == 'buy':
    buy = input(
        'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> ')
    if buy == '1':
        status = [x - y for x, y in zip(status, espresso)]
        machine_status()
    if buy == '2':
        status = [x - y for x, y in zip(status, latte)]
        machine_status()
    if buy == '3':
        status = [x - y for x, y in zip(status, cappuccino)]
        machine_status()

elif action == 'fill':
    status[0] += int(input('Write how many ml of water do you want to add:\n> '))
    status[1] += int(input('Write how many ml of milk do you want to add:\n> '))
    status[2] += int(input('Write how many grams of coffee beans do you want to add:\n> '))
    status[3] += int(input('Write how many disposable cups of coffee do you want to add:\n> '))
    machine_status()

elif action == 'take':
    print(f'I gave you ${abs(status[4])}')
    status[4] -= status[4]
    machine_status()

else:
    print('\nWrong Input!')
