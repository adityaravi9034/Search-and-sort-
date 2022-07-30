# import all the modules
from matplotlib import pyplot as plt, animation
import random


def quickSort(alist):
    first = 0
    last = len(alist) - 1
    yield from quickSort_(alist, first, last)


def quickSort_(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        yield alist
        yield from quickSort_(alist, first, splitpoint - 1)
        yield alist
        yield from quickSort_(alist, splitpoint + 1, last)
        yield alist


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# visualization method
def visualize(generator, text):
    # creates a figure and subsequent subplots
    fig, ax = plt.subplots()
    ax.set_title(text)
    bar_sub = ax.bar(range(len(A)), A, align="edge")

    # sets the maximum limit for the x-axis
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    # update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    # creating animation object for rendering the iteration
    anim = animation.FuncAnimation(fig,
                                   func=update,
                                   fargs=(bar_sub, iteration),
                                   frames=generator,
                                   repeat=False,
                                   blit=False,
                                   interval=100,
                                   )

    # for showing the animation on screen
    plt.show()
    plt.close()


if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    # test quick sort
    generator = quickSort(A)
    visualize(generator, "Quick Sort O(nlogn)")
    print(A)
