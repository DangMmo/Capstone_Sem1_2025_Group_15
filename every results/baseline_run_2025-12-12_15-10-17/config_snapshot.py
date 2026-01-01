# --- START OF FILE config.py ---

import random

# ==============================================================================
# 1. CẤU HÌNH BÀI TOÁN & DỮ LIỆU
# ==============================================================================
# Đường dẫn đầy đủ đến file dữ liệu đầu vào
FILE_PATH = "C:\\Users\\Dang\\Documents\\Capstone\\2e-vrp-pdd-main\\instance-set-tight-deadline\\100_customers_TD\\A_100_1_TD.csv"

# Tốc độ của phương tiện (đơn vị/thời gian)
VEHICLE_SPEED = 1.0  

# ==============================================================================
# 2. CẤU HÌNH GIAI ĐOẠN TẠO LỜI GIẢI BAN ĐẦU
# ==============================================================================
# [Mapping: initialLNS = 250]
LNS_INITIAL_ITERATIONS = 250

# Tỷ lệ khách hàng bị phá hủy trong giai đoạn tạo lời giải ban đầu
Q_PERCENTAGE_INITIAL = 0.4

# ==============================================================================
# 3. CẤU HÌNH GIAI ĐOẠN ALNS CHÍNH
# ==============================================================================
# [Mapping: iteration = 100000]
# Tổng số lần lặp cho thuật toán ALNS
ALNS_MAIN_ITERATIONS = 100000

# ----- 3.1. Các tham số cho Simulated Annealing (SA) -----
# [Mapping: initialAcceptanceProbability = 0.5]
START_TEMP_ACCEPT_PROB = 0.5

# [Mapping: temperatureControlParameter = 0.05]
START_TEMP_WORSENING_PCT = 0.05

# [Mapping: coolingRate = 0.9995]
COOLING_RATE = 0.9995

# ----- 3.2. Các tham số cho Cơ chế Học Thích ứng (Adaptive Mechanism) -----
# [Mapping: decayRate = 0.1]
# Hệ số phản ứng (reaction factor)
REACTION_FACTOR = 0.1

# [Mapping: batch = 100]
# Số lần lặp trong một "segment" trước khi cập nhật lại trọng số
SEGMENT_LENGTH = 100

# [Mapping: gamma1 = 9.0]
SIGMA_1_NEW_BEST = 9.0

# [Mapping: gamma2 = 5.0]
SIGMA_2_BETTER = 5.0

# [Mapping: gamma3 = 2.0]
SIGMA_3_ACCEPTED = 2.0

# (Lưu ý: gamma4 = 0.0 là mặc định cho trường hợp từ chối, không cần cấu hình biến riêng)

# ----- 3.3. Các tham số cho Logic Điều khiển ALNS Nâng cao (GIAI ĐOẠN 2) -----
# [Mapping: lowerBoundSmallRemoval=4, smallRemoval=0.2]
# Với 100 node, 4 node tương đương 0.04 (4%). Range sẽ là (0.04, 0.2)
Q_SMALL_RANGE = (0.04, 0.2)

# [Mapping: lowerBoundLargeRemoval=0.55, largeRemoval=0.8]
Q_LARGE_RANGE = (0.55, 0.8)

# [Mapping: largeRemovalOccurrence = 500]
# Số lần phá hủy nhỏ liên tiếp trước khi thực hiện một lần phá hủy lớn
SMALL_DESTROY_SEGMENT_LENGTH = 500

# [Mapping: restartPeriod = 10000]
# Số lần lặp không cải thiện hoặc chu kỳ để khởi động lại
RESTART_THRESHOLD = 10000


# ==============================================================================
# 4. CẤU HÌNH CHUNG
# ==============================================================================
RANDOM_SEED = 42

# ==============================================================================
# 5. CẤU HÌNH PRUNING (CẮT TỈA) CHO LOGIC CHÈN
# ==============================================================================
PRUNING_K_CUSTOMER_NEIGHBORS = 10
PRUNING_M_SATELLITE_NEIGHBORS = 3
PRUNING_N_SE_ROUTE_CANDIDATES = 2

# ==============================================================================
# 6. CẤU HÌNH HÀM MỤC TIÊU (OBJECTIVE FUNCTION)
# ==============================================================================
PRIMARY_OBJECTIVE = "DISTANCE" 
OPTIMIZE_VEHICLE_COUNT = True
WEIGHT_PRIMARY = 1.0
WEIGHT_FE_VEHICLE = 1000.0
WEIGHT_SE_VEHICLE = 200.0

# ==============================================================================
# 7. CẤU HÌNH DỌN DẸP KẾT QUẢ
# ==============================================================================
CLEAR_OLD_RESULTS_ON_START = False

# ==============================================================================
# 8. CẤU HÌNH PHÂN CỤM (CLUSTERING CONFIGURATION)
# ==============================================================================
K_CLUSTERS_RANGE = range(2, 10) 
MAX_SCHEDULING_FLEXIBILITY = 900.0

# ==============================================================================
# 9. CẤU HÌNH ĐƯỜNG DẪN VÀ THƯ MỤC
# ==============================================================================
RESULTS_BASE_DIR = "results"

# --- NOTES ON UNMAPPED PARAMETERS ---
# perturbation = 0.5        -> Không có biến tương ứng trực tiếp (thường nằm trong logic code xáo trộn)
# perturbationFactor = 0.01 -> Không có biến tương ứng trực tiếp
# split = 20000             -> Không có biến tương ứng trực tiếp