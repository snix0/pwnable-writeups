### Synopsis
This is a challenge focused on understanding Linux file descriptors.

### Solution
The program is reading user input and checking the contents of the buffer after a call to `read(argv[1] - 0x1234, buffer, 32)` to see if it matches the string `LETMEWIN\n`.
Thus, we need to pass in a value that will make the first argument of read equal to stdin (the first argument is the file descriptor: see `man 2 read`).
The file descriptor for stdin is 0, so we want to satisfy `argv[1] - 0x1234 == 0`. If we convert 0x1234 to decimal, we get 4660.
Therefore, we need to pass in 4660 to `argv[1]` in order to get the program to read from stdin (4660 - 4660 == 0).

We run the program and pass in 4660, and we can see that the program appears to hang. However, this is exactly what we want!
It is now reading from stdin and placing whatever we type into the buffer.

In order to get the flag, we will pass in the correct string `LETMEWIN` into stdin followed by a newline, strcmp will return 0 since the strings are equal and we've got the flag!
