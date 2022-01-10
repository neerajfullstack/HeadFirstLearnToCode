def bubble_sort(sortable, numbers):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(sortable) - 1):
            if sortable[i] < sortable[i + 1]:
                temp = sortable[i]
                sortable[i] = sortable[i + 1]
                sortable[i + 1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                swapped = True


scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57,
          52, 44, 18, 41, 53, 55, 61, 51, 44]

number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))
bubble_sort(scores, solution_numbers)
print('Top bubble solutions:')
for i in range(0, 5):
    print(str(i + 1) + ')',
          'Bubble Solution #' + str(solution_numbers[i]),
          'score: ', scores[i])

# There are many sorting algorithms with various tradeoffs in complexity and space/time considerations

# Bubble sort is a simple algorithm that makes passes through list, comparing and swapping values as it goes.

# Bubble sort is complete when a pass through the list finds no items that are out of order.

# Most langs and libs provide sort functionality.

# When we have a loop within loop, we call it a nested loop

# Nested loops often increase the runtime and complexity of an algorithm

# You should study sorting algos provided by your lang and libs.
