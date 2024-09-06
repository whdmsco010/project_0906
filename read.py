from createmember import members  

# 전체 회원 조회
def readMember():
    print("회원 목록:")
    if not members:
        print("회원이 없습니다.")
    else:
        for member in members:
            print(f"ID: {member['id']}, Name: {member['name']}, Birth: {member['birth']}")

# 선택 회원 조회
def readMemberId(member_id):
    for member in members:
        if member['id'] == member_id:
            print(f"ID: {member['id']}, Name: {member['name']}, Birth: {member['birth']}")
            return
    print(f"회원 ID {member_id}를 찾을 수 없습니다.")
