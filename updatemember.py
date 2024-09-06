# 회원 수정
def updateMember(id, name=None, birth=None):
    member = readMemberId(id)
    if member:
        if name:
            member['name'] = name
        if birth:
            member['birth'] = birth
        print(f"'{id}' 수정")
    else:
        print(f"'{id}' 수정 x")