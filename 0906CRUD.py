from read import readMember, readMemberId
from updatemember import updateMember
from deletemember import deleteMember


def menu_selection():
    print("(C)reate, (R)ead, (U)pdate, (D)elete")
    menu = input("메뉴 입력: ").upper() 

    if menu == "C":
        print()
        # Create 관련 로직 추가
    elif menu == "R":
         print("(A)ll, (S)elect")
         choice = input("선택: ").upper() 

         if choice == "A":
            readMember()
         elif choice == "S":
            try:
                member_id = int(input("조회할 회원의 ID를 입력하세요: "))
                readMemberId(member_id)
            except ValueError:
                print("올바른 숫자를 입력하세요.")
    elif menu == "U":
        try:
            id = int(input("수정할 회원의 ID를 입력하세요: "))
            name = input("수정할 이름 (변경하지 않으려면 Enter): ")
            birth = input("수정할 생일 (변경하지 않으려면 Enter): ")
            updateMember(id, name, birth)
        except ValueError:
            print("잘못된 입력입니다.")
    elif menu == "D":
        try:
            id = int(input("삭제할 회원의 ID를 입력하세요: "))
            deleteMember(id)
        except ValueError:
                print("잘못된 입력입니다.")
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")


if __name__ == "__main__":
    menu_selection()