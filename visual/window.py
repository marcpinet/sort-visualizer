import pygame
from random import shuffle

# Massive imports
import visual.colors as vc
import algorithms.bubble_sort as bubble_sort
import algorithms.selection_sort as selection_sort
import algorithms.insertion_sort as insertion_sort
import algorithms.merge_sort as merge_sort
import algorithms.heap_sort as heap_sort
import algorithms.quick_sort as quick_sort


class Window:
    WIDTH = 800
    HEIGHT = 600
    FPS = 1

    def __init__(self, array: list[int], algorithm: str):

        Window.FPS *= len(array)

        self.clock = pygame.time.Clock()
        self.running = False

        self.array = array
        self.algorithm = algorithm
        self.sorted = False

        pygame.init()
        self.screen = Window.SCREEN = pygame.display.set_mode(
            (Window.WIDTH, Window.HEIGHT)
        )
        self.screen.fill(vc.Color.BLACK)
        pygame.display.set_caption("Sorting Visualizer : " + algorithm)

    def _refresh_background(self) -> None:
        self.screen.fill(vc.Color.BLACK)

    def _refresh_all(self) -> None:
        pygame.event.pump()  # I still don't know why, but removing this line of code makes the program crash at the middle of the animation (lol)
        pygame.display.update()
        pygame.display.flip()
        self._refresh_background()
        self.clock.tick(Window.FPS)

    def _draw_rods(self, important_rods: list[int] = []) -> None:
        rod_width = (Window.WIDTH - 100) / len(self.array)
        rod_height = (Window.HEIGHT - 100) / max(self.array) - 1

        center_x_start = Window.WIDTH / 2 - (len(self.array) * (rod_width + 1)) / 2

        x_coord = center_x_start
        for k in self.array:
            if k in important_rods:
                pygame.draw.rect(
                    self.screen,
                    vc.Color.RED,
                    (
                        x_coord,
                        Window.HEIGHT - 100 - k * rod_height,
                        rod_width,
                        k * rod_height,
                    ),
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    vc.Color.WHITE,
                    (
                        x_coord,
                        Window.HEIGHT - 100 - k * rod_height,
                        rod_width,
                        k * rod_height,
                    ),
                )
            x_coord += rod_width + 1

    def _draw_some_rods(
        self, array: list[int], important_rods: list[int] = [], do_others: bool = False
    ) -> None:
        rod_width = (Window.WIDTH - 100) / len(self.array)
        rod_height = (Window.HEIGHT - 100) / max(self.array) - 1

        center_x_start = Window.WIDTH / 2 - (len(self.array) * (rod_width + 1)) / 2

        x_coord = center_x_start
        for k in self.array:
            if k in array:
                pygame.draw.rect(
                    self.screen,
                    vc.Color.GREEN,
                    (
                        x_coord,
                        Window.HEIGHT - 100 - k * rod_height,
                        rod_width,
                        k * rod_height,
                    ),
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    vc.Color.WHITE,
                    (
                        x_coord,
                        Window.HEIGHT - 100 - k * rod_height,
                        rod_width,
                        k * rod_height,
                    ),
                )
            x_coord += rod_width + 1

    def sorted_animation(self) -> None:
        """Little animation that plays at the end of a sorting animation"""
        tmp = []
        for k in self.array:
            tmp.append(k)
            self._draw_some_rods(tmp, do_others=True)
            self._refresh_all()

    def show_total_time(self, total_time: int) -> None:
        print(
            vc.CMDColors.BLUE
            + "Total time: "
            + str(total_time)
            + "ms"
            + vc.CMDColors.RESET
        )

    def start(self):
        if self.running:
            raise RuntimeError("Window is already running")
        else:
            self.running = True
            while self.running:

                # Tick
                self.clock.tick(Window.FPS)

                # Handling events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if not self.sorted:
                                print("\nSorting...")

                                # Sort the array
                                total_time = 0
                                for step, important_rods, time in ArrayTool.sort(
                                    self.algorithm, self.array
                                ):
                                    if (
                                        step is not None
                                        and len(step) > 0
                                        and not (len(step) == 1 and step[0] != -1)
                                    ):
                                        self.array = [s for s in step if s != -1]
                                    else:
                                        continue
                                    total_time = time

                                    # In a case where the yielded array is not the same length as the original array (e.g Merge Sort)

                                    # Refreshing EVERYTHING
                                    self._draw_rods(important_rods)
                                    self._refresh_all()

                                self.sorted_animation()
                                print(
                                    vc.CMDColors.GREEN + "Sorted!" + vc.CMDColors.RESET
                                )
                                self.sorted = True
                                self.show_total_time(total_time)

                            # Resetting the array
                            elif self.sorted:
                                shuffle(self.array)
                                self.sorted = False

                # Refreshing EVERYTHING
                self._draw_rods()
                self._refresh_all()


class ArrayTool:
    @staticmethod
    def sort(algorithm: str, array: list[int]):
        steps = None

        if algorithm == "Bubble Sort":
            steps = bubble_sort.sort(array)
        elif algorithm == "Selection Sort":
            steps = selection_sort.sort(array)
        elif algorithm == "Insertion Sort":
            steps = insertion_sort.sort(array)
        elif algorithm == "Merge Sort":
            steps = merge_sort.sort(array)
        elif algorithm == "Quick Sort":
            steps = quick_sort.sort(array)
        elif algorithm == "Heap Sort":
            steps = heap_sort.sort(array)

        return steps