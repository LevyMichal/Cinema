from DAL.membersWS import MembersWS


class Members:
    def __init__(self):
        self.__membersWS = MembersWS()
        print(self.__membersWS)

    def get_all_members(self):
        members = self.__membersWS.get_members()
        filtered_members = []
        for m in members:
            name = m["name"]
            email = m["email"]
            city = m["address"]["city"]
            member = {"name": name, "email": email, "city": city}

            filtered_members.append(member)

        print(filtered_members)
        return filtered_members
