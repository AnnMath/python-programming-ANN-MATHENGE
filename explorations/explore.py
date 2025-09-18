import random

# Let's do a heckin' explore

def draw_card():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card = f'{random.choice(ranks)}{random.choice(suits)}'
    return card

print('You drew:', draw_card())
