
class Game:

    def __init__(self, players, words):
        self.players = players
        self.words = words
        self.word_list = list()
    '''
    게임 진행 함수
    '''
    def play(self):
        for i in range(self.players):   # 입력된 모든 단어들을 첫 단어로 설정해보기 위한 반복문
            self.word_list.clear()  # 새로 검색하기 위해 기존의 리스트를 비우기
            self.word_list.append(self.words[i])    # 입력된 단어들 중 i 번째 인덱스의 단어를 끝말잇기의 첫 단어로 설정
            valid_count = 1     # valid_count : 끝말 잇기 성공한 단어 수를 체크할 변수
            for j in range(self.players):   # 모든 단어의 개수만큼 검사하기 위한 반복문
                for k in range(1, self.players):    # 남아 있는 단어들 중 끝말잇기가 가능한 단어가 있는지 확인하는 반복문
                    check_idx = (i + k) % self.players  # i 번째 기준으로 다음 단어들을 검색(i가 0이 아닐 경우 단어들 끝에서 처음 단어로 돌아감)
                    last_word = self.word_list[len(self.word_list) - 1] # last_word : 끝말을 이어야 할 단어
                    # 끝말잇기 가능한 단어인지 검사
                    if last_word[len(last_word) - 1] is self.words[check_idx][0]\
                            and self.words[check_idx] not in self.word_list:    # 단어 중복 검사
                        self.word_list.append(self.words[check_idx])
                        valid_count += 1
                        if valid_count == self.players:     # 끝말잇기가 완성된 경우 종료
                            return None
        self.word_list = ['IMPOSSIBLE']     # 검색 실패시 IMPOSSIBLE
        return None
    '''
    결과를 출력해주는 함수
    '''
    def result(self):
        for i in range(len(self.word_list)):
            print(self.word_list[i], end=' ')
        print()




