# 회원 삭제
def deleteMember(id):
    member = readMemberId(id)
    if member:
        members.remove(member)
        print(f"'{id}' 삭제")
    else:
        print(f"'{id}' 삭제 x")