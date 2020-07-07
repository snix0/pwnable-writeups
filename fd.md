### Synopsis
This is a challenge focused on understanding Linux file descriptors. We are given a SUID binary which reads input from a file descriptor and compares it to a given string.
The file descriptor is passed in via argv[1]. If the strings are equal, the flag (owned by the SUID user) is fetched.

### Source Code
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
    if(argc<2){
        printf("pass argv[1] a number\n");
        return 0;
    }
    int fd = atoi( argv[1] ) - 0x1234;
    int len = 0;
    len = read(fd, buf, 32);
    if(!strcmp("LETMEWIN\n", buf)){
        printf("good job :)\n");
        system("/bin/cat flag");
        exit(0);
    }
    printf("learn about Linux file IO\n");
    return 0;
}
```

### Analysis
The program is reading user input and checking the contents of the buffer after a call to `read(argv[1] - 0x1234, buffer, 32)` to see if it matches the string `LETMEWIN\n`.
Thus, we need to pass in a value that will make the first argument of read equal to stdin (the first argument is the file descriptor: see `man 2 read`).
The file descriptor for stdin is 0, so we want to satisfy `argv[1] - 0x1234 == 0`. If we convert 0x1234 to decimal, we get 4660.
Therefore, we need to pass in 4660 to `argv[1]` in order to get the program to read from stdin (4660 - 4660 == 0).

We run the program and pass in 4660, and we can see that the program appears to hang. However, this is exactly what we want!
It is now reading from stdin and placing whatever we type into the buffer.

In order to get the flag, we will pass in the correct string `LETMEWIN` into stdin followed by a newline, strcmp will return 0 since the strings are equal and we've got the flag!
