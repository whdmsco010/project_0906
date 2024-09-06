from createmember import members  
from read import readMemberId  

def deleteMember(id):
    member = readMemberId(id)
    if member:
        members.remove(member) 
        print(f"회원 '{id}' 삭제 완료")
    else:
        print(f"회원 '{id}'를 찾을 수 없습니다. 삭제할 수 없습니다.")
