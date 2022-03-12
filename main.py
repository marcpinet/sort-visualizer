import glob

from random import shuffle

import visual.colors as vc
import visual.window as vw


def ask_for_int(sentence: str) -> int:
    """
    Ask the user for an integer.
    """
    while True:
        try:
            return int(input(sentence))
        except ValueError:
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


def generate_array(size: int, reverse: bool = False) -> list[int]:
    """Generate a randomized array with a provided size

    Args:
        size (int): The size of the array to generate

    Returns:
        list[int]: The generated array (with randomized order)
    """
    a = [i for i in range(1, size + 1)]
    if reverse:
        a.reverse()
    else:
        shuffle(a)
    return a


def main():

    # Initializing variables
    choice = None
    size = None
    choice2 = None

    # Getting list of algorithms
    algorithms = get_algorithms()

    # Printing available choices
    for i in range(len(algorithms)):
        print(vc.CMDColors.YELLOW, i, ":", algorithms[i])

    print()

    # Getting the user's inputs
    while choice not in range(len(algorithms)):
        choice = ask_for_int(
            vc.CMDColors.RESET
            + "Input the n° of the algorithm you want to visualize: "
            + vc.CMDColors.YELLOW
        )

    # Getting the size of the array to generate and sort
    while size not in range(2, 701):
        size = ask_for_int(
            vc.CMDColors.RESET
            + "Input the size [2 ; 700] of the array to generate and sort: "
            + vc.CMDColors.YELLOW
        )

    print()

    # Printing available choices
    print(vc.CMDColors.YELLOW, "0 : Randomized")
    print(vc.CMDColors.YELLOW, "1 : Reversed")

    print()

    # Getting choice2
    while choice2 not in [0, 1]:
        choice2 = ask_for_int(
            vc.CMDColors.RESET
            + "Is array fully randomized or reversed? "
            + vc.CMDColors.YELLOW
        )

    array = generate_array(size, reverse=bool(choice2))

    # Instructions
    print(
        vc.CMDColors.CYAN
        + "Press "
        + vc.CMDColors.FAIL
        + "SPACE"
        + vc.CMDColors.CYAN
        + " to start sorting.\nPress "
        + vc.CMDColors.FAIL
        + "SPACE"
        + vc.CMDColors.CYAN
        + " again to shuffle it.\nPress "
        + vc.CMDColors.HEADER
        + "ESCAPE"
        + vc.CMDColors.CYAN
        + " in the terminal to exit."
        + vc.CMDColors.RESET
    )

    animation = vw.Window(array, algorithms[choice])
    animation.start()

    _ = input("\nPress ENTER to exit.\n")


if __name__ == "__main__":
    main()
