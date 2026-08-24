def check(question, valid):
    while True:
        answer = input(question).lower().strip()
        for item in valid:
            if answer == item or answer == item[0]:
                return item
        print(f"Please enter one of: {valid}")


def repeat(task):
    while True:
        task()
        if check("Go again? ", ["yes", "no"]) == "no":
            print("Goodbye!")
            break


def demo():
    user = input("What's your name? ").strip()
    print(f"Hello, {user}! Task complete!")


if __name__ == "__main__":
    repeat(demo)