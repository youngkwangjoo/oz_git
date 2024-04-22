-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
-- SET SQL_SAFE_UPDATES = 0;
DELETE FROM customers WHERE name = "주영광";
-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE product_name = "매화수";
-- (3) **`products`** 테이블에서 특정 직원을 삭제하세요.
DELETE FROM products WHERE name = "";
-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE office_name = "경기도 양주시 파천군";
-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE customers_id = "dudrknd1643";
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE name = "";
-- (7) **`orderdetails`** 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM orderdetails WHERE name = "";
-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE shampoo = "shampoo";
-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE name = "주영광";
-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE product_name = "이니스프리폼클렌징";