-- 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와 평균 대여 기간(컬럼명: AVERAGE_DURATION) 리스트를 출력
-- +1을 한 이유는 한 달에 31일인 달도 있기 때문

SELECT CAR_ID,
       ROUND(AVG(END_DATE - START_DATE + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVG(END_DATE - START_DATE + 1) >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC