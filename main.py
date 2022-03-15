import glob

from random import shuffle, randint

import visual.colors as vc
import visual.window as vw


def ask_for_int(sentence: str) -> int:
    """
    Ask the user for an integer.
    """
    while True:
        try:
            tmp = input(sentence)
            return int(tmp)
        except ValueError:
            if "exit" in tmp:
                exit(0)

            print(
                vc.CMDColors.FAIL + "Invalid input. Please try again.",
                vc.CMDColors.RESET,
            )


def get_algorithms() -> list[str]:
    """Returns a list of all available algorithms

    Returns:
        list[str]: Gathered algorithms from the folder
    """
    files = glob.glob("algorithms/*.py")
    return [
        file.split("\\")[-1].split(".")[0].replace("_", " ").title() for file in files
    ]


def generate_array(
    size: int, reverse: bool = False, few_unique: bool = False
) -> list[int]:
    """Generate a randomized array with a provided size

    Args:
        size (int): The size of the array to generate

    Returns:
        list[int]: The generated array (with randomized order)
    """
    a = [i for i in range(1, size + 1)]

    if reverse:
        a.reverse()
    elif few_unique:
        a = [randint(1, size) for _ in range(1, size + 1)]
        shuffle(a)
    else:
        shuffle(a)

    return a


def main():
    
    running = True
    while running:

        print(
            "\nType ",
            vc.CMDColors.UNDERLINE
            + vc.CMDColors.BOLD
            + "exit"
            + vc.CMDColors.RESET
            + " at any time to exit.\n",
        )

        # Initializing variables
        choice = None
        size = None
        choice2 = None

        # Getting list of algorithms
        algorithms = get_algorithms()

        # Printing available choices
        for i in range(len(algorithms)):
            if algorithms[i] == "Bitonic Sort":
                print(
                    vc.CMDColors.YELLOW,
                    i,
                    ":",
                    algorithms[i],
                    "(only if size of array is a power of 2)",
                )
            else:
                print(vc.CMDColors.YELLOW, i, ":", algorithms[i])

        print()

        # Getting the user's inputs
        while choice not in range(len(algorithms)):
            choice = ask_for_int(
                vc.CMDColors.RESET
                + "Input the n° of the algorithm you want to visualize\n> "
                + vc.CMDColors.YELLOW
            )

        # Getting the size of the array to generate and sort
        while size not in range(2, 901):
            size = ask_for_int(
                vc.CMDColors.RESET
                + "Input the size [2 ; 900] of the array to generate and sort\n> "
                + vc.CMDColors.YELLOW
            )

        print()

        # Printing available choices
        print(vc.CMDColors.YELLOW, "0 : Randomized")
        print(vc.CMDColors.YELLOW, "1 : Reversed")
        print(vc.CMDColors.YELLOW, "2 : Few Unique")

        print()

        # Getting choice2
        while choice2 not in [0, 1, 2]:
            choice2 = ask_for_int(
                vc.CMDColors.RESET
                + "Is array fully randomized or reversed?\n> "
                + vc.CMDColors.YELLOW
            )

        print()

        array = generate_array(
            size,
            reverse=True if choice2 == 1 else False,
            few_unique=True if choice2 == 2 else False,
        )

        # Instructions
        print(
            vc.CMDColors.CYAN
            + "Press "
            + vc.CMDColors.FAIL
            + "SPACE"
            + vc.CMDColors.CYAN
            + " to start sorting.\nPress "
            + vc.CMDColors.FAIL
            + "LEFT_ARROW"
            + vc.CMDColors.CYAN
            + " or "
            + vc.CMDColors.FAIL
            + "RIGHT_ARROW"
            + vc.CMDColors.CYAN
            + " to adjust the speed.\nPress "
            + vc.CMDColors.FAIL
            + "SPACE"
            + vc.CMDColors.CYAN
            + " again to shuffle it.\nPress "
            + vc.CMDColors.FAIL
            + "ESCAPE"
            + vc.CMDColors.CYAN
            + " to exit."
            + vc.CMDColors.RESET
        )

        animation = vw.Window(array, algorithms[choice])
        animation.start()
        del animation

    _ = input("\nPress ENTER to exit.\n")


if __name__ == "__main__":
    main()
