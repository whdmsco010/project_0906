from read import readMembers
from read import readMemberId



if __name__ == "__main__":
    try:
        # 사용자로부터 회원 ID 입력받기
        user_input = int(input("조회할 회원의 ID를 입력하세요: "))
        # 입력받은 ID로 회원 정보 조회
        read_member_by_id(user_input)
    except ValueError:
        print("올바른 숫자를 입력하세요.")
    readMembers()