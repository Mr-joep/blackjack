import random

DEALER_STAND_VALUE = 17
BLACKJACK_VALUE = 21

def create_deck():
    """
    Creates a deck of 52 cards.
    """    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    return deck

def shuffle_deck(deck):
    """
    Shuffles the cards in the deck.
    """
    random.shuffle(deck)

def deal_cards(deck, num_cards=2):
    """
    Deals a specified number of cards from the deck.
    """
    return [deck.pop() for _ in range(num_cards)]

def calculate_hand_value(hand):
    """
    Calculates the total value of the cards in the hand.
    """
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            num_aces += 1

    while value > BLACKJACK_VALUE and num_aces:
        value -= 10
        num_aces -= 1

    return value

def display_hand(hand, player_name):
    """
    Displays the cards in the hand and their total value.
    """
    print(f"{player_name}'s hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total value: {calculate_hand_value(hand)}\n")

def dealer_should_hit(dealer_hand):
    """
    Determines if the dealer should hit based on the hand value.
    """
    return calculate_hand_value(dealer_hand) < DEALER_STAND_VALUE

def is_blackjack(hand):
    """
    Checks if the hand is a blackjack.
    """
    return len(hand) == 2 and calculate_hand_value(hand) == BLACKJACK_VALUE

def get_yes_no_input(prompt):
    """
    Gets a valid yes/no input from the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in ['ja', 'nee']:
            return user_input
        else:
            print("Invalid input. Choose 'Ja' or 'Nee'.")

def blackjack():
    # Create a deck of 52 cards
    deck = create_deck()

    while True:
        # Shuffle the cards
        shuffle_deck(deck)

        # Deal 2 cards to the player and 2 cards to the dealer
        player_hand = deal_cards(deck, 2)
        dealer_hand = deal_cards(deck, 2)

        # Show the value of the player's cards
        display_hand(player_hand, "Player")

        # Show one card of the dealer and keep the other one hidden
        print("Dealer's hand:")
        print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
        print("Unknown card\n")

        # Ask the player for more cards
        while get_yes_no_input("Do you want another card? (Ja/Nee): ") == 'ja':
            player_hand.extend(deal_cards(deck, 1))
            display_hand(player_hand, "Player")

            # Check if the player is over 21
            if calculate_hand_value(player_hand) > BLACKJACK_VALUE:
                print("You lost! Over the value of 21.")
                break

        # Show the second card of the dealer
        print("Dealer's hand:")
        display_hand(dealer_hand, "Dealer")

        # Dealer draws cards until the total value is above 17
        while dealer_should_hit(dealer_hand):
            dealer_hand.extend(deal_cards(deck, 1))
            display_hand(dealer_hand, "Dealer")

        # Determine the winner
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        print("Result:")
        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer")

        if player_value > BLACKJACK_VALUE:
            print("You lost! Over the value of 21.")
        elif dealer_value > BLACKJACK_VALUE or player_value > dealer_value:
            print("Congratulations! You won.")
        elif player_value == dealer_value:
            print("It's a tie!")
        else:
            print("You lost! Dealer has a higher value.")

        # Ask if the player wants to play again
        play_again = get_yes_no_input("Do you want to play again? (Ja/Nee): ")

        if play_again == 'nee':
            while True:
                # Ask if the player changed their mind about playing
                play_again = get_yes_no_input("Do you still want to play? (Ja/Nee): ")

                if play_again == 'ja':
                    break  # Break out of the loop and continue the game
        elif play_again == 'ja':
            continue

if __name__ == "__main__":
    blackjack()
