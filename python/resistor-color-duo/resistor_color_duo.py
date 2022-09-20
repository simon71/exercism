
stripes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    result=""
    for i in range(2):
        result+=str(stripes.index(colors[i]))

    return int(result)
