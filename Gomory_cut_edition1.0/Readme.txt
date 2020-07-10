Nguyễn Văn Sơn -20163560 

Gomory-cut with dual-simplex 

# Cấu trúc chương trình
Gồm 5 class:

1. Simplex
- Giải bài toán LP (maximize) được cho dưới dạng chính tắc (ràng buộc đẳng thức) và biết trước một cơ sở chấp nhận được. Chúng ta cần phải đưa bài toán đầu vào thành dạng chuẩn tức đẳng thức.
tự thêm các slack vars vào file test.
- Input: ./data/simplex_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- m dòng tiếp theo,  trên mỗi dòng chứa lần lượt là ràng buộc của n biến , RHS (số thứ n+1), chỉ số của biến cơ sở trên dòng (số thứ n +2)
	- Dòng cuối cùng gồm n số là hệ số của các biến trong hàm mục tiêu
2. TwoPhase
- Giải bài toán LP (maximize) được cho dưới dạng chính tắc (ràng buộc đẳng thức) và chưa biết bất kỳ cơ sở chấp nhận được nào
- Input: ./data/twophase_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- m dòng tiếp theo,  trên mỗi dòng chứa lần lượt là ràng buộc của n biến , RHS (số thứ n+1)
	- Dòng cuối cùng gồm n số hữu tỉ là hệ số của các biến trong hàm mục tiêu
3. Gomory
- Giải bài toán MILP (maximize) được cho dưới dạng chính tắc (ràng buộc bất đẳng thức), trong đó tất cả các biến bị ràng buộc nguyên
- Input: ./data/gomory_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- m dòng tiếp theo,  trên mỗi dòng chứa lần lượt là ràng buộc của n biến , RHS (số thứ n+1)
	- Dòng thứ m + 2 gồm n số hữu tỉ là hệ số của các biến trong hàm mục tiêu
4. Dual Simplex
 Cài đặt thuật toán Dual simplex implement từ class Simplex
5.GomoryDualSimplex 
Cài đặt thuật toán gomory-cut dưới dạng bài toán dual.
đầu vào cũng giống bài toán gomory-cut

# Cách chạy chương trình
với mỗi class đều có def main vì thế chỉ cần sửa đường dẫn file phù hợp là có thể chạy được chương trình với câu lệnh
ví dụ:
thay đổi đường dẫn trong file:
   # test chuc nang cua file
    f = open("data/gomory_04", "r")
	và chạy 
python GomoryDualSimplex.py