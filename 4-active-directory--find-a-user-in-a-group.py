# Active Directory
# In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
# We can construct this hierarchy as such. Where User is represented by str representing their ids.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    def recur(user, group):
        if user in group.get_users():
            return True
        for g in group.get_groups():
            return recur(user, g)
        return False

    return recur(user, group)


if __name__ == "__main__":
    print("--------------------Starting Test 1--------------------")
    parent1 = Group("parent")
    child1 = Group("child")
    sub_child1 = Group("subchild")

    sub_child_user1 = "sub_child_user"
    sub_child1.add_user(sub_child_user1)

    child1.add_group(sub_child1)
    parent1.add_group(child1)
    result1 = is_user_in_group("sub_child_user", parent1)   # should return True
    print(result1)

    print("--------------------Starting Test 2--------------------")
    parent2 = Group("parent")
    child2 = Group("child")
    sub_child2 = Group("subchild")

    sub_child_user2 = ""   # user is empty!
    sub_child2.add_user(sub_child_user2)

    child2.add_group(sub_child2)
    parent2.add_group(child2)
    result2 = is_user_in_group("sub_child_user", parent2)  # should return False
    print(result2)

    print("--------------------Starting Test 3--------------------")
    parent3 = Group("parent")
    result3 = is_user_in_group("sub_child_user", parent3)  # should return False
    print(result3)