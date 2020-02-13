def partition(arr, left, right, graph, vertices):
    # poslednji element postaje pivot
    pivot = arr[right]
    # varijabla čuva indeks poslednjeg elementa manjeg od pivota
    i = left - 1

    for j in range(left, right):
        if graph.count_of_incoming(vertices[arr[j]]) > graph.count_of_incoming(vertices[pivot]):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr, left, right, graph, vertices):
    if left < right:
        pivot = partition(arr, left, right, graph, vertices)
        quick_sort(arr, left, pivot - 1, graph, vertices)
        quick_sort(arr, pivot + 1, right, graph, vertices)
