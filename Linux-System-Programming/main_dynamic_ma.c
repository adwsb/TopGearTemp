#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/wait.h>

static char mode[2], *ifile, *ofile; 
static pid_t pid;
static int onset[2], offset[2], size;

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

		ifile = (char*) malloc(strlen(argv[2])* sizeof(char));
		ofile = (char*) malloc(strlen(argv[3])* sizeof(char));

		strcpy(ifile, argv[2]);
		strcpy(ofile, argv[3]);		

	}
	else{
		invalid:
		printf("Invalid");
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

///////////////////////////////////////////////////////////////////////////////////////
	if(pid == 0)
	{
	// Child

		char *buffer;
		buffer = (char*) malloc(size * sizeof(char));

		printf("%d\n", size);

		if(buffer == NULL)
		{
			printf("Buffer Error\n");
			exit(1);
		}

	// IPC Receive
		close(onset[1]);
		read(onset[0], buffer, size);
		
	// Case Change
		printf("%s\n", buffer);

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
		write(offset[1], buffer, size);
		close(offset[1]);

	}
///////////////////////////////////////////////////////////////////////////////////////
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
		
		char *buffer;
		buffer = (char*) malloc(size * sizeof(char));

		if(buffer == NULL)
		{
			printf("Buffer Error\n");
			exit(1);
		}

		fread(buffer, sizeof(char), size, readfp);
		fclose(readfp);

	// IPC Send
		close(onset[0]);
		printf("%s\n", buffer);
		write(onset[1], buffer, size);
		close(onset[1]);
		wait(NULL);

	// IPC Receive
		close(offset[1]);
		read(offset[0], buffer, size);
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