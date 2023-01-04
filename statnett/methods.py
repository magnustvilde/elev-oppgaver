import collections.abc as abc

# Dette er en metode som skal retunere "fizz" hvis inputten kan deles på 3, "buzz" hvis inputten kan deles på 5
# og "fizzbuzz" hvis inputten kan deles på både 5 og 3. Fungerer metoden slik den skal? Hvis ikke, hva kan være feil?
def fizzbuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"


# Dette er en metode som tar inn en array som en parameter og utfører selection sort på arrayen. Deretter
# vil deretter retuneres. Funker metoden slik den skal? Hvis ikke, hva kan være feil?
def selection_sort(array):
    if not isinstance(array, abc.Iterable):
        raise (TypeError("Typen kan ikke itereres"))

    for i in range(len(array)):
        s = i

        for j in range(i + 1, len(array)):
            if array[j] < array[s]:
                s = j

        if i != s:
            array[s], array[i] = array[i], array[s]

    return array


if __name__ == "__main__":
    print(selection_sort([3, 8, 4, 12, 1]))
