def partition(arr, left, right, rang):
    # poslednji element postaje pivot
    pivot = arr[right]
    # varijabla čuva indeks poslednjeg elementa manjeg od pivota
    i = left - 1
    for j in range(left, right):
        if rang[arr[j]] > rang[pivot]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr, left, right, rang):
    if left < right:
        pivot = partition(arr, left, right, rang)
        quick_sort(arr, left, pivot - 1, rang)
        quick_sort(arr, pivot + 1, right, rang)


# funkcija izracunava rang jedne stranice
def izracunaj_rang(graph, vert, ponavljanja, arr):
    (inc, outg) = graph.get_in_out(vert)
    suma = 0
    for o in inc:
        if not arr.check_element(str(o)):
            suma += ponavljanja[str(o)]
    # mozda ispraviti
    return 1 * ponavljanja[str(vert)] + 0.9 * graph.count_of_incoming(vert) + 0.8 * suma


# funkcija izracunava rang svih stranica koje su rezultat pretrage
def rang_svih(ponavljanja, vertices, graph, arr):
    rang = {}
    for a in arr:
        rang[a] = izracunaj_rang(graph, vertices[a], ponavljanja, arr)
    return rang
