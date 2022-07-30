# MERGE SORT

from matplotlib import pyplot as plt, animation
import random


# function to recursively divide the array
def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        yield from mergeSort(lefthalf)
        yield from mergeSort(righthalf)
        yield from merge(alist, lefthalf, righthalf)


# function to merge the array
def merge(alist, lefthalf, righthalf):
    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            alist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1
        # yield alist

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1
    # print("Merging ",alist)

    yield alist


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

    # test merge sort
    generator = mergeSort(A)
    visualize(generator, "Merge Sort O(nlogn)")
