WITH dairy_info_19 AS (
    -- Calculating all dairy purchased monthly in 2019
    SELECT
        f19.purchase_month,
        COUNT(f19.purchase_id) AS total_monthly_purchase_2019
    FROM {{ ref('farmers')}} AS f19
    LEFT JOIN {{ ref('farmers_categories')}} AS c
        ON f19.purchase_id = c.purchase_id
    WHERE f19.purchase_year = 2019
        AND c.category in ('whole milk', 'yogurt' ,'domestic eggs')
    GROUP BY f19.purchase_month
    ORDER BY f19.purchase_month
),sales_info_2020 AS (
    -- Calculating all products sold each month in 2020, alongside total market share of all products sold in 2020
    SELECT
        purchase_month,
        COUNT(f20.purchase_id) AS total_purchase_2020,
        SUM(CASE WHEN c.category IN ('whole milk', 'yogurt' ,'domestic eggs') THEN 1 ELSE 0 END) AS total_monthly_purchase_2020,
        ROUND(SUM(CASE WHEN c.category IN ('whole milk', 'yogurt' ,'domestic eggs') THEN 1 ELSE 0 END)*100::NUMERIC / COUNT(f20.purchase_id), 2) AS market_share
    FROM {{ ref('farmers')}} AS f20
    LEFT JOIN {{ ref('farmers_categories') }} AS c
        ON f20.purchase_id = c.purchase_id
    WHERE purchase_year = 2020
    GROUP BY purchase_month
    ORDER BY purchase_month
),
dairy_purchases_goods_2020 AS (
    SELECT
        s.purchase_month,
        s.total_monthly_purchase_2020 AS total_sales,
        s.market_share,
        ROUND((s.total_monthly_purchase_2020 - d.total_monthly_purchase_2019)*100::NUMERIC / d.total_monthly_purchase_2019, 2) AS yearly_change
    FROM sales_info_2020 AS s
    LEFT JOIN dairy_info_19 AS d
        ON s.purchase_month = d.purchase_month
),
final AS (
    SELECT
        purchase_month,
        total_sales,
        market_share,
        yearly_change
    FROM dairy_purchases_goods_2020
)
SELECT *
FROM final
