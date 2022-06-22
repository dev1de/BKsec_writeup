#include <stdio.h>

#include <math.h>
#include <stdlib.h>

void win(){
	system("/bin/sh");
}

void getLong(long* a){
	puts("enter number : ");
	getchar();
	char buf[0x10] = {};
	fgets(buf, 0xf,stdin);
	*a = atol(buf);
}

int main(int argc, char const *argv[])
{
	setbuf(stdin,NULL);
	setbuf(stdout,NULL);
	int idx;
	int result = 1;
	
	while(result){
		result = scanf("%d",&idx);
	}
	printf("%d",&idx);
	printf("your main %p\n",main);
	long bof[0x10];
	long value;
	getLong(&value);
	bof[idx] = value;

	printf("value %ld\n",value);
	return 0;
}