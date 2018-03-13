#include<stdlib.h>
#include<stdio.h>

int main() {
	int ret ;
	printf("Calling system...\n");
	ret = system("ls -l");
	printf("\nExiting system...");
	return 0;

}
