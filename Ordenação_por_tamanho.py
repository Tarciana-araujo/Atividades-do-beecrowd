frases = [input().split() for _ in range(int(input()))]
for i in range(len(frases)):
    frases[i].sort(key=len , reverse=True)

for frases in frases:
    print(' '.join(frases))
