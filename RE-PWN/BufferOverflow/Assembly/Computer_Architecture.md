# Computer Architecture
---
Ngày nay, hầu hết các máy tính hiện đại đều được xây dựng trên kiến ​​trúc Von Neumann. 

Nó chủ yếu bao gồm các yếu tố sau:
- Central Processing Unit (CPU)
    - Control Unit (CU)
    - Arithmetic/Logic Unit (ALU)
    - Registers
- Memory Unit
- Input/Output Devices
    - Mass Storage Unit
    - Keyboard
    - Display

![Computer Architecture](https://academy.hackthebox.com/storage/modules/85/von_neumann_arch.jpg)

## [+] Memory
Bộ nhớ của máy tính là nơi chứa dữ liệu **tạm thời** và hướng dẫn của các chương trình đang chạy goij là **Primary Memory**.

Đây là vị trí chính mà CPU sử dụng để truy xuất và xử lý dữ liệu. Việc này diễn ra rất thường xuyên (hàng tỷ lần một giây), do đó bộ nhớ phải cực kỳ nhanh trong việc lưu trữ và truy xuất dữ liệu cũng như hướng dẫn.

Có hai loại bộ nhớ chính:
- Cache
- Random Access Memory (RAM)

### Cache

Cache nằm trong CPU và có tốc độ chạy rất nhanh (hơn RAM) vì có cùng tốc độ vs CPU. Tuy nhiên, nó rất hạn chế về kích thước, rất phức tạp và đắt tiền để sản xuất do nó nằm quá gần lõi CPU.

Vì tốc độ xung nhịp của RAM thường chậm hơn nhiều so với lõi CPU, ngoài việc nó ở xa CPU, nếu CPU phải đợi RAM truy xuất từng lệnh thì nó thực sự sẽ chạy ở tốc độ xung nhịp thấp hơn nhiều. Đây là lợi ích chính của bộ nhớ đệm. Nó cho phép CPU truy cập các lệnh và dữ liệu sắp tới nhanh hơn việc lấy chúng từ RAM

Thường có ba cấp độ bộ nhớ đệm, tùy thuộc vào mức độ gần với lõi CPU:
| Level         | Description                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------|
| Level 1 Cache | Usually in kilobytes, the fastest memory available, located in each CPU core. (Only registers are faster.) |
| Level 2 Cache | Usually in megabytes, extremely fast (but slower than L1), shared between all CPU cores.                   |
| Level 3 Cache | Usually in megabytes (larger than L2), faster than RAM but slower than L1/L2. (Not all CPUs use L3.)       |

### RAM
RAM lớn hơn nhiều so với bộ nhớ đệm, có kích thước từ gigabyte đến terabyte. RAM cũng nằm cách xa lõi CPU và chậm hơn rất nhiều so với bộ nhớ đệm. Việc truy cập dữ liệu từ các địa chỉ RAM cần nhiều hướng dẫn hơn.


Ví dụ: việc truy xuất lệnh từ các thanh ghi chỉ mất một chu kỳ xung nhịp và việc truy xuất lệnh từ bộ đệm L1 mất một vài chu kỳ, trong khi truy xuất lệnh từ RAM mất khoảng 200 chu kỳ.


Trước đây, với địa chỉ 32 bit, địa chỉ bộ nhớ bị giới hạn từ 0x00000000 đến 0xffffffff. Điều này có nghĩa là kích thước RAM tối đa có thể là 2^32 byte, tức là chỉ 4 gigabyte, tại thời điểm đó chúng tôi đã hết địa chỉ duy nhất


Với địa chỉ 64 bit, phạm vi hiện lên tới 0xffffffffffffffff, với kích thước RAM tối đa theo lý thuyết là 2^64 byte, tức là khoảng 18,5 exabyte (18,5 triệu terabyte), vì vậy chúng ta sẽ không sớm hết địa chỉ bộ nhớ

Khi một chương trình được chạy, tất cả dữ liệu và hướng dẫn của nó sẽ được chuyển từ bộ lưu trữ sang RAM để CPU có thể truy cập khi cần.Điều này xảy ra vì việc truy cập chúng từ thiết bị lưu trữ chậm hơn nhiều và sẽ tăng thời gian xử lý dữ liệu. Khi một chương trình bị đóng, dữ liệu của nó sẽ bị xóa hoặc có sẵn để sử dụng lại từ RAM.

Như chúng ta có thể thấy, RAM được chia thành bốn phân đoạn chính:

![RAM](https://academy.hackthebox.com/storage/modules/85/memory_structure.jpg)


- Stack: Last in first out
- HEAP: Có thiết kế phân cấp và do đó lớn hơn và linh hoạt hơn nhiều trong việc lưu trữ dữ liệu vì dữ liệu có thể được lưu trữ và truy xuất theo bất kỳ thứ tự nào. Tuy nhiên, điều này làm cho heap chậm hơn so với Stack.
- Data: Có hai phần: Dữ liệu, được sử dụng để giữ các biến và .bss, được sử dụng để chứa các biến chưa được gán (tức là bộ nhớ đệm để phân bổ sau này).
- Text: Các lệnh lắp ráp chính được tải vào phân đoạn này để CPU tìm nạp và thực thi.


## [+] IO/Storage
Bộ xử lý có thể truy cập và điều khiển các thiết bị IO bằng Giao diện Bus, hoạt động như 'đường cao tốc' để truyền dữ liệu và địa chỉ, sử dụng điện tích cho dữ liệu nhị phân.

Không giống như bộ nhớ chính dễ thay đổi và lưu trữ dữ liệu cũng như hướng dẫn tạm thời khi chương trình đang chạy, bộ nhớ lưu trữ dữ liệu cố định, như tệp hệ điều hành hoặc toàn bộ ứng dụng và dữ liệu của chúng.

Đã có sự thay đổi từ các thiết bị lưu trữ từ tính cổ điển, như băng hoặc Ổ đĩa cứng (HDD), sang Ổ đĩa thể rắn (SSD) trong những năm gần đây. Điều này là do SSD sử dụng thiết kế tương tự như RAM, sử dụng mạch ổn định để lưu giữ dữ liệu ngay cả khi không có điện. Điều này làm cho các đơn vị lưu trữ nhanh hơn nhiều trong việc lưu trữ và truy xuất dữ liệu.

Tuy nhiên, vì chúng ở xa CPU và được kết nối thông qua các giao diện đặc biệt nên chúng là thiết bị truy cập chậm nhất.


## [+] CPU

Instruction Cycle là chu kỳ mà CPU cần để xử lý một lệnh máy.
![](https://academy.hackthebox.com/storage/modules/85/assembly_instruction_cycle.jpg)

Các bộ xử lý hiện đại có thể xử lý song song nhiều lệnh bằng cách cho nhiều chu kỳ lệnh/đồng hồ chạy cùng lúc. Điều này được thực hiện nhờ có thiết kế đa luồng và đa lõi.

![](https://academy.hackthebox.com/storage/modules/85/assembly_clock_cycle_2.jpg)


Mỗi loại bộ xử lý có Kiến trúc tập lệnh riêng và mỗi kiến ​​trúc có thể được biểu diễn sâu hơn bằng một số định dạng cú pháp


```
| Instruction |                                        Description                                        |
|:-----------:|:-----------------------------------------------------------------------------------------:|
|     call    | push the next instruction pointer rip to the stack, then jumps to the specified procedure |
|     ret     | pop the address at rsp into rip, then jump to it                                          |
```

