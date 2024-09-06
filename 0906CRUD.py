from read import readMember, readMemberId
from createmember import addMember

def menu_selection():
    while True: 
        print("(C)reate, (R)ead, (U)pdate, (D)elete, (Q)uit")  
        menu = input("메뉴 입력: ").upper()

        if menu == "C":
            addMember("조은채", "2001-07-17")
            addMember("유서영", "2001-10-14")
            addMember("이태훈", "1998-12-31")
            # Create 관련 로직 추가
        elif menu == "R":
            print("(A)ll, (S)elect")
            choice = input("선택: ").upper()

            if choice == "A":
                readMember()  # 전체 회원 조회
            elif choice == "S":
                try:
                    member_id = int(input("조회할 회원의 ID를 입력하세요: "))
                    readMemberId(member_id)  # 특정 ID로 회원 조회
                except ValueError:
                    print("올바른 숫자를 입력하세요.")
        elif menu == "U":
            print("Update 기능을 실행합니다.")
            # Update 관련 로직 추가
        elif menu == "D":
            print("Delete 기능을 실행합니다.")
            # Delete 관련 로직 추가
        elif menu == "Q":  # 사용자가 'Q'를 입력하면 프로그램 종료
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    menu_selection()
