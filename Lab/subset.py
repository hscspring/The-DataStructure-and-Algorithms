subset = []
n = 3


def search(k):
    if k==n:
        print(subset)
        pass
    else:

        search(k+1)
        subset.append(k)

        search(k+1)
        x = subset.pop()
        print("x", x)
    


search(0)
