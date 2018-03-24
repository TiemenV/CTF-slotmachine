import random

FRUITS = ['🍌', '🍒', '🍐', '🍈', '🍇', '🍊', '🍉']
COMBOS = {
	'🍌3': 1,
	'🍒2': 1,
	'🍐2': 3,
	'🍈2': 3,
	'🍇2': 3,
	'🍊2': 3,
	'🍉2': 3,
	'🍒3': 3,
	'🍐3': 10,
	'🍈3': 10,
	'🍇3': 10,
	'🍊3': 10,
	'🍉3': 10
}

def line():
	return [random.choice(FRUITS) for i in range(3)]

def payout(line):
	for fruit in line:
		combo = fruit + str(line.count(fruit))
		if combo in COMBOS:
			return COMBOS[combo]
	return 0


print('Welcome to Fruit Slots!\n')
print('We\'ve given you $10.00 on the house.\n')
print('Once you\'re a high roller, we\'ll give you a flag.\n')


def slots():
    money = 10
    while True:
    	print('You have ${0:.2f}.\n'.format(money))
    	bet = input('Place your bets: ')
    	try:
    		bet = float(bet)
    	except:
    		print('Your bet must be a number!\n')

    		return
    	if bet <= 0:
    		print('Sneaky, but not good enough.\n')

    		return
    	elif bet > money:
    		print('You don\'t have enough money to wager this.\n')
    		return
    	line1 = line()
    	line2 = line()
    	line3 = line()
    	while payout(line2):
    		line2 = line()
    	win = bet * payout(line2)
    	money += win - bet
    	print('{}\n{} ◀\n{}\n'.format(' : '.join(line1), ' : '.join(line2), ' : '.join(line3)))
    	if win > 0:
    		print('You won ${0:.2f}!'.format(win))
    	else:
    		print('You lost everything.\n')
    	if money <= 0:
    		print('You have no money left. Low roller.\n')
    		return
    	elif money < 100000000:
    		print('Play more to become a high roller!\n')
    	else:
    		print('Wow, you\'re a high roller!\n')
    		print('You broke the slotmachine!\n')
    		return

slots()