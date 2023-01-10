import main

sel = ['가위', '바위', '보']
sel_images = ['scissors', 'rock', 'paper']  # 가위, 바위, 보 문자 그림
result = {0: '당신이 이겼습니다!', 1: '당신이 졌습니다.', 2: '비겼습니다.'}

def images_list(user=0, com=0):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    if user == '보' or com == '보':
        return paper
    elif user == '가위' or com == '가위':
        return scissors
    elif user == '바위' or com == '바위':
        return rock

def checkWin(user, com):
    #유저, 컴퓨터가 입력한 값과 문자 이미지를 출력
    print(images_list(user))
    print(f'사용자 : {user}')

    print(images_list(com))
    print(f'컴퓨터 : {com}')

    if user == com:
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(result[state])   # result 딕셔너리의 해당되는 번호 value 값을 출력
    return True, state

def restart():
    user = input("다시하시겠습니까? : <예 or 아니요> : ")
    if user == '예':       # 예를 입력 했을 때 다시 시작
        main.main()
    elif user == '아니요':  # 아니요를 입력 했을 때 종료
        print('게임을 종료합니다.')
    else:
        print("*** 예 또는 아니요를 입력하세요. ***")

def score(user_score, com_score):
    if user_score > com_score:           # 유저 score가 컴퓨터 score보다 클 때
        print('[최종 결과] >>> 유저 : 승리 , 컴퓨터 : 패배 <<<')
    elif user_score == com_score:        # 컴퓨터 score랑 유저 score와 같을 때
        print('[최종 결과] >>> 유저 : 무 , 컴퓨터 : 무 <<<')
    elif user_score < com_score:         # 컴퓨터 score가 유저 score보다 클 때
        print('[최종 결과] >>> 유저 : 패배 , 컴퓨터 : 승리 <<<')