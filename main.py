import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    # Player deal
    card1 = cards[random.randint(0, len(cards) - 1)]
    card2 = cards[random.randint(0, len(cards) - 1)]
    your_cards = [card1, card2]
    total = sum(your_cards)
    print(f"Your cards are: {your_cards} and your total is: {total}")

    # Dealer deal
    dealer_card1 = cards[random.randint(0, len(cards) - 1)]
    dealer_cards = [dealer_card1]
    dealer_total = sum(dealer_cards)
    print(f"Dealer's first card is: {dealer_card1}")
    
    # Player_turn
    draw_next = input("Do you want to draw another card? (y/n): ")
    while draw_next.lower() == 'y':
        new_card = cards[random.randint(0, len(cards) -1)]
        your_cards.append(new_card)
        total = sum(your_cards)
        print(f"New card: {new_card}, Your cards are now: {your_cards} and your total is: {total}")

        if total > 21:
            print("Bust! You lose.")
            return
        elif total == 21:
            print("Congratulations! Blackjack!")
            break

        draw_next = input("Do you want to draw another card? (y/n): ")

    # Dealer turn
    while dealer_total < 17:
        new_card = cards[random.randint(0, len(cards) - 1)]
        dealer_cards.append(new_card)
        dealer_total = sum(dealer_cards)
        
    print(f"Dealer's cards are: {dealer_cards} and their total is: {dealer_total}")

    if dealer_total > 21:
        print("Dealer busts! You win!")
    elif dealer_total > total:
        print("Dealer wins!")
    elif dealer_total == total:
        print("It's a tie!")
    else: 
        print("You win!")

    restart = input("Would you like to restart the game? (y/n): ")
    if restart == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        deal_cards()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for playing the game.")

deal_cards()

