def substrings(s: str):
    n = len(s)

    res = []
    for l in range(1, n + 1):
        for i in range(n - l):
            res.append(s[i: i + l])
    return res

if __name__ == "__main__":
    res = substrings("abcd")
    print(res)