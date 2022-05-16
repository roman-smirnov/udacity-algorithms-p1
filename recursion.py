""" Finding all files under a directory """""

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not suffix or not path:
        return []
    if not os.path.exists(path):
        return []
    file_paths = []
    for p in os.listdir(path):
        p = os.path.join(path, p)
        if os.path.isdir(p):
            file_paths.extend(find_files(suffix, p))
        elif os.path.isfile(p) and p.endswith(suffix):
            file_paths.append(p)
    return file_paths


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
for f in find_files('.py', '.'):
    print(f)

# Test Case 2
for f in find_files('.c', './testdir'):
    print(f)

# Test Case 3
print(find_files(None, '.'))
print(find_files('', None))
print(find_files('', ''))
print(find_files('', 'nonexistantpath'))
print(find_files('.nonexistantsuffix', '.'))
