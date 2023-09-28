WITH sales_info_2019 AS (
    SELECT
        purchase_month,
        COUNT(purchase_id) AS total_purchase_2019
    FROM {{ ref('farmers')}}
    WHERE purchase_year = 2019
    GROUP BY purchase_month
    ORDER BY purchase_month
),sales_info_2020 AS (
    SELECT
        purchase_month,
        COUNT(purchase_id) AS total_purchase_2020
    FROM {{ ref('farmers')}}
    WHERE purchase_year = 2020
    GROUP BY purchase_month
    ORDER BY purchase_month
)
SELECT *
FROM sales_info_2019