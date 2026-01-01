# Capstone_Sem1_2025_Group_15
Decompose-Route-Improve: A Clustering and Metaheuristic Framework for Two-Echelon Vehicle Routing in E-commerce
Authors: 
Ngô Trọng Đăng - IELSIU22015
Phan Vũ Minh Ngọc - IELSIU22340
Nguyễn Hải Vân Trang - IELSIU22339
------
Đây là bài Capstone thực hiện tại trường Đại học Quốc Tế - Đại học Quốc Gia dưới sự hướng dẫn của Dr. Hà Thị Xuân Chi lấy cảm hứng từ các bài báo key references sau: 
Ropke, S., Pisinger, D., 2006. An adaptive large neighborhood search heuristic for the pickup and delivery problem with time windows. Transp. Sci. 40 (4), 455–472. http://dx.doi.org/10.1287/trsc.1050.0135.
Zamal, M. A., Schrotenboer, A. H., & Van Woensel, T. (2025). The two-echelon vehicle routing problem with pickups, deliveries, and deadlines. Computers & Operations Research, 107016. https://doi.org/10.1016/j.cor.2025.107016
Kerscher, C., & Minner, S. (2025). Decompose-route-improve framework for solving large-scale vehicle routing problems with time windows. Transportation Research Part E: Logistics and Transportation Review, 204, 104409. https://doi.org/10.1016/j.tre.2025.104409
-----
Trong link Git hub này gồm các Instances set đã được test cùng Results được thực hiện bởi nhóm sinh viên trường Đại học Quốc Tế - Đại học Quốc Gia
-----
HƯỚNG DẪN SỬ DỤNG CODE:

Bài Capstone này giải cho bài toán Vận tải Hai cấp (2E-VRP) có các ràng buộc về Cửa sổ thời gian và Deadline (2E-VRP-PDD). Thuật toán cốt lõi là Adaptive Large Neighborhood Search (ALNS), được tăng cường với một phương pháp tiền xử lý bằng cách phân cụm khách hàng.

## **Tính năng chính**

- **Hai chế độ hoạt động:**
  1.  **Baseline:** Giải quyết toàn bộ bài toán bằng một lượt chạy ALNS.
  2.  **Clustered:** Tự động phân cụm khách hàng thành các bài toán con, giải quyết từng bài toán con, sau đó hợp nhất thành lời giải cuối cùng.
- **Hàm mục tiêu linh hoạt:** Dễ dàng cấu hình để tối ưu hóa theo **Khoảng cách** hoặc **Thời gian di chuyển**.
- **Tối ưu hóa số lượng xe:** Có thể bật/tắt việc đưa chi phí sử dụng xe vào hàm mục tiêu.
- **Phân tích và Trực quan hóa:** Tự động tạo và lưu log chi tiết, biểu đồ hội tụ, và bản đồ trực quan hóa lời giải sau mỗi lần chạy.

## **Cài đặt**

Dự án này được viết bằng Python. Bạn cần cài đặt các thư viện cần thiết trước khi chạy. Nếu không biết sử dụng Git clone, cứ tải full tệp xuống như bình thường

1.  **Clone a repository (Tải a repository):**
    ```bash
    git clone https://your-repository-url.git](https://github.com/DangMmo/Capstone_Sem1_2025_Group_15.git
    cd VRP_Solver_Integrated
    ```

2.  **Cài đặt các thư viện:**
    Cài đặt các gói từ file `requirements.txt`.

    ```bash
    # Cài đặt các thư viện
    pip install -r requirements.txt
    ```

    **File `requirements.txt`:**
    ```
    pandas
    numpy
    matplotlib
    seaborn
    scikit-learn
    kmedoids
    ```

## **Cách sử dụng**

Tất cả các cấu hình chính đều nằm trong file `src/config.py`. Hãy mở file này và chỉnh sửa các tham số trước khi chạy.

### **1. Cấu hình**

Mở file `src/config.py` và chỉnh sửa các mục quan trọng:

-   **`FILE_PATH`**: Đường dẫn tuyệt đối đến file dữ liệu đầu vào (`.csv`).
-   **`ALNS_MAIN_ITERATIONS`**: Số vòng lặp cho thuật toán ALNS chính.
-   **`PRIMARY_OBJECTIVE`**: Chọn `"DISTANCE"` hoặc `"TRAVEL_TIME"`.
-   **`OPTIMIZE_VEHICLE_COUNT`**: Đặt là `True` hoặc `False`.
-   **`K_CLUSTERS_RANGE`**: (Dành cho chế độ Clustered) Khoảng số cụm `k` để thử nghiệm.

### **2. Chạy các kịch bản**

Mở terminal tại thư mục gốc của dự án (`VRP_Solver_Integrated/`) và chạy một trong các lệnh sau:

-   **Để chạy bộ giải trên toàn bộ bài toán (Baseline):**
    ```bash
    python run_baseline_solver.py
    ```

-   **Để chạy bộ giải với phương pháp phân cụm:**
    ```bash
    python run_clustered_solver.py
    ```
    *Chương trình sẽ gợi ý số cụm (`k`) tối ưu. Bạn có thể nhấn Enter để chấp nhận hoặc nhập một số khác.*

### **3. Xem kết quả**

-   Sau mỗi lần chạy, một thư mục con mới sẽ được tạo trong thư mục `results/`.
-   Ví dụ: `results/baseline_run_2023-10-27_15-00-00/`.
-   Bên trong thư mục này chứa:
    -   `log.txt`: Toàn bộ output của chương trình.
    -   `config_snapshot.py`: Bản sao của file config đã được sử dụng.
    -   Các file ảnh `.png`: Trực quan hóa lời giải, biểu đồ hội tụ, v.v.
    -   (Chỉ ở chế độ Clustered) Các thư mục con chứa dữ liệu và lời giải của từng cụm.

## **Cấu trúc dự án**

```
VRP_Solver_Integrated/
├── src/                  # Chứa toàn bộ code logic
│   ├── algorithm/        # Các thuật toán (ALNS, Clustering)
│   ├── core/             # Các cấu trúc dữ liệu cốt lõi
│   ├── utils/            # Các công cụ hỗ trợ (plotter, logger)
│   └── config.py         # File cấu hình chính
├── data/                 # Chứa các file dữ liệu đầu vào
├── results/              # Chứa kết quả sau mỗi lần chạy
├── run_baseline_solver.py  # File thực thi cho chế độ Baseline
└── run_clustered_solver.py   # File thực thi cho chế độ Clustered
```
