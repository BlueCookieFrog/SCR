#include <stdio.h>
#include <string.h>
#include <unistd.h>
#define PACKET_SIZE 10
int main(int argc, char *argv[])

{
    int pid;
    int fd[2];
    pipe(fd);

    if (pid = fork())
    {
        char buf[PACKET_SIZE];
        while (read(fd[0], buf, PACKET_SIZE))
        {
            if (buf[PACKET_SIZE - 1] == 0)
                break;
            buf[PACKET_SIZE - 1] = '\0';
            printf("#%s#\n", buf);
        }
    }
    else
    {
        //proces macierzysty
        FILE *f = fopen(argv[1], "r");
        char buf[PACKET_SIZE];
        while (fgets(buf, PACKET_SIZE - 1, f))
        {
            buf[PACKET_SIZE - 1] = 1;
            write(fd[1], buf, PACKET_SIZE);
        }

        buf[PACKET_SIZE - 1] = 0;
        write(fd[1], buf, PACKET_SIZE);

        fclose(f);
    };
}
