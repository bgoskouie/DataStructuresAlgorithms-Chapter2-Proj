# Problem Statement:
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by str representing their ids.


# Solution explanation:
`is_user_in_group` is the entry point function that calls the recurring function `recur`. The function scans through all the groups and their users and looks for the `user` under question to see if it can be found in any of the users of any of the groups.
If there are `m` groups, `n` users each time complexity is `O(m * n)` or if `m == n` then time complexity is `O(n ** 2)`.

# Time and Space Analyses:
- Overall
    - SPACE:  `2 * n * 10`   (assuming each string would take 10 chars = 10 bytes)
    - TIME:     is_user_in_group:   `O(n**2)` or `O(m * n)`

- DETAILS:
    - Group:
        - SPACE:  1 string, 2 lists;
        - TIME:   `O(1)`
    - is_user_in_group:
        - SPACE:  `(m + n) * sizeof(string)`
        - TIME:   `O(m * n)`    m users, n groups
