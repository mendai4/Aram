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

print("Naive String Match:", naive_string_match(text, pattern))


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
