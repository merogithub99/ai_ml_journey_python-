import random


def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your balance"))
            if balance <= 0:
                print("enter more than 0")
            else:
                return balance
        except ValueError:
            print("Please enter a valid number")


def get_bet_amount(balance):
    while True:
        try:
            bet = int(input("enter you bet amount: Rs."))
            if bet <= 0 or bet > balance:
                print(f"invalid bet.Enter a value between  rs.1 and rs. {balance}")
            else:
                return bet
        except ValueError:
            print("Please enter a valid number. ")


def spin_reels():
    symbols = ["🔔", "🍎", "⭐", "🍉", "🍒"]
    return [random.choice(symbols) for _ in range(3)]


def display_reels(reels):
    print(f"{reels[0]} | {reels[1]} | {reels[2]} ")


def calculate_payout(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        return bet * 10
    elif (
        reels[0] == reels[1]
        or reels[1] == reels[2]
        or reels[2] == reels[1]
        or reels[0] == reels[2]
    ):
        return bet * 5
    else:
        return 0


def main():
    print("🖥️ welcome to the slot machine game ")
    balance = get_starting_balance()
    print(f"you start with a balance of rs. {balance}")
    while balance > 0:
        print(f"current balance rs.{ balance}")
        bet = get_bet_amount(1000)
        reels = spin_reels()
        display_reels(reels)
        payout = calculate_payout(reels, bet)

        if payout > 0:
            print(f"You won rs. {payout}")
        else:
            print("sorry you lost")

        balance += payout - bet

        if balance <= 0:
            print(" you are out of money ! game over ")
            break

        play_again = input("play again? (y/n)").lower()
        if play_again != "y":
            print(f"you walk away with rs.{balance}")
            break


if __name__ == "__main__":
    main()
