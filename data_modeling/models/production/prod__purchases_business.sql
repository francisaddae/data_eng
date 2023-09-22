WITH sales_info_2019 AS (
    SELECT
        p.purchase_month,
        COUNT(p.purchase_id) AS monthly_category_sale_2019
    FROM {{ ref('stg__purchases') }} AS p
    LEFT JOIN {{ ref('farmers__categories')}} AS c
        ON p.purchase_id = c.purchase_id
        AND c.category IN ('whole milk', 'yogurt' ,'domestic eggs')
        AND p.purchase_year = 2019
    GROUP BY p.purchase_month
),
sales_info_2020 AS (
    SELECT
        p.purchase_month,
        COUNT(p.purchase_id) AS monthly_category_sale_2020
    FROM {{ ref('stg__purchases') }} AS p
    LEFT JOIN {{ ref('farmers__categories')}} AS c
        ON p.purchase_id = c.purchase_id
        AND c.category IN ('whole milk', 'yogurt' ,'domestic eggs')
        AND p.purchase_year = 2020
    GROUP BY p.purchase_month
),
market_share AS (
    SELECT
        p.purchase_month,
        SUM( CASE WHEN p.purchase_year = 2019 THEN 1 ELSE 0 END) AS yearly_purchase_2019,
        SUM( CASE WHEN p.purchase_year = 2020 THEN 1 ELSE 0 END) AS yearly_purchase_2020
    FROM {{ ref('stg__purchases') }} AS p
    GROUP BY p.purchase_month
)
SELECT *
FROM market_share