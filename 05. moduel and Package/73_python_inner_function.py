# python 은 builtins 함수는 기본 내장되어 있음.
import builtins

builtins.print('abc')

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}
print(ranking)
for key in ranking:
    print(key)

# 점수 순으로 랭킹을 보고 싶을때 [오름 차순임]
print(sorted(ranking, key=ranking.get))

# 내림 차순으로 보고 싶다면.
print(sorted(ranking, key=ranking.get, reverse=True))