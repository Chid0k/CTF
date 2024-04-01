# CPU Registers
---
Các thanh ghi là thành phần thiết yếu của CPU. Hầu hết tất cả các thanh ghi đều cung cấp một lượng nhỏ không gian lưu trữ để dữ liệu có thể được lưu trữ tạm thời. Tuy nhiên, một số trong số chúng có một chức năng cụ thể.

Các thanh ghi này sẽ được chia thành các thanh ghi chung, thanh ghi điều khiển và thanh ghi phân đoạn.

Các thanh ghi quan trọng nhất mà chúng ta cần là các thanh ghi chung.Trong đó, có các phân chia nhỏ hơn thành các thanh ghi Dữ liệu, các thanh ghi Con trỏ và các thanh ghi Chỉ mục.

## Thanh ghi dữ liệu - Data registers

| 32-bit Register | 64-bit Register | Mô tả                                                                                                   |
|-----------------|-----------------|---------------------------------------------------------------------------------------------------------|
| EAX             | RAX             | (Accumulator) Bộ tích lũy được sử dụng trong đầu vào/đầu ra và cho các phép tính số học                 |
| EBX             | RBX             | (Base) Địa chỉ được lập chỉ mục                                                                         |
| ECX             | RCX             | (Count) được sử dụng để xoay hướng dẫn và đếm vòng lặp                                                  |
| EDX             | RDX             | (Data) Được sử dụng cho I/O và trong các phép tính số học cho các phép tính nhân và chia có giá trị lớn |


## Thanh ghi con trỏ lệnh - Pointer registers

| 32-bit Register | 64-bit Register | Mô tả                                                                                        |
|:---------------:|:---------------:|----------------------------------------------------------------------------------------------|
| EIP             | RIP             | Chứa địa chỉ offset của lệnh sau sẽ thực hiện                                                |
| ESP             | RSP             | Con trỏ ngăn xếp trỏ đến đỉnh ngăn xếp                                                       |
| EBP             | RBP             | Base pointer còn được gọi là Stack base pointer hoặc Frame pointer trỏ đến Base của ngăn xếp |

## Stack Frames

Ngăn xếp bắt đầu từ địa chỉ cao và giảm dần xuống địa chỉ thấp trong bộ nhớ khi các giá trị dược thêm vào. Nên <span style="color:blue">Base pointer</span> trỏ đến phần cơ sở (Base) của ngăn xếp - Trái ngược với <span style="color:blue">Stack poiter</span> trỏ đến đỉnh ngăn xếp.

Khung ngăn xếp xác định khung dữ liệu có **Begin (EBP)** và **End (ESP)** được đẩy lên ngăn xếp khi một hàm được gọi.

```shell
| Address | Stack  |
|:-------:|:------:|
| Low     | ...... | <--- ESP           
|         | Data 0 |                    DATA
|         | Data 1 |                     ⬇
|         | Data 2 |                     ⬇
| High    | ...... | <--- EBP          
```

Do bộ nhớ ngăn xếp được xây dựng trên cấu trúc dữ liệu Vào trước ra trước (LIFO) nên bước đầu tiên là lưu trữ vị trí EBP trước đó trên ngăn xếp, vị trí này có thể được khôi phục sau khi chức năng hoàn thành.

* **EBP :** Được đặt đầu tiên khi hàm được gọi và chứa EBP của khung ngăn xếp trước đó. 
* **ESP :** Được đặt trên cùng cho các hoạt động và biến xử lí trong ngăn xếp.

**Example :**
```shell
(gdb) disas bowfunc 

Dump of assembler code for function bowfunc:
   0x0000054d <+0>:	    push   ebp       # <---- 1. Stores previous EBP
   0x0000054e <+1>:	    mov    ebp,esp
   0x00000550 <+3>:	    push   ebx
   0x00000551 <+4>:	    sub    esp,0x404
   <...SNIP...>
   0x00000580 <+51>:	leave  
   0x00000581 <+52>:	ret 

```

**EBP** trong khung ngăn xếp được đặt đầu tiên khi hàm được gọi và chứa **EBP** của khung ngăn xếp trước đó. Tiếp theo, giá trị của **ESP** được sao chép vào **EBP**, tạo khung ngăn xếp mới.

```shell
(gdb) disas bowfunc 

Dump of assembler code for function bowfunc:
   0x0000054d <+0>:	    push   ebp       # <---- 1. Stores previous EBP
   0x0000054e <+1>:	    mov    ebp,esp   # <---- 2. Creates new Stack Frame
   0x00000550 <+3>:	    push   ebx
   0x00000551 <+4>:	    sub    esp,0x404 
   <...SNIP...>
   0x00000580 <+51>:	leave  
   0x00000581 <+52>:	ret    
```

Sau đó, một số không gian được tạo trong ngăn xếp, di chuyển **ESP** lên trên cùng cho các hoạt động và các biến cần thiết và được xử lý.

```shell
(gdb) disas bowfunc 

Dump of assembler code for function bowfunc:
   0x0000054d <+0>:	    push   ebp       # <---- 1. Stores previous EBP
   0x0000054e <+1>:	    mov    ebp,esp   # <---- 2. Creates new Stack Frame
   0x00000550 <+3>:	    push   ebx
   0x00000551 <+4>:	    sub    esp,0x404 # <---- 3. Moves ESP to the top
   <...SNIP...>
   0x00000580 <+51>:	leave  
   0x00000581 <+52>:	ret    
```

## Prologue

Ba lệnh trên được gọi là **Prologue**. Để thoát khỏi khung ngăn xếp thì làm ngược lại **Epilogue**. 

## Epilogue

```shell
(gdb) disas bowfunc 

Dump of assembler code for function bowfunc:
   0x0000054d <+0>:	    push   ebp       
   0x0000054e <+1>:	    mov    ebp,esp   
   0x00000550 <+3>:	    push   ebx
   0x00000551 <+4>:	    sub    esp,0x404 
   <...SNIP...>
   0x00000580 <+51>:	leave  # <----------------------
   0x00000581 <+52>:	ret    # <--- Rời khỏi stack.
```

## Thanh ghi chỉ số - Index registers

| Register 32-bit | Register 64-bit | Description                                                            |
|-----------------|-----------------|------------------------------------------------------------------------|
| ESI             | RSI             | Source Index được sử dụng làm con trỏ từ nguồn cho các hoạt động chuỗi |
| EDI             | RDI             | Destination được sử dụng làm con trỏ tới đích cho các thao tác chuỗi   |


## CALLING

Lệnh **call** dùng để gọi một hàm và thực hiện hai thao tác sau:
- _Push_ **Return address** vào stack để việc thực hiện chương trình có thể được tiếp tục sau khi chức năng đã hoàn thành thành công mục tiêu của nó.
- Thay đổi thanh ghi lệnh EIP(instruction pointer), đến đích hàm được **call** và bắt đầu thực hiện ở đó.






