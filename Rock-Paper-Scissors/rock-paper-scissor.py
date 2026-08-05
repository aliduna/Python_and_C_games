import random

WIN_SCORE = 3
CHOICES = ["rock", "paper", "scissors"]


def determine_winner(player, computer):
    if player == computer:
        return "draw"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


def main():
    print("🎮 Welcome to Rock Paper Scissors!")

    player_score = 0
    computer_score = 0

    while True:
        player = input(
            "\nYour choice (rock / paper / scissors)\n"
            "'sc' = Score\n"
            "'q' = Quit\n"
            "> "
        ).lower()

        if player == "q":
            print("\nGame ended.")
            break

        if player == "sc":
            print(f"\nYou: {player_score}")
            print(f"Computer: {computer_score}")
            continue

        if player not in CHOICES:
            print("❌ Invalid choice! Please try again.")
            continue

        computer = random.choice(CHOICES)

        print(f"\nComputer: {computer}")

        result = determine_winner(player, computer)

        if result == "draw":
            print("🤝 It's a draw!")
        elif result == "player":
            player_score += 1
            print("✅ You won! +1 Point")
        else:
            computer_score += 1
            print("❌ The computer won!")

        print(f"Score → You: {player_score} | Computer: {computer_score}")

        if player_score == WIN_SCORE:
            print("\n🏆 Congratulations! You won the game!")
            break

        if computer_score == WIN_SCORE:
            print("\n💀 The computer won the game.")
            break


if __name__ == "__main__":
    main()