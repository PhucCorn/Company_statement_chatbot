from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from langchain_core.documents import Document

def get_session_history_mongodb(session_id):
    return MongoDBChatMessageHistory(
        'mongodb://localhost:27017/', 
        session_id, 
        database_name="company_statement_chat_database", 
        collection_name="messages"
    )
    
def bbas_docs():
    docs = docs = [
        Document(
            page_content="Tuyên ngôn doanh nghiệp: \"là tuyên bố chính thức của doanh nghiệp đối với khách hàng, đối tác, người lao động, cộng đồng và các bên liên quan khác về doanh nghiệp.\"",
            metadata={"topic": "định nghĩa tuyên ngôn doanh nghiệp"},
        ),
        Document(
            page_content="""Tuyên ngôn của một tổ chức: 
            \"- Không phải là những lời sáo rỗng
            - Không phải là những câu khoe khoang; Không phải là những lời ...tự sướng
            - Là linh hồn, bản chất, con người thực
            - Là niềm tin, lẽ sống, «tôn giáo»
            - Là sự định vị rõ ràng, nhất quán
            - Là cách thức để tìm “bạn” tốt
            - Là VĂN HÓA TỔ CHỨC
            - Là CÔNG CỤ MARKETING
            - Là THÔNG ĐIỆP TRUYỀN THÔNG hiệu quả
            - Là LỢI THẾ CẠNH TRANH\"
            """,
            metadata={"topic": "tuyên ngôn của tổ chức"},
        ),
        Document(
            page_content="TUYÊN NGÔN ĐẠO ĐỨC: \"Mô tả cam kết của công ty với việc duy trì các chuẩn mực đạo đức cao trong mọi hoạt động kinh doanh. Nó hướng dẫn nhân viên về cách thức hành xử một cách trung thực và công bằng.\"",
            metadata={"topic": "định nghĩa tuyên ngôn đạo đức"},
        ),
        Document(
            page_content="TUYÊN NGÔN CHẤT LƯỢNG: \"Phản ánh cam kết của công ty đối với việc duy trì chất lượng sản phẩm hoặc dịch vụ. Nó thường bao gồm các mục tiêu chất lượng cụ thể và cách thức công ty đo lường và đạt được chúng.\"",
            metadata={"topic": "định nghĩa tuyên ngôn đạo đức"},
        ),
        Document(
            page_content="TUYÊN NGÔN ĐA DẠNG, BÌNH ĐẰNG, HÒA NHẬP: \"Biểu thị cam kết của công ty với việc xây dựng một môi trường làm việc đa dạng, công bằng và hòa nhập, nơi mọi người được trân trọng và kính trọng, đối xử bình đẳng bất kể sự khác biệt về nền văn hóa, giới tính, tuổi tác, tôn giáo, và khả năng\"",
            metadata={"topic": "đa dạng, bình đẳng, hòa nhập"},
        ),
        Document(
            page_content="TUYÊN NGÔN BỀN VỮNG: \"Cam kết của công ty với việc kinh doanh một cách bền vững, tôn trọng môi trường và tìm cách giảm thiểu tác động tiêu cực đến hành tỉnh.\"",
            metadata={"topic": "đa dạng, bình đẳng, hòa nhập"},
        ),
        Document(
            page_content="TUYÊN NGÔN AN TOÀN, SỨC KHỎE, MÔI TRƯỜNG: \"Khẳng định ưu tiên của công ty đối với việc bảo vệ an toàn, sức khỏe và môi tường của nhân viên tại nơi làm việc và ngoài cộng đồng. Nó thường bao gồm các chính sách và thủ tục cụ thể để đảm bảo an toàn, sức khoẻ và không gây hại cho môi trường\"",
            metadata={"topic": "đa dạng, bình đẳng, hòa nhập"},
        ),
        Document(
            page_content="TUYÊN NGÔN CAM KẾT VỚI KHÁCH HÀNG: \"Mô tả sự cam kết của công ty đối với việc cung cấp dịch vụ khách hàng xuất sắc và làm thế nào họ đáp ứng hoặc vượt qua kỳ vọng của khách hàng.\"",
            metadata={"topic": "đa dạng, bình đẳng, hòa nhập"},
        ),
        Document(
            page_content="""Vì sao cần tuyên ngôn? \"Các câu tuyên ngôn giúp làm rõ hơn các nguyên tắc và giá trị mà công ty hoạt động dựa trên chúng, cung cấp hướng dẫn cho nhân viên, và truyền đạt cam kết của công ty đến các bên liên quan như khách hàng, đối tác, và cộng đồng\"""",
            metadata={"topic": "vì sao cần tuyên ngôn"},
        ),
        Document(
            page_content="""Lợi ích của tuyên ngôn doanh nghiệp: \"
            - XÁC ĐỊNH ĐỊNH HƯỚNG, MỤC TIÊU, VÀ GIÁ TRỊ CỐT LÕI: Tạo ra sự thống nhất và hướng dẫn cho NV và những người liên quan về mục tiêu và giá trị của doanh nghiệp. 
            - THU HÚT NHÂN TÀI, KHÁCH HÀNG, ĐỐI TÁC, NHÀ ĐẦU TƯ, đặc biệt là những người chia sẻ các giá trị và mục tiêu của doanh nghiệp. Nó giúp tạo ra một ấn tượng mạnh mẽ và gây dựng lòng trung thành từ phía những người quan tâm. 
            - XÁC ĐỊNH VỊ TRÍ THỊ TRƯỜNG: Xác định và tạo ra một vị trí độc đáo trong thị trường. Nó cho phép doanh nghiệp tạo ra một hình ảnh và danh tiếng mạnh mẽ, giúp nó nổi bật giữa các đối thủ cạnh tranh.
            - GẮN KẾT NHÂN VIÊN: Câu tuyên ngôn cung cấp cho nhân viên một cái nhìn tổng thể về mục tiêu và giá trị của doanh nghiệp. Điều này giúp tạo ra sự đoàn kết và tinh thần làm việc trong tổ chức.
            - HƯỚNG DẪN RA QUYẾT ĐỊNH: Câu tuyên ngôn có thể hoạch định một khung nhìn và hướng dẫn cho các quyết định chiến lược của doanh nghiệp. Nó làm rõ những hành động và quyết định nào phù hợp với mục tiêu và giá trị cốt lõi của tổ chức.
            - GÂY DỰNG NIỀM TIN VÀ LÒNG TIN: Một câu tuyên ngôn mạnh mẽ có thể tạo ra sự tin tưởng và lòng tin từ phía khách hàng, nhà đầu tư và cộng đồng. Điều này giúp tăng cường uy tín và độ tin cậy của doanh nghiệp trong mắt công chúng.
            - TẠO ĐỘNG LỰC CHO NHÂN VIÊN: Khi NV hiểu rõ mục tiêu và giá trị mà doanh nghiệp hướng đến thông qua câu tuyên ngôn, họ cảm thấy được động viên và cam kết hơn trong công việc hàng ngày của mình.
            - TẠO ĐIỂM NHẤN CHO CHIẾN LƯỢC MARKETNG: Là một phần quan trọng của chiến lược marketing của doanh nghiệp. Nó giúp tạo ra thông điệp mạnh mẽ và dễ nhớ cho sản phẩm dịch vụ, từ đó thu hút và giữ chân khách hàng.
            - ĐỊNH HÌNH VĂN HÓA TỔ CHỨC: Là nền móng của văn hóa tổ chức. Nó không chỉ nêu bật mục tiêu và giá trị của doanh nghiệp mà còn giúp xây dựng và định hình cách NV làm việc và tương tác trong tổ chức.
            - TẠO SỰ KHÁC BIỆT & LỢI THẾ CẠNH TRANH: Câu tuyên ngôn độc đáo và phù hợp có thể giúp doanh nghiệp tạo ra sự khác biệt với đối thủ cạnh tranh. Nó giúp nâng cao nhận thức về thương hiệu và tạo ra một ấn tượng đặc biệt trong tâm trí của khách hàng.
            - THÚC ĐẨY SÁNG TẠO VÀ ĐỔI MỚI: Câu tuyên ngôn có thể là một nguồn cảm hứng và khuyến khích sự sáng tạo và đổi mới trong tổ chức. Nó có thể khuyến khích nhân viên tìm kiếm cách tiếp cận mới và tưởng tượng về cách thức thực hiện mục tiêu và giá trị của doanh nghiệp.
            \"""",
            metadata={"topic": "lợi ích của tuyên ngôn doanh nghiệp"},
        ),
        Document(
            page_content="""Định nghĩa triết lý kinh doanh của một doanh nghiệp: \"Là những niềm tin hoặc nguyên tắc nền tảng, làm định hướng cho cách thức kinh doanh của doanh nghiệp, bao gồm thái độ của công ty đối với khách hàng, nhân viên, đối tác, các bên liên quan và mục đích tổng thể của nó.\"""",
            metadata={"topic": "định nghĩa triết lý kinh doanh"},
        ),
        Document(
            page_content="""Triết lý kinh doanh của doanh nghiệp Bao Bì Ánh Sáng: 
            \"Chúng tôi quan niệm rằng bao bì không đơn giản là vỏ bọc của sản phẩm. Bao bì phải thực hiện 3 vai trò quan trọng: 
            - Là lá chắn bảo vệ an toàn cho sản phẩm
            - Là giải pháp thuận tiện cho việc bốc xếp, vận chuyển, lưu kho
            - Là diện mạo và hình ảnh của thương hiệu. 
            Bao Bì Ánh Sáng không kinh doanh bao bì đơn thuần. Chúng tôi trao giá trị vượt trội cho khách hàng bằng các giải pháp tối ưu trong bảo vệ sản phẩm, trong bốc xếp, vận chuyển, lưu kho, và góp phần nâng tầm thương hiệu.\"""",
            metadata={"topic": "triết lý kinh doanh của Bao Bì Ánh Sáng"},
        ),
        Document(
            page_content="""Định nghĩa sứ mệnh của một doanh nghiệp: \"Là tuyên bố về mục đích của tổ chức, lý do tồn tại; là tuyên ngôn về mục đích cốt lõi và trọng tâm của tổ chức và thường không thay đổi theo thời gian\"""",
            metadata={"topic": "định nghĩa sứ mệnh"},
        ),
        Document(
            page_content="""sứ mệnh của Bao Bì Ánh Sáng: \"Đồng hành đem lại sự thịnh vượng cho khách hàng thông qua các giải pháp bao bì, đóng gói tiên tiến và hiệu quả, không chỉ giúp bảo vệ an toàn sản phẩm, đem lại sự thuận tiện trong bốc xếp, vận chuyển, lưu kho, mà còn hỗ trợ đắc lực khách hàng nâng tầm hình ảnh thương hiệu.\"""",
            metadata={"topic": "sứ mệnh của Bao Bì Ánh Sáng"},
        ),
        Document(
            page_content="""Định nghĩa tầm nhìn của một doanh nghiệp: \"Tầm nhìn là viễn cảnh, mục tiêu lâu dài, là ước muốn về tương lai xa của tổ chức;\"""",
            metadata={"topic": "định nghĩa tầm nhìn"},
        ),
        Document(
            page_content="""tầm nhìn của Bao Bì Ánh Sáng: \"Trở thành doanh nghiệp hàng đầu Việt Nam và khu vực trong lĩnh vực bao bì, đóng gói, là lựa chọn ưu tiên nhất, tin cậy nhất của khách hàng trong lĩnh vực này.\"""",
            metadata={"topic": "tầm nhìn của Bao Bì Ánh Sáng"},
        ),
        # Document(
        #     page_content="""những điều quan trọng, rất được coi trọng tại Bao Bì Ánh Sáng hoặc giá trị cốt lõi của Bao Bì Ánh Sáng: \"
        #     TRÁCH NHIỆM: 'Trách nhiệm với công việc, Trách nhiệm với khách hàng, đối tác, nhà cung cấp, người lao động, Trách nhiệm với cổ đông, nhà đầu tư, cơ quan chức năng và các bên liên quan khác. Trách nhiệm với công ty, cấp trên, cấp dưới, đồng nghiệp. Trách nhiệm với mục tiêu, kế hoạch, thời hạn hoàn thành và các cam kết thực hiện. Trách nhiệm với lời nói và việc làm. Trách nhiệm với kết quả.'
        #     TẬN TÂM: 'Hiểu ý khách hàng, đối tác, đồng nghiệp, cấp trên, cấp dưới... Hợp tác, hỗ trợ, tư vấn, giải thích, xử lý đến nơi, đến chốn. Thể hiện tinh thần trách nhiệm cao. Tự giác, tự nguyện, nhiệt tình, vui vẻ, tận tụy. Lường trước khó khăn của đồng nghiệp, khách hàng để giúp họ tránh được khó khăn. Luôn đặt mục tiêu thách thức để chinh phục.'
        #     CAM KẾT: 'Cam kết với mục tiêu. Cam kết với deadline. Cam kết với khách hàng, đối tác, nhà cung cấp... Cam kết với nội bộ (cấp trên, cấp dưới, đồng nghiệp). Hứa và giữ lời hứa.'
        #     CHÍNH TRỰC: 'Trung thực: Thành thật, không gian dối, lừa lọc. Liêm chính: Không gian lận, trục lợi, tư túi, trộm, cắp tài sản, tiền bạc. Đạo đức: Sống theo các giá trị tốt đẹp, phổ quát của nhân loại, coi trọng đạo lý, hành xử nhân nghĩa, nhân bản, nhân văn. Ngay thẳng: Không lươn lẹo, lấp liếm, lèo lá, bất minh, bất chính. Tử tế: Sống tốt, sống có tình người, sẵn lòng giúp đỡ người khác trong khả năng có thể.'
        #     SÁNG TẠO: 'Chủ động, sáng tạo trong công việc; Liên tục nghĩ cách cải tiến, nâng cấp tư duy và đề xuất ý tường mới; Sáng tạo trong sản xuất, tiếp thị, bán hàng, giao hàng, phục vụ và chăm sóc khách hàng; Sáng tạo trong phương pháp quản lý; Chủ động suy nghĩ đề ra giải pháp cho những vẫn đề gặp phải; Luôn đặt câu hỏi và tự trả lời: "Liệu có cách nào khác tốt hơn không?".'
        #     ĐỒNG ĐỘI: 'Mục tiêu: Luôn nghĩ đến mục tiêu chung; Quá trình: Thống nhất và tôn trọng quá trình, quy trình, quy định, kế hoạch, deadline; Giao tiếp: Giao tiếp rõ ràng, hiệu quả, giúp đồng đội hiểu rõ ý mình và tìm cách hiểu rõ đồng đội; Tham gia: Tham gia nhiệt tình, vui vẻ, phân công rõ ràng trách nhiệm, không chồng chéo, không bỏ sót nhiệm vụ; Cam kết: Cam kết với mục tiêu và thể hiện tinh thần trách nhiệm cao; Tin tưởng vào đồng đội; Hợp tác, hỗ trợ lẫn nhau trong công việc, nhắc nhờ nhau thực hiện các cam kết; Thân thiện, gần gũi, chào hỏi vui vẻ; Cởi mở, trao đổi cởi mở, không để bụng những điều không hài lòng về nhau; Chân tình, thành thật và tình cảm với nhau, thiện chí, thể hiện ý tốt.'
        #     BIẾT ƠN: 'Biết ơn khách hàng. Biết ơn đối tác, nhà cung cấp. Biết ơn nhà đầu tư, cổ đông đồng hành. Biết ơn cấp trên, cấp dưới, đồng nghiệp. Biết ơn thiên nhiên, môi trường sống, cộng đồng. Biết ơn những hành động tốt dù rất nhỏ mà người khác làm cho mình.'
        #     \"""",
        #     metadata={"topic": "những điều quan trọng, rất được coi trọng tại Bao Bì Ánh Sáng hoặc giá trị cốt lõi của Bao Bì Ánh Sáng"},
        # ),
        Document(
            page_content="""Giá trị cốt lõi(GTCL) của Bao Bì Ánh Sáng: \"
            1. TRÁCH NHIỆM: 
            - Trách nhiệm với công việc
            - Trách nhiệm với khách hàng, đối tác, nhà cung cấp, người lao động
            - Trách nhiệm với cổ đông, nhà đầu tư, cơ quan chức năng và các bên liên quan khác. 
            - Trách nhiệm với công ty, cấp trên, cấp dưới, đồng nghiệp. 
            - Trách nhiệm với mục tiêu, kế hoạch, thời hạn hoàn thành và các cam kết thực hiện. 
            - Trách nhiệm với lời nói và việc làm. Trách nhiệm với kết quả.
            2. TẬN TÂM: 
            - Hiểu ý khách hàng, đối tác, đồng nghiệp, cấp trên, cấp dưới... 
            - Hợp tác, hỗ trợ, tư vấn, giải thích, xử lý đến nơi, đến chốn. 
            - Thể hiện tinh thần trách nhiệm cao. 
            - Tự giác, tự nguyện, nhiệt tình, vui vẻ, tận tụy. 
            - Lường trước khó khăn của đồng nghiệp, khách hàng để giúp họ tránh được khó khăn. 
            - Luôn đặt mục tiêu thách thức để chinh phục.
            3. CAM KẾT: 
            - Cam kết với mục tiêu. 
            - Cam kết với deadline. 
            - Cam kết với khách hàng, đối tác, nhà cung cấp... 
            - Cam kết với nội bộ (cấp trên, cấp dưới, đồng nghiệp). Hứa và giữ lời hứa.
            4. CHÍNH TRỰC: 
            - Trung thực: Thành thật, không gian dối, lừa lọc. 
            - Liêm chính: Không gian lận, trục lợi, tư túi, trộm, cắp tài sản, tiền bạc. 
            - Đạo đức: Sống theo các giá trị tốt đẹp, phổ quát của nhân loại, coi trọng đạo lý, hành xử nhân nghĩa, nhân bản, nhân văn. 
            - Ngay thẳng: Không lươn lẹo, lấp liếm, lèo lá, bất minh, bất chính. 
            - Tử tế: Sống tốt, sống có tình người, sẵn lòng giúp đỡ người khác trong khả năng có thể.
            5. SÁNG TẠO: 
            - Chủ động, sáng tạo trong công việc
            - Liên tục nghĩ cách cải tiến, nâng cấp tư duy và đề xuất ý tường mới
            - Sáng tạo trong sản xuất, tiếp thị, bán hàng, giao hàng, phục vụ và chăm sóc khách hàng
            - Sáng tạo trong phương pháp quản lý
            - Chủ động suy nghĩ đề ra giải pháp cho những vẫn đề gặp phải
            - Luôn đặt câu hỏi và tự trả lời: "Liệu có cách nào khác tốt hơn không?".
            6. ĐỒNG ĐỘI: 
            - Mục tiêu: Luôn nghĩ đến mục tiêu chung
            - Quá trình: Thống nhất và tôn trọng quá trình, quy trình, quy định, kế hoạch, deadline
            - Giao tiếp: Giao tiếp rõ ràng, hiệu quả, giúp đồng đội hiểu rõ ý mình và tìm cách hiểu rõ đồng đội
            - Tham gia: Tham gia nhiệt tình, vui vẻ, phân công rõ ràng trách nhiệm, không chồng chéo, không bỏ sót nhiệm vụ
            - Cam kết: Cam kết với mục tiêu và thể hiện tinh thần trách nhiệm cao
            - Tin tưởng vào đồng đội
            - Hợp tác, hỗ trợ lẫn nhau trong công việc, nhắc nhờ nhau thực hiện các cam kết
            - Thân thiện, gần gũi, chào hỏi vui vẻ
            - Cởi mở, trao đổi cởi mở, không để bụng những điều không hài lòng về nhau
            - Chân tình, thành thật và tình cảm với nhau, thiện chí, thể hiện ý tốt.
            7.BIẾT ƠN: 
            - Biết ơn khách hàng
            - Biết ơn đối tác, nhà cung cấp. 
            - Biết ơn nhà đầu tư, cổ đông đồng hành. 
            - Biết ơn cấp trên, cấp dưới, đồng nghiệp. 
            - Biết ơn thiên nhiên, môi trường sống, cộng đồng. 
            - Biết ơn những hành động tốt dù rất nhỏ mà người khác làm cho mình.'
            \"""",
            metadata={"topic": "giá trị cốt lõi(GTCL) của Bao Bì Ánh Sáng"},
        ),
        Document(
            page_content="""Vì sao Tổ chức cần có Giá Trị Cốt Lõi(GTCL)? \"
            Câu trả lời đơn giản là để "dẫn dắt Hành vi của Tổ chức", là Kim chỉ nam trong "mọi Hành động" của tất cả nhân viên trong Tổ chức đó và xa hơn là thứ hoàn toàn có thể "Nói" với Khách hàng (Khách hàng, Đối tác, Nhân viên, Xã hội) như là "một Lời hứa Thương hiệu", là thứ khác biệt giữa Tổ chức này và Tổ chức khác. Đây được xem như là một "Phẩm chất bên trong" của một Tổ chức, là thứ Bất biến, không thay đổi theo Thời gian thì mới được gọi là Giá trị Cốt lõi.
            Không có "Giá trị Cốt lõi" để dẫn dắt hành vi thì Tổ chức đấy rất dễ bị lạc lối và khó tồn tại lâu dài, vì các cấp Nhân viên hành động không theo một cách thống nhất, hoặc chỉ Hành động theo Lợi ích của mình hoặc của một phòng Ban mình, mỗi người hành động không theo một Nguyên tắc nào. Và chắc chắn khi đó thì những giá trị đó không được gọi là Giá trị Cốt lõi.
            Khi công ty bắt đầu lớn lên, có nhiều phòng ban, có nhiều nhân viên (trên 30 người, ở các công ty không thâm hụt lao động nghề lớn) thì việc có một Hệ giá trị cốt lõi (tối đa 6 giá trị) là điều kiện cần để đưa công ty đi xa. Và ở công ty đó, nhân viên được "hoàn toàn An toàn" nếu Hành động theo các Giá trị cốt lõi mà không phải lo ngại hay sợ bị sa thải hay khiển trách, mà trái lại còn được Tuyên dương, được xem là một trong số những phẩm chất quan trọng để xét xem nhân viên đó có phải là "Hiền tài" của Tổ chức hay không? Những nhân viên "thường xuyên" vi phạm các Giá trị cốt lõi sớm hay muộn rồi thì cũng không thể tồn tại hay làm lâu trong Tổ chức đó. Vậy nên tại sao lại có sự chia tay, một số người trong Tổ chức (hoặc một Group) lại tách ra và thành lập một Tổ chức mới, thể hiện các Giá trị, các Niềm tin chung mà người ta hay gọi là "cùng Hệ giá trị"?
            Theo Jim Collins, "Giá trị cốt lõi" là những giá trị Bên trong mà Tổ chức đó Tin tưởng và Kiên trì theo đuổi, cho dù hoàn cảnh bên ngoài có thay đổi hoặc gây bất lợi".
            Nêu ra một Danh sách các Giá trị mà Tổ chức đó Tin tưởng thì không khó (vì có những Giá trị chung củaXã hội mà ai cũng Tin là nó đúng đắn), nhưng nó chỉ được gọi là Giá trị Cốt lõi khi Tổ chức đó "Kiên trì theo đuổi" ngày này theo tháng nọ, không phải bằng lời nói suông, mà bằng Hành động cụ thể để bảo vệ Giá trị đó, cho dù có đánh đổi bằng rất rất nhiều tiền gây thiệt hại lớn về Kinh tế, Cơ hội. Việc này phải được thực hiện xuyên suốt trong toàn bộ Tổ chức, đặc biệt là các cấp quản lý cần hiểu, nắm rõ, vận dụng và "Làm gương" cho cấp dưới (vì sẽ chắc chắn có làm sai, hiểu sai tinh thần của Giá trị cốt lõi khi không được truyền thông thường xuyên hoặc không được thực hiện nghiêm túc bởi toàn bộ CB-CNV trong Tổ chức đó). Điều này không phải dễ và cần một quyết tâm, một sự kiên trì dài lâu. Tuy nhiên, nếu làm được thì lợi ích lâu dài mang lại là cực lớn. Lấy ví dụ một Tổ chức lấy "Tính Cam kết" làm Giá trị Cốt lõi của mình, được Định nghĩa, Truyền thông, in ra treo đầy trong công ty và thường xuyên được chính Ban Giám đốc thực hiện theo, có mô tả như sau:
            + Chúng tôi cam kết mang đến Sản phẩm và Dịch vụ chất lượng, có lợi ích, mang lại giá trị Ứng dụng Thực tế và Giải quyết vấn đề của Khách hàng.
            + Chúng tôi thực hiện đúng Cam kết với Khách hàng, Đối tác, Cổ đông và Nhân viên về các Thoả thuận đã được Thống nhất.
            Có nghĩa là khi làm ăn với công ty này, Khách hàng có thể nhận được Sự Đảm bảo 100%, Sự An tâm không chỉ là về chất lượng sản phẩm, về những cam kết ban đầu mà còn là chịu trách nhiệm cho đến khi Giải quyết được vấn đề của Khách hàng và đặc biệt là những sản phẩm cung cấp phải mang lại giá trị ứng dụng thực tế. Vì vậy, Giá trị Cốt lõi của Tổ chức thực sự là một Lời hứa, một "Lời hứa xây dựng nên Thương Hiệu", cần được thực hiện nghiêm túc, không chỉ một lần mà xuyên suốt mãi mãi trong quá trình Tồn tại của Tổ chức.
            \"""",
            metadata={"topic": "Vì sao Tổ chức cần có Giá Trị Cốt Lõi(GTCL) ?"},
        ),
        Document(
            page_content="""lý tưởng của Bao Bì Ánh Sáng: \"
            Dẫn dắt và giúp đỡ tất cả các thành viên trong công ty có một cuộc sống hạnh phúc và một cuộc đời ý nghĩa. Trong khả năng và tầm ảnh hưởng của doanh nghiệp, làm cho thế giới này trở nên tốt đẹp hơn.
            \"""",
            metadata={"topic": "lý tưởng của Bao Bì Ánh Sáng"},
        ),
        Document(
            page_content="""trách nhiệm của Bao Bì Ánh Sáng: \"
            Mang lại cơm no áo ấm, đời sống sung túc cho toàn thể anh chị em công nhân viên. Xây dựng một môi trường làm việc hoàn thiện để khai phá và phát triển con người ở mức cao nhất. Dựa vào con người, tạo ra những sản phẩm và dịch vụ chất lượng nhằm đem đến giá trị thực sự cho khách hàng, cho cộng đồng, cho xã hội.
            \"""",
            metadata={"topic": "trách nhiệm của Bao Bì Ánh Sáng"},
        ),
        Document(
            page_content="""lợi thế cạnh tranh từ năng lực cốt lõi(NLCL): \"
            Giả sử, trong 100 người bán, tất cả đều cam kết mang đến những sản phẩm chất lượng, với mức giá cạnh tranh. Tuy nhiên, thực tế chỉ có 50 doanh nghiệp thực hiện đúng cam kết. Trong 50 doanh nghiệp đó, chỉ có 10 doanh nghiệp mang đến những trải nghiệm thực tế vượt trội cho khách hàng. Khi đó, 10 doanh nghiệp này đang có nhiều lợi thế cạnh tranh so với các doanh nghiệp khác, lẽ đương nhiên, cơ hội các doanh nghiệp đó bán được hàng cũng sẽ cao hơn, thu nhập và các chế độ phúc lợi cho nhân viên của họ cũng tốt hơn nhiều số còn lại.
            Vậy, tại sao 10 doanh nghiệp đó có được lợi thế cạnh tranh còn 90 doanh nghiệp còn lại thì không?
            Sự khác biệt nằm ở năng lực cốt lõi. Năng lực cốt lõi được hiểu ở đây phải được lựa chọn phù hợp với đặc thù doanh nghiệp. Đó phải là những ưu thế, giá trị tốt nhất doanh nghiệp có thể mang đến cho khách hàng. Trong ví dụ trên, 10 doanh nghiệp có lợi thế cạnh tranh đã lựa chọn và mang đến cho khách hàng những ưu thế thực sự, gắn liền với năng lực của họ. Đảm bảo các yếu tố:
            1. Sự phù hợp: năng lực cốt lõi phải phù hợp với mong muốn của khách hàng. Biểu hiện:
            - Chủ động tìm hiểu nhu cầu thị trường và đáp ứng nhu cầu của khách hàng
            - Không ngừng học tập, đào tạo và phát triển kiến thức, kỹ năng đảm bảo thực hiện đúng
            và đủ các năng lực cốt lõi. Vì, như đã đề cập bên trên, trong kỷ nguyên của trải nghiệm, mong muốn của khách hàng không ngừng được nâng cao, yêu cầu với sản phẩm cũng ngày càng cao hơn. Đồng nghĩa, doanh nghiệp nào không thể đáp ứng nhu cầu của khách hàng, doanh nghiệp đó hoàn toàn không có cơ hội để bán được hàng.
            2. Tính duy nhất: Năng lực cốt lõi cần có tính duy nhất, không bị sao chép hoặc tái tạo dễ
            dàng bởi các công ty khác. Chúng giúp tăng khả năng nhận biết, phân biệt và lựa chọn doanh nghiệp so với các đối thủ cạnh tranh.
            3. Tính bền vững: năng lực cốt lõi phải luôn được giữ vững và phát huy được hiệu quả trong
            suốt quá trình phát triển của tổ chức.
            \"""",
            metadata={"topic": "lợi thế cạnh tranh từ năng lực cốt lõi(NLCL)"},
        ),
        Document(
            page_content="""khái niệm năng lực cốt lõi(NLCL): \"
            Năng lực cốt lõi là cơ sở tạo ra lợi thế cạnh tranh. Từ đó, định hướng phát triển và tăng trưởng lợi nhuận, góp phần tạo nên môi trường làm việc và mức thu nhập tốt hơn cho toàn thể nhân viên.
            \"""",
            metadata={"topic": "khái niệm năng lực cốt lõi(NLCL)"},
        ),
        Document(
            page_content="""mối quan hệ giữa năng lực cốt lõi(NLCL) và giá trị cốt lõi(GTCL): \"
            Nếu ví doanh nghiệp như một ngôi nhà thì giá trị cốt lõi là nền móng vững chắc ban đầu nhằm hình thành và định hướng bộ khung các năng lực cốt lõi của doanh nghiệp, hướng đến xây dựng và hoàn thành mái nhà chung (sứ mệnh, tầm nhìn).
            - Sứ mệnh là nhiệm vụ lâu dài, và là LÝ DO TỒN TẠI của tổ chức/ doanh nghiệp.
            - Tầm nhìn là MỤC TIÊU mà doanh nghiệp muốn hướng đến.
            - Giá trị cốt lõi ("GTCL") là những nguyên tắc và niềm tin của tổ chức, là nền tảng định hướng toàn thể thành viên của tổ chức cùng nhau thực hiện và đạt được kết quả chung.
            \"""",
            metadata={"topic": "khái niệm năng lực cốt lõi(NLCL)"},
        ),
        Document(
            page_content="""5 năng lực cốt lõi(NLCL) của Bao Bì Ánh Sáng: \"
            1. Đa dạng mẫu mã - giá cả cạnh tranh:
            Đa dạng mẫu mã: 
            'Đa dạng loại hình sản phẩm và đa dạng phân khúc bán hàng. Liên tục cung cấp hàng loạt các loại sản phẩm đa dạng với nhiều kích thước, hình dạng và chất liệu khác nhau. Không chỉ sản xuất bao bì, định hướng đa dạng hóa nhiều sản phẩm hơn như túi xách, tấm cách nhiệt,...
            Với mỗi loại sản phẩm, tăng khả năng sản xuất và cung ứng cho nhiều ngành, từ thực phẩm, vật liệu xây dựng, hóa chất, .... Đáp ứng được nhu cầu đa dạng của khách hàng và tạo ra giải pháp sản phẩm tối ưu cho mỗi ngành.
            Chủ động tìm hiểu và đáp ứng nhu cầu của khách hàng (ngay cả khi khách chưa phát sinh nhu cầu trên thực tế), đáp ứng nhu cầu đa dạng của khách hàng, tùy chỉnh mẫu mã theo yêu cầu của khách, từ cấu trúc tiêu chuẩn đến cấu trúc đặc biệt. Nắm bắt được nhu cầu thị trường và chủ động nghiên cứu, cải tiến nhằm tạo ra giải pháp sản xuất tối ưu cho khách hàng
            Thường xuyên nghiên cứu và phát triển các mẫu mã mới, đáp ứng xu hướng thị trường và nhu cầu khách hàng. Không ngừng đưa ra các giải pháp sáng tạo và độc đáo, tăng sự đa dạng mẫu mã nhằm thu hút khách hàng.'
            Giá cả cạnh tranh: 
            'Xây dựng và hiệu chuẩn quy trình sản xuất nhằm tăng năng suất, tiết kiệm chi phí, 
            Quản lý chi phí (Cắt giảm tất cả chi phí thừa, không cần thiết), 
            Xây dựng chiến lược mua hàng hiệu quả (Tìm kiếm nhà cung cấp nguyên vật liệu giá tốt, đáp ứng thời gian công nợ nhưng vẫn đảm bảo chất lượng đầu vào), 
            Tối ưu chi phí thông qua cải tiến và sử dụng công nghệ nhằm tăng năng suất và giảm chi phí sản xuất. Những điều này giúp họ cung cấp sản phẩm bao bì với giá cả cạnh tranh so với các đối thủ khác.'
            2. Chất lượng đảm bảo:
            Thực hiện quy trình kiểm soát chất lượng từ quá trình nhập nguyên vật liệu, thiết kế, sản xuất đến giai đoạn đóng gói và giao hàng. Liên tục kiểm tra chất lượng định kỳ theo tần suất để đảm bảo rằng sản phẩm đáp ứng được các yêu cầu kỹ thuật, chất lượng bền và an toàn cho sản phẩm bên trong.
            Đào tạo và xây dựng đội ngũ kiểm soát chất lượng có kinh nghiệm và tay nghề cao. Thường xuyên tiến hành kiểm tra mẫu ngẫu nhiên, đánh giá các thông số kỹ thuật và liên tục kiểm soát, hướng dẫn, cảnh báo về chất lượng sản phẩm.
            Thiết lập và thực hiện hệ thống quản lý chất lượng nghiêm ngặt theo tiêu chuẩn ISO 9001 để đảm bảo rằng sản phẩm đáp ứng được yêu cầu chất lượng và an toàn cho khách hàng.
            Cải tiến và sử dụng công nghệ nhằm đo lường chính xác và đảm bảo chất lượng tốt nhất.
            Tiếp nhận phản hồi và cải tiến liên tục: luôn lắng nghe phản hồi từ khách hàng và sử dụng thông tin thu được nhằm nâng cao chất lượng sản phẩm.
            3. Tiến độ vượt trội:
            Cung cấp tiến độ sản xuất nhanh nhất trong khả năng, đáp ứng nhu cầu của khách hàng. Quản lý và hiệu chuẩn quy trình quản lý sản xuất, thiết lập kế hoạch và liên tục bám sát mục tiêu nhằm đảm bảo rằng mọi đơn đặt hàng đều được hoàn thành đúng hạn. Đào tạo, xây dựng đội ngũ quản lý chuyên nghiệp và có kinh nghiệm, có khả năng lập kế hoạch và điều phối công việc hiệu quả. Liên tục theo dõi tiến độ sản xuất, quản lý tài nguyên và tương tác với các bộ phận khác nhằm đảm bảo rằng tiến độ luôn được duy trì và ngày càng vượt trội hơn.
            Nghiên cứu cải tiến và ứng dụng công nghệ vào sản xuất để tăng năng suất và đạt được hiệu quả cao hơn. Tăng khả năng xử lý các đơn hàng lớn và phức tạp một cách hiệu quả, giúp tạo nên ưu thế vượt trội về tiến độ so với các đối thủ cạnh tranh.
            4. Thiết kế đẹp và ấn tượng số 1 ngành bao bì:
            Thiết kế độc đáo và sáng tạo: 'Tuyển dụng, đào tạo đội ngũ thiết kế chuyên nghiệp và tài năng, có khả năng tạo ra các thiết kế độc đáo và sáng tạo. Thiết kế chỉ đẹp thôi chưa đủ, thiết kế của BBAS phải tạo được ấn tượng số 1, thông qua: Bắt kịp xu hướng thị trường, tìm hiểu kỹ thuật và xu hướng thiết kế mới nhất nhằm áp dụng vào sản phẩm. Nghiên cứu và đưa ra các giải pháp thiết kế đột phá để tạo nên sự khác biệt. Tận dụng các yếu tố thiết kế như màu sắc, hình ảnh và font chữ để tạo nên sự ấn tượng và tăng tính nhận diện thương hiệu. Đảm bảo rằng bao bì của khách hàng sẽ nổi bật và gây ấn tượng tốt đến khách hàng cuối cùng. Sử dụng công nghệ và công cụ thiết kế hiện đại để tạo ra sản phẩm với các hình ảnh sắc nét, màu sắc và chất liệu đẹp, ấn tượng số 1.'
            Chất lượng thiết kế cao cấp (khẳng định vị thế số 1 ngành bao bì): 'Thiết kế của BBAS không chỉ tập trung vào tính thẩm mỹ mà còn đảm bảo tính khả thi và hiệu quả trong việc bảo vệ sản phẩm, tạo ấn tượng và giá trị cho thương hiệu. Thiết kế phù hợp với nhu cầu và mong muốn của khách hàng, đảm bảo bao bì đáp ứng được yêu cầu kỹ thuật và bảo vệ, chứa đựng sản phẩm an toàn, tiện lợi. Tạo ấn tượng và là giải pháp cho diện mạo của thương hiệu. Hiểu rõ tầm quan trọng của bao bì trong việc tạo dựng và thể hiện thương hiệu của khách hàng. Thông qua thiết kế, truyền tải các giá trị và thông điệp thương hiệu của khách hàng.'
            Với năng lực cốt lõi "Thiết kế đẹp và ấn tượng số 1 ngành bao bì", BBAS tạo ra những giải pháp thiết kế độc đáo và sáng tạo, đáp ứng nhu cầu của khách hàng trong việc tạo dựng thương hiệu và tăng cường giá trị thương hiệu thông qua bao bì.
            5. Tạo sự an tâm bằng tinh thần phục vụ, trách nhiệm và uy tín:
            Tận tâm phục vụ: 'Tuyển dụng, đào tạo đội ngũ nhân viên tận tâm và chuyên nghiệp. Luôn sẵn sàng lắng nghe và đáp ứng nhu cầu của khách hàng, đồng thời cung cấp giải pháp tốt nhất cho các yêu cầu của khách. Nắm rõ và thực hiện nguyên tắc lấy khách hàng là trung tâm, luôn đảm bảo rằng mọi yêu cầu và mong muốn của khách hàng được đáp ứng đúng hẹn và chất lượng.'
            Uy tín và trách nhiệm: 'Xây dựng uy tín thông qua việc luôn tuân thủ các cam kết. Hướng dẫn, đào tạo nhân viên tuân theo các quy tắc đạo đức, đảm bảo tính trung thực, không gian dối, luôn tuân thủ đúng các quy định và tiêu chuẩn. Đảm bảo các thông tin liên quan đến sản phẩm và quy trình sản xuất được cung cấp một cách minh bạch và chính xác cho khách hàng. Đồng thời, bảo đảm yếu tố bảo mật thông tin cho khách, tạo dựng sự tin tưởng và an tâm khi sử dụng sản phẩm của công ty.'
            Với năng lực cốt lõi "Tạo dựng sự an tâm bằng tinh thần phục vụ trách nhiệm và uy tín", công ty thể hiện sự cam kết, tận tâm phục vụ và tuân thủ các nguyên tắc đạo đức, từ đó, xây dựng một hình ảnh đáng tin cậy và uy tín trong ấn tượng của khách hàng về BBAS.
            \"""",
            metadata={"topic": "5 năng lực cốt lõi(NLCL) của Bao Bì Ánh Sáng"},
        ),
    ]
    return docs