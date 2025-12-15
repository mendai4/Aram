#1. Վերջավոր ավտոմատներ
def dfa_accepts(sample: str) -> bool:
    state = 0
    for ch in sample:
        if state == 0:
            state = 1 if ch == '0' else 0
        elif state == 1:
            state = 1 if ch == '0' else 2
        else:
            state = 1 if ch == '0' else 0
    return state == 2

test = ["01", "101", "001", "111", "010", ""]
for sample in test:
    print(sample, "=>", dfa_accepts(sample))