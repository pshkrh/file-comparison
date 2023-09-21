"""This module contains the LCS algorithm logic for comparing two strings."""


class Change:
    def __init__(self, data, change_type):
        self.data = data
        self.change_type = change_type  # Represents the type of change


def _compute_lcs(text1, text2):
    n = len(text1)
    m = len(text2)

    lcs = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs


def compare_text(text1, text2):
    lcs = _compute_lcs(text1, text2)

    results = []

    i = len(text1)
    j = len(text2)

    while i != 0 or j != 0:
        if i == 0:
            results.append(Change(text2[j - 1], "add"))
            j -= 1
        elif j == 0:
            results.append(Change(text1[i - 1], "remove"))
            i -= 1
        elif text1[i - 1] == text2[j - 1]:
            results.append(Change(text1[i - 1], "no-change"))
            i -= 1
            j -= 1
        elif lcs[i - 1][j] <= lcs[i][j - 1]:
            results.append(Change(text2[j - 1], "add"))
            j -= 1
        else:
            results.append(Change(text1[i - 1], "remove"))
            i -= 1

    return list(reversed(results))
