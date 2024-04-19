SELECT * FROM challenge.employee;
-- 과제 데이터 생성
CREATE DATABASE challenge 
USE challenge
-- 1번문제  employee 테이블을 생성하고 id, name, position, salary 컬럼 만들기
CREATE TABLE employee(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
position VARCHAR(100),
salary DECIMAL(10,2)
)
-- 2번문제 직원데이터 추가  
INSERT INTO employee (name, position, salary) VALUES
('혜린', 'PM', 90000),
('은우', 'Frontend', 80000),
('가을', 'Backend', 92000),
('지수', 'Frontend', 78000),
('민혁', 'Frontend', 96000),
('하온', 'Backend', 30000);


