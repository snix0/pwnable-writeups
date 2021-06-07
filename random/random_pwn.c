#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Random: %d\n", rand() ^ 0xdeadbeef);
    return 0;
}
