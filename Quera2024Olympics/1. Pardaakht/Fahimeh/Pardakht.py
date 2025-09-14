output = list()
words = list()
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        words.append(input())
    elements = "".join(words)
    res = "".join([char for i, char in enumerate(elements) if char not in elements[:i]])
    output.append(0)
    for elem in res:
        count = 0
        for word in words:
            count = max(count, word.count(elem))
        output[-1] += count
    words.clear()
for k in output:
    print(k)
