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



Đọc source code, ta có thể thấy chương trình in ra địa chỉ của hàm main, sau đó cho phép chúng ta ghi value vào vị trí bof[idx]

Chúng ta dễ dàng thấy, có thể ghi 1 giá trị bất kì vào 1 địa chỉ ở trong stack
-> chúng ta có thể ghi đè return value ở hàm main bằng địa chỉ của hàm win 

Dùng gdb, disass hàm main ta thấy địa chỉ của bof là rbp-0x90
![alt text](https://github.com/dev1de/images/blob/main/1.png)



