-- SELECT LV4 - 서울에 위치한 식당 목록 출력하기

SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO A, REST_REVIEW B
WHERE A.REST_ID = B.REST_ID
 AND A.ADDRESS LIKE '서울%'
GROUP BY A.REST_ID
ORDER BY SCORE DESC, A.FAVORITES DESC