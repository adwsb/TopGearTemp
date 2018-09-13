#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h> 
#include <sys/types.h> 
  

void SIGPIPE_handler(int signal)
{
	printf("SIGPIPE Encountered\n");
	exit(1);
}
  
int main() 
{ 
    int fd1; 
  
    // FIFO file path 
    char * myfifo = "fifo"; 
  
    // Creating the named file(FIFO) 
    // mkfifo(<pathname>,<permission>) 
    mkfifo(myfifo, 0666); 

	signal(SIGPIPE, SIGPIPE_handler);

  
    char str1[80], str2[80]; 
    while (1) 
    { 

        // First open in read only and read 
        fd1 = open(myfifo,O_RDONLY); 
        read(fd1, str1, 80); 
  
        // Print the read string and close 
        printf("User1: %s\n", str1); 
        close(fd1); 
  
        // Now open in write mode and write 
        // string taken from user. 
        fd1 = open(myfifo,O_WRONLY); 
        fgets(str2, 80, stdin); 
        write(fd1, str2, strlen(str2)+1); 
        close(fd1); 
    } 
    return 0; 
} 