#include<stdio.h>

int main(){
	char *pbVar3 = (char *)0x57;
	printf("%p\n",pbVar3);
	//char s[]="Magic";
	int param_1=0;
	int local_10 = 0x613b215e;
	/*for(int i=0;i<5;i++){
		pbVar3 = (char *)(param_1 + i);
		*pbVar3 = *(char *)(param_1 + i) ^
		          *(char *)((int)&local_10 + i) ^ s[i];
	}*/
	//printf("%s\n",pbVar3);
}