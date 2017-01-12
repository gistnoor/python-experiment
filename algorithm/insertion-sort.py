# example 1
def sort_numbers(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val

def main():
    x = (eval(input("Enter numbers to be sorted: ")))
    x = list(x)
    sort_numbers(x)
    print(x)


# example 2
def insertion_sort(k):
    for i in range(1, len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]:
            k[j], k[j-1] = k[j-1], k[j]
            j = j-1
    return k
