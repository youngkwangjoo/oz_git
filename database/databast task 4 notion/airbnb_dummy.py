
import pymysql
connectanb = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'class-password',
    db = 'airbnb'
)

try: 
    with connectanb.cursor() as cursor:
        #cursor은 리소스를 안정적이게 해주는것? with문이 끝나면 close시켜준다?
        #새로운 제품 추가
        sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, ("Python Book", 29.99, 50))
        connectanb.commit()
        #execute는 커서의 메서드인데 쿼리를 실행하기 위해 사용. 
        # 문제 2: 고객 목록 조회
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
        #fetchall() 각 행의 값을 리스트형태로 튜플행을 가져온다.

        # 문제 3: 제품 재고 업데이트
        # products table에 alter table product , add column quantity_sold int로 추가 칼럼을 만듬
        sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(sql, (quantity_sold, product_id))
        connectanb.commit()

        # 문제 4: 고객별 총 주문 금액 계산
        sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

        # 문제 5: 고객 이메일 업데이트
        sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql, (new_email, customer_id))
        connectanb.commit()

        # 문제 6: 주문 취소
        sql = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql, (order_id,))
        #튜플을 생성하기위해 , 를 붙여서 변수를 넣음 만약 쉼표가없으면 튜플이 아니라 정수나 다른 형태로 받아들일수 있음
        connectanb.commit()

        # 문제 7: 특정 제품 검색
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql, ('%Book%',))
        for row in cursor.fetchall():
            print(row)

        # 문제 8: 특정 고객의 모든 주문 조회
        sql = "SELECT * FROM Orders WHERE customerID = %s"
        cursor.execute(sql, (1,))
        for row in cursor.fetchall():
            print(row)

        # 문제 9: 가장 많이 주문한 고객 찾기
        sql = """
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders 
        GROUP BY customerID 
        ORDER BY orderCount DESC 
        LIMIT 1
        """
        cursor.execute(sql)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer[0]}, Orders: {top_customer[1]}")

finally:
    connectanb.close()
