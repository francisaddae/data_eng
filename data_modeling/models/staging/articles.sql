WITH final AS(
    SELECT
        article_key::TEXT,
        category::TEXT,
        headline::TEXT,
        short_description::TEXT,
        COALESCE(keywords, 'Unknown') AS keywords,
        {{ at_date('release_date') }}
    FROM {{ ref('news_articles')}}
)
SELECT *
FROM final
