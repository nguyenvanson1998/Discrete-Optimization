# Discrete-Optimization
Báo cáo giữa kỳ Tối ưu tổ hợp
1. Bài toán Knapsack(60/60)
•	Quy hoạch động(3 test đầu: 10/10): giải chính xác với bộ dữ liệu nhỏ (số item <400) các bộ khác bị ngắt do thời gian giải hàm mũ
•	Greedy(tất cả các test 7/10): Tham lam theo tỉ lệ  value/weight của từng đồ vật
•	Ortools multi-brand and bound( 60/60): sử dụng thư viện ortools cho bài knapshack và áp dụng chiến thuật brand and bound trong thư viện (CP)

2. Bài toán Coloring(54/60)
•	Sử dụng phương pháp random kết hợp hoán vị ngẫu nhiên(Test 1,2,3,5 : 10/10 , Test 4,6 : 7/10):  Đưa ra một lời giải greedy cho bài toán sau đó sử dụng chiến lược hoán vị ngẫu nhiên như sau. Nhóm các đỉnh đã tô cùng màu vào 1 group, với mỗi group sắp xếp theo bậc của đỉnh. Hoán vị các group được 1 cách sắp xếp các đỉnh mới. dùng greedy tô màu cho các đỉnh mới theo bậc của đỉnh. lặp lại các bước trên 1000 lần để tìm kết quả tối ưu.(Thuật toán trong discussion)
3. Bài toán TSP(48/60)
•	Test1 ,test 2 :10/10 với các test có số đỉnh từ 200 trở lên 7/10
•	Phương pháp sử dụng ortools dùng chiến lược localsearch 2-opt và or-otp
•	Với test cuối ortools bị out do quá thời gian chạy sử dụng chiến lược greedy theo cách chọn đỉnh gần nó nhất mà chưa được chọn trong mỗi bước lặp và không xây dựng distance matrix để tiết kiệm bộ nhớ.
4. Bài toán Facility Location(80/80)
•	Sử dụng mô hình mip sau đây :  
•	Với các test 1,2,3 do số lượng customers và facilities nhỏ nên sử dụng mip-ortools luôn
•	Với các test 4,5,6,7,8 ta sử dụng chiến lược local search + mip: sử dụng thuật toán greedy (chọn lần lượt các nhà máy còn sức chứa để phục vụ khác hàng đến khi hết khách hàng). Từ kết quả đã có random chọn 1 nhà máy và 100 nhà máy gần nhất với nó, các khách hàng mà nó phục vụ để chạy mô hình mip. Thực hiện đến 10000 bước lặp.
5.Bài toán Vehicle Routing(54/60)
•	Sử dụng ortools với tham số là localsearch 2-opt để giải quyết bài toán
6. Bài toán quy hoạch nguyên
•	Đã cài đặt thuật toán Gomory và nhánh cận
Input: ./data/gomory_xx
	- Dòng đầu gồm 2 số nguyên m và n lần lượt là số ràng buộc và số biến
	- m dòng tiếp theo,  trên mỗi dòng chứa lần lượt là ràng buộc của n biến , RHS (số thứ n+1)
	- Dòng thứ m + 2 gồm n số hữu tỉ là hệ số của các biến trong hàm mục tiêu
•	Trong đó đang sử dụng tối đa m = 6 và n =5.
•	Đã cài đặt thêm thuật toán branch and bound và branch and cut, và thử với các bộ dữ liệu đầu vào ở trên. Tuy nhiên với bài set cover các ràng buộc đã ở dạng cover cut nên trong quá trình thêm constraint, nó không tự thêm constraint cover cut nào cả. Thuật toán chạy khá chậm.


 
