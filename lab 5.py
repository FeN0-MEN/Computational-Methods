w, l, r = map(int, input().split())
FirstCnt = 1
SecondCnt = 1

FirstPart = list(map(int, input().split()))
SumForFirstPart = 0
SecontPart = list(map(int, input().split()))
SumForSecondPart = w

str = w - (max(sum(FirstPart), sum(SecontPart))-min(sum(FirstPart), sum(SecontPart)))

for i in FirstPart:
    if SumForFirstPart + i > str:
        SumForFirstPart = 0
        FirstCnt += 1
    else:
        SumForFirstPart += i
for i in SecontPart:
    if SumForSecondPart - i < str:
        SumForSecondPart = w
        SecondCnt += 1
    else:
        SumForSecondPart -= i

print(max(FirstCnt, SecondCnt))