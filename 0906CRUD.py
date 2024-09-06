from read import readMember, readMemberId


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
        print()
        # Update 관련 로직 추가
    elif menu == "D":
        print()
        # Delete 관련 로직 추가
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")


if __name__ == "__main__":
    menu_selection()