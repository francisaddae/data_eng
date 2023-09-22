WITH purchases_2019 AS(
    SELECT
        member_id,
        purchase_id,
        full_date AS purchase_date,
        year AS purchase_year,
        month AS purchase_month,
        day AS purchase_day,
        day_of_week AS purchase_week_day
    FROM {{ ref('farmers__purchases_2019')}}
),
purchases_2020 AS (
    --Cleaning up fact data to match purchases in 2019
    SELECT
        memberid AS member_id,
        purchaseid AS purchase_id,
        fulldate AS purchase_date,
        EXTRACT(YEAR FROM fulldate) AS purchase_year,
        EXTRACT(MONTH FROM fulldate) AS purchase_month,
        EXTRACT(DAY FROM fulldate) AS purchase_day,
        dayofweek AS purchase_week_day
    FROM {{ ref('farmers__purchases_2020')}}
),
final AS (
    SELECT *
    FROM purchases_2019

    UNION ALL

    SELECT *
    FROM purchases_2020
)
SELECT *
FROM final