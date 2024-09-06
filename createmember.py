members = []

def addMember(name, birth):
    id = len(members) + 1  
    member = {
        'id': id,
        'name': name,
        'birth': birth,
    }
    members.append(member)
    print(f"Member added: {member}")

addMember("조은채","010717")
addMember("유서영","011014")
addMember("이태훈","981231")