import random

def create_deck():
    """
    Creert een kaartendeck met hierin 52 kaarten.
    """    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    return deck

def shuffle_deck(deck):
    """
    Schudt de kaarten uit het kaartendeck.
    """
    random.shuffle(deck)

def deal_cards(deck, num_cards=2):
    """
    Deelt een willekeurige kaart uit het kaartendeck.
    """
    return [deck.pop() for _ in range(num_cards)]

def calculate_hand_value(hand):
    """
    Berekent de waarde waarde van de kaarten in de hand.
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

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def display_hand(hand, player_name):
    print(f"{player_name}'s hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total value: {calculate_hand_value(hand)}\n")

def update_results(wins, losses):
    with open("result.txt", "w") as file:
        file.write(f"Wins: {wins}\nLosses: {losses}")

def restart_game():
    while True:
        play_again = input("Wil je opnieuw spelen? (Ja/Nee): ").lower()
        if play_again == 'nee':
            return False
        elif play_again == 'ja':
            return True
        else:
            print("Ongeldige invoer. Kies 'Ja' of 'Nee'.")

def play_anyway():
    while True:
        play_anyway_input = input("Wil je toch wel spelen? (Ja/Nee): ").lower()
        if play_anyway_input == 'nee':
            return False
        elif play_anyway_input == 'ja':
            return True
        else:
            print("Ongeldige invoer. Kies 'Ja' of 'Nee'.")

def blackjack():
    # Initialize win and loss counters
    wins = 0
    losses = 0

    while True:
        # Stap 1: Creëer een deck of 52 kaarten
        deck = create_deck()

        # Stap 2: Schud de kaarten
        shuffle_deck(deck)

        # Stap 3: Deel 2 kaarten aan de speler en 2 kaarten aan de dealer
        player_hand = deal_cards(deck, 2)
        dealer_hand = deal_cards(deck, 2)

        # Stap 4: Toon de waarde van de kaarten van de speler
        display_hand(player_hand, "Player")

        # Stap 5: Toon de waarde van 1 kaart van de dealer en de andere onbekend
        print("Dealer's hand:")
        print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
        print("Unknown card\n")

        # Stap 6: Vraag de speler om een kaart
        while input("Wil je nog een kaart? (Ja/Nee): ").lower() == 'ja':
            player_hand.extend(deal_cards(deck, 1))
            display_hand(player_hand, "Player")

            # Stap 7: Controleer of de speler boven de waarde van 21 zit
            if calculate_hand_value(player_hand) > 21:
                print("Je hebt verloren! Boven de waarde van 21.")
                losses += 1
                break

        # Stap 8: Toon de tweede kaart van de dealer
        print("Dealer's hand:")
        display_hand(dealer_hand, "Dealer")

        # Stap 9: Dealer trekt kaarten totaalwaarde boven 17 heeft
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.extend(deal_cards(deck, 1))
            display_hand(dealer_hand, "Dealer")

        # Stap 10: Bepaal de winnaar
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        print("Resultaat:")
        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer")

        if player_value > 21:
            print("Je hebt verloren! Boven de waarde van 21.")
            losses += 1
        elif dealer_value > 21 or player_value > dealer_value:
            print("Gefeliciteerd! Je hebt gewonnen.")
            wins += 1
        elif player_value == dealer_value:
            print("Gelijkspel!")
        else:
            print("Je hebt verloren! Dealer heeft een hogere waarde.")
            losses += 1

        # Update results after each round
        update_results(wins, losses)

        # Restart the game or exit
        if not restart_game():
            if play_anyway():
                continue
            else:
                break

if __name__ == "__main__":
    blackjack()
