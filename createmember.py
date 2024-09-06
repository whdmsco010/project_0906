members = []

def addMember(name, birth):
    id = len(members) + 1  
    member = {
        'id': id,
        'name': name,
        'birth': birth,
    }
    members.append(member)
    #print(f"Member added: {member}")