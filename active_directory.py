""" Windows Active Directory """


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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user: str, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        raise ValueError('group should not be None')
    if user is None or user == '':
        raise ValueError('user should not be None or empty')

    if user in group.get_users():
        return True

    return any([is_user_in_group(user, g) for g in group.get_groups()])

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1


def test1():
    print(is_user_in_group('123', parent))


# Test Case 2
def test2():
    print(is_user_in_group('sub_child_user', parent))


# Test Case 3
def test3():
    try:
        _ = is_user_in_group('', parent)
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    test1()
    test2()
    test3()
