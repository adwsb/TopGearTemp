#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/wait.h>

static char mode[2], ifile[20], ofile[20]; 
static pid_t pid;
static int onset[2], offset[2], size;
char buffer[100];

// Function to parse command line arguments
void parsearg(int argc, char *argv[])
{
	if(argc == 4){
		if(!strcmp(argv[1], "-l"))
		{
			strcpy(mode,"-l");
		}
		else if(!strcmp(argv[1], "-u"))
		{
			strcpy(mode,"-u");
		}
		else
		{
			goto invalid;
		}

		strcpy(ifile, argv[2]);
		strcpy(ofile, argv[3]);
	}
	else
	{
		invalid:
		printf("Usage: convert [ -l | -u ] inputfile outputfile");
		exit(1);
	}
}

int main(int argc, char const *argv[])
{
	parsearg(argc, (char**)argv);
	int reton = pipe(onset);
	int retoff = pipe(offset);
	
	pid = fork();

	if(pid == -1)
	{
		perror("Error creating process");
		exit(-1);
	}
	if(reton == -1 || retoff == -1)
	{
		perror("Error creating pipes");
		exit(-1);
	}


	if(pid == 0)
	{
	// Child

	// IPC Receive
		close(onset[1]);
		read(onset[0], buffer, 100);
		
	// Case Change
		if(!strcmp(mode, "-l"))
		{
			for(int i=0; buffer[i]!='\0'; i++)
			{
				if(isupper(buffer[i]))
				{
					buffer[i] = tolower(buffer[i]);
				}
			}
		}
		else if(!strcmp(mode, "-u"))
		{
			for(int i=0; buffer[i]!='\0'; i++)
			{
				if(islower(buffer[i]))
				{
					buffer[i] = toupper(buffer[i]);
				}
			}	
		}

	// IPC Send
		close(offset[0]);
		write(offset[1], buffer, 100);
		close(offset[1]);

	}
	else
	{
	// Parent

	// File Reading
		FILE *readfp;
		readfp = fopen(ifile, "r");

		if(readfp == NULL)
		{
			printf("File %s does not exist\n", ifile);
			exit(1);
		}

		fseek(readfp, 0L, SEEK_END);
		size = ftell(readfp);
		fseek(readfp, 0L, SEEK_SET);
		// buffer = (char*)calloc(size, sizeof(char));

		// if(buffer == NULL)
		// {
		// 	printf("Buffer Error\n");
		// 	exit(1);
		// }

		fread(buffer, sizeof(char), size, readfp);
		fclose(readfp);

	// IPC Send
		close(onset[0]);
		write(onset[1], buffer, 100);
		close(onset[1]);
		
		wait(NULL);

	// IPC Receive
		close(offset[1]);
		read(offset[0], buffer, 100);
		close(offset[0]);

	// File Writing
		FILE *writefp;
		writefp = fopen(ofile, "w");

		if(writefp == NULL)
		{
			printf("Error creating file %s\n", ofile);
			exit(1);
		}

		fprintf(writefp, "%s\n", buffer);

	}



	return 0;
}