score = 0


def game():
    level = 1

    def level_up():
        nonlocal level
        level += 1
        print(f"Level: {level}")

    level_up()
    global score
    score += 77


game()

print(f"Score : {score}")
