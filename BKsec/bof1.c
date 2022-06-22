#include <stdio.h>
#include <stdlib.h>


void win(){
	system("/bin/sh");
}

void getLong(long* a){
	puts("enter number : ");
	char buf[0x10] = {};
	fgets(buf, 0xf,stdin);
	*a = atol(buf);
}

int main(int argc, char const *argv[])
{
	setbuf(stdin,NULL);
	setbuf(stdout,NULL);
	printf("your main %p\n",main);

	long bof[0x10];
	long idx;
	long value;
	getLong(&idx);
	getLong(&value);
	bof[idx] = value;
	return 0;
}