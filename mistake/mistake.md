Operator priority causes fd to be assigned to 0, which is stdin.

So the "pw1" will be read from stdin, meaning we control the input for pw1 (which was supposed to be read from the "password" file).

So we can simply submit two numbers that are the XOR of each other.
For example, 0000000000 and 1111111111.

