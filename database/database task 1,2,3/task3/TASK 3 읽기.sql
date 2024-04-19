-- 프론트엔드 직원 이름과 연봉만 조회하기
SELECT name, salary FROM employee;
-- 프론트엔드에서 연봉 90000이하인 직원 이름과 연봉조회 
SELECT name, salary FROM employee WHERE position = 'Frontend' AND salary <= 90000;
-- pm직책을 가진 직원 연봉을 10%인상 후 결과 확인
update employee set salary = salary * 1.10 where id = 1;
SELECT * FROM employee WHERE position = 'congrate';
