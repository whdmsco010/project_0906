from createmember import addMember

members = [
    {"id": 1, "name": "Alice", "birth": "1990-01-01"},
    {"id": 2, "name": "Bob", "birth": "1985-05-12"},
    {"id": 3, "name": "Charlie", "birth": "1992-08-15"}
]

#전체 회원 조회
def readMember():
    print("회원 목록:")
    for member in members:
        print(f"ID: {member['id']}, Name: {member['name']}, Birth: {member['birth']}")

#선택 회원 조회
def readMemberId(member_id):
    for member in members:
        if member['id'] == member_id:
            print(f"ID: {member['id']}, Name: {member['name']}, Birth: {member['birth']}")
            return
    print(f"회원 ID {member_id}를 찾을 수 없습니다.")