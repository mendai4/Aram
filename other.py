text = "chxklpndxklpndz"
pattern = "klpn"

def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    results = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            results.append(i)
    return results

asd = ", ".join([str(i) for i in naive_string_match(text, pattern)])
print(f"Matches found on index-es {asd}")



A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]
def naive_matrix_mult(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0]*p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C
print("Naive Matrix Multiplication:", naive_matrix_mult(A,B))


def bad_char_table(pattern):
    table = {}
    for i, c in enumerate(pattern):
        table[c] = i
    return table

def boyer_moore(text, pattern):
    table = bad_char_table(pattern)
    n, m = len(text), len(pattern)
    results = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1
        if j < 0:
            results.append(i)
            i += 1
        else:
            i += max(1, j - table.get(text[i+j], -1))
    return results

print("Boyer-Moore Match:", boyer_moore(text, pattern))
