#Linear Search
#미정렬된 리스트에 대해 사용할 수 있는 탐색 방법
ls = [4,2,7,1,9,10,5,8,15,23]
def linear_Search(lst,key):
    for index,item in enumerate(lst):
        if item == key:
            return index

print(linear_Search(ls,5))

#배운 것 : Python에서 index, key를 동시에 접근하기 위해 enumerate를 사용할 수 있다.