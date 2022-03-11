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


def generate_array(size: int) -> list[int]:
    """Generate a randomized array with a provided size

    Args:
        size (int): The size of the array to generate

    Returns:
        list[int]: The generated array (with randomized order)
    """
    a = [i for i in range(1, size + 1)]
    shuffle(a)
    return a


def main():

    # Initializing variables
    choice = None
    size = None
    
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
    while size not in range(2, 101):
        size = ask_for_int(
            vc.CMDColors.RESET
            + "Input the size [2 ; 100] of the array to generate and sort: "
            + vc.CMDColors.YELLOW
        )

    array = generate_array(size)

    animation = vw.Window(array, algorithms[choice])
    animation.start()

if __name__ == "__main__":
    main()
