import wordgame

if __name__ == '__main__':
    t = int(input())    # test case 입력
    for i in range(t):  # test case 만큼 반복
        words = []      # 입력 받을 문자열 list 초기화
        n = int(input())    # 문자열 개수 입력
        for j in range(n):
            words.append(input())   # 입력 받은 문자열 리스트에 추가
        game = wordgame.Game(n, words)  # Game Class 초기화
        game.play()     # 끝말잇기 가능 여부 판단
        game.result()   # 결과 출력






