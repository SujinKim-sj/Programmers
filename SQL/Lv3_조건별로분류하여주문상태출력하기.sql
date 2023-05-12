-- String, Date LV3 - 조건별로 분류하여 주문상태 출력하기
-- 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회

SELECT ORDER_ID
    , PRODUCT_ID
    , TO_CHAR(OUT_DATE, 'YYYY-MM-DD') AS OUT_DATE
    , CASE WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') <= '2022-05-01' THEN '출고완료'
           WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') > '2022-05-01' THEN '출고대기'
           ELSE '출고미정' END AS "출고여부"
 FROM FOOD_ORDER
 ORDER BY ORDER_ID ASC