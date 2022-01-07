def bubble_sort(sortable):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(sortable)-1):
            if sortable[i] < sortable[i+1]:
                temp = sortable[i]
                sortable[i] = sortable[i+1]
                sortable[i+1] = temp
                swapped = True

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]



bubble_sort(scores)
print(scores)
