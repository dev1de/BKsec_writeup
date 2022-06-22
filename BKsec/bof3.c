#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getLong(long* a){
	puts("enter number : ");
	char buf[0x10] = {};
	fgets(buf, 0xf,stdin);
	*a = atol(buf);
}

long *bof;

void aaaa(){
	printf("puts %p\n",puts);
	printf("main %p\n",aaaa);

	long size = 0;
	getLong(&size);
	bof = (long*)malloc(size);
	strcpy((char*)bof,"/bin/sh\x00"); // for anyone need it


	long idx;
	long value;
	getLong(&idx);
	getLong(&value);
	bof[idx] = value;

}

int main(int argc, char const *argv[])
{
	/* code */
	setbuf(stdin,NULL);
	setbuf(stdout,NULL);


	aaaa();

	puts("done\n");
	free(bof);

	return 0;
}