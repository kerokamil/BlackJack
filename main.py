import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def hand_cards(cards):
    """Calculates the hand total, adjusting for aces"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0  # blackjack
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def casino_deal(casino_card):
    """Casino draws until its total is 17 or higher"""
    while hand_cards(casino_card) < 17:
        casino_card.append(deal_card())
    return casino_card


def print_cards(client, casino):
    """Prints the first hand’s cards of the client and casino’s visible card"""
    print(f"The casino's visible card is {casino[-1]}")
    print(f"Your cards are {client[0]} and {client[1]}")


def check_black_jack(client, casino):
    """Checks for blackjack and declares the winner"""
    print_cards(client, casino)
    client_score = hand_cards(client)
    casino_score = hand_cards(casino)

    if client_score == 0 and casino_score == 0:
        print("Both you and casino have Blackjacks! It's a draw.")
        return True
    if client_score == 0:
        print("You have Blackjack! ?? You win!")
        return True
    if casino_score == 0:
        print("Casino has Blackjack! ?? You lose.")
        return True
    return False


def check_result(client, casino):
    """Compares the final hands and decides the winner"""
    client_score = hand_cards(client)
    casino_score = hand_cards(casino)

    print("\n--- Final Results ---")

    print("Casino cards:", ", ".join(map(str, casino)))
    print(f"Casino final score: {casino_score}")
    print("Your cards:", ", ".join(map(str, client)))
    print(f"Your final score: {client_score}")

    if client_score > 21:
        print("You went over 21 — you lose ??")
    elif casino_score > 21:
        print("Casino went over 21 — you win! ??")
    elif client_score > casino_score:
        print("You win! ??")
    elif client_score < casino_score:
        print("You lose ??")
    else:
        print("It's a draw ??")


# --- Game Sequence ---
while True:
    client_card = [deal_card(), deal_card()]
    casino_card = [deal_card(), deal_card()]

    # Check for blackjack immediately

    if check_black_jack(client_card, casino_card):
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing, hope to see you again!")
            break
        else:
            continue

    # Player's turn
    while True:

        user_input = input("\nWould you like me to deal your cards? (y/n)? ").lower()

        if user_input == 'y':
            new_card = deal_card()
            print(f"Your new card is {new_card}")
            client_card.append(new_card)
            score = hand_cards(client_card)
            print(f"Your new score is {score}")

            if score > 21:
                print("YOUR SCORE IS OVER 21, YOU LOST :(")
                break


        elif user_input == 'n':
            casino_deal(casino_card)
            check_result(client_card, casino_card)
            break

        else:
            print("Invalid input. Please input y or n.")

    # Replay?
    game_input = input("\nDo you want to play again? (y/n)? ").lower()
    if game_input == 'y':
        continue

    elif game_input == 'n':
        print("Thank you for playing, hope to see you again!")
        break
    else:
        print("Invalid input. Please input y or n.")
