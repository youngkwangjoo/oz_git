
-- pm직책을 가진 직원 연봉을 10%인상 후 결과 확인
update employee set salary = salary * 1.10 where id = 1;
SELECT * FROM employee WHERE position = 'congrate';
-- 백엔드 직책의 직원 연봉을 5퍼 인상하세요
SET SQL_SAFE_UPDATES = 0;
UPDATE employee SET salary = salary * 1.05 WHERE position = 'Backend';
ALTER TABLE employee ADD COLUMN congrate VARCHAR(100); 
-- 민혁사원 퇴사시키기
DELETE FROM employee WHERE name = '민혁';
-- 각 포지션 별 연봉구하기
SELECT position, AVG(salary) AS avg_salary
FROM employee
GROUP BY position;