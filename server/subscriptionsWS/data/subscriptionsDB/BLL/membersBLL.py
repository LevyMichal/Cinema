from DAL.membersDAL import MembersDAL


class MembersBLL:
    def __init__(self):
        self.__members = MembersDAL()

    # get all members
    def get_all_members(self):
        members = list(self.__members.get_all_members())
        return members
