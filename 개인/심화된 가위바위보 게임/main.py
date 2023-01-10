from game import *
import random

def main():
    # 라운드 시작 1 라운드부터
    round_count = 1
    # 유저, 컴퓨터 시작 체력 0
    user_score = 0
    com_score = 0

    while True:
        try:
            round = int(input('라운드를 입력해주세요 >>> '))
            break
        except ValueError:
            print('숫자를 입력해주세요.')

    for i in range(round):    # 입력한 라운드 횟수 만큼 반복
        print(f'< {round_count}번째 Round >')
        com = sel[random.randint(0, 2)]  # 컴퓨터가 sel 리스트 안의 가위,바위,보 값을 랜덤으로 받는다.
        user = input("안 내면 진다~! 가위, 바위, 보!!  >>>  ")  # 사용자로부터 입력을 받는다.
        while True:
            if user in sel:     # 만약 user가 입력한 값이 sel 리스트 안에 있을 때
                break
            else:
                print('가위, 바위, 보 중 입력해주세요.')
                user = input("안 내면 진다~! 가위, 바위, 보!!  >>>  ")

        check, ret = checkWin(user, com)  # 잘못된 값인지와 결과값을 가져온다.
        if check == True:
            if ret == 1:  # 결과 값에 따라 점수를 누적한다.
                com_score += 1
            if ret == 0:
                user_score += 1
            print(f"ㅡ 유저 Score : {user_score}, 컴퓨터 Score : {com_score} ㅡ")
            round_count += 1  # 라운드를 1씩 증가시킨다.

    score(user_score, com_score)
    restart()  # 다시 게임 시작할 구문