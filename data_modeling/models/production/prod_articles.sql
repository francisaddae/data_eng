WITH journal_data AS(
    SELECT
        article_key,
        UPPER(
            CASE
                WHEN category IN ('FOOD & DRINK', 'WELLNESS') THEN 'LIFESTYLE'
            ELSE category END
        ) AS category,
        CASE
            WHEN headline LIKE '%:%' THEN RIGHT(headline, STRPOS(headline, ':')-1)
            ELSE headline
        END AS headline,
        CASE
            WHEN headline LIKE '%:%' THEN RIGHT(headline, CHAR_LENGTH(headline) - STRPOS(headline, ':'))
            ELSE headline
        END AS subtitle,
        LEFT(short_description, STRPOS(short_description, '.')) AS description,
        CASE
            WHEN COALESCE(keywords, '') IN ('', 'None') THEN 'Unknown'
            ELSE keywords
        END AS keywords,
        {{ at_date_with_format('release_date', 'Mon dd, yyyy') }} AS publish_date
    FROM {{ ref('articles') }}
    WHERE release_date BETWEEN '2014-01-01' AND '2015-12-31'
        AND LEFT(article_key, 4) = '1754'
),
final AS (
    SELECT
        article_key,
        category,
        headline,
        subtitle,
        description,
        keywords,
        publish_date
    FROM journal_data
)
SELECT *
FROM final