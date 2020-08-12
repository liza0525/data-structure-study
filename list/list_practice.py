# 자료구조 선언
a = list()
b = [1, 2, 3, 4, 5]

# 데이터의 추가
a.append('hi')
b.append(6)
b.append('seven') # 파이썬의 리스트는 데이터의 자료형에 통일성이 없어도 된다.

# 데이터 검색
print(a[0])
print(b[1])
print(b[-1]) # 파이썬의 리스트에서 음수 인덱스는, 맨 뒤에서부터 검색한다는 것을 의미한다.

# 데이터의 삭제
a.remove('hi')
b.remove(6)