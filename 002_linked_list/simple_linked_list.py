# 단순 연결 리스트 클래스
class SimpleLinkedList():
    # 노드 클래스
    class Node():
        def __init__(self, item, next_node):
            self.item = item
            self.next_node = next_node
    
    # 리스트 초기화
    def __init__(self):
        self.head = None # data type : Node
        self.size_num = 0

    # 리스트 크기 확인
    def size(self):
        print(self.size_num)
    
    # 리스트 empty 여부 확인
    def is_empty(self):
        return True if self.size_num == 0 else False

    # 리스트 요소 맨 앞에 추가
    # 단순 연결 리스트는 요소 추가를 맨 앞에 하는 것이 효율적이다.
    def add_first(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else: # 맨 앞 추가이므로, 다음 노드는 현재의 head가 됨
            self.head = self.Node(item, self.head)
        print('what is next', self.head.item)
        self.size_num += 1

    # 리스트 요소 중간 삽입
    def insert_next(self, item, node):
        node.next_node = SimpleLinkedList.Node(item, node.next_node)
        self.size_num += 1

    # 리스트 맨 앞 요소 삭제
    def remove_first(self):
        if self.is_empty():
            return 'isEmpty'
        else:
            self.head = self.head.next_node
        self.size_num -= 1

    # 리스트 중간 요소 삭제
    def remove_next(self, node):
        if self.is_empty():
            return 'isEmpty'
        else:
            temp = node.next_node
            node.next_node = temp.next_node
        self.size_num -= 1

    # 리스트 요소 인덱스 검색
    def get_index(self, item):
        temp = self.head
        for i in range(self.size_num):
            if item == temp.item:
                print(i)
                break
            temp = temp.next_node
        else:
            print('There is no element you want to get')


    # 리스트 전체 출력
    def all_list(self):
        temp = self.head
        while temp:
            print(temp.item, end=' ')
            temp = temp.next_node
        print()

# 리스트 생성
sll = SimpleLinkedList()

# 데이터 추가
sll.add_first('hi')
sll.add_first('my')
sll.add_first('friend')
sll.insert_next('my1', sll.head.next_node)

# 데이터 삭제
sll.remove_first()
sll.all_list()
sll.remove_next(sll.head.next_node)

# 데이터 검색
sll.get_index('my1')
sll.get_index('your')
sll.all_list()
sll.size()