WITH final AS(
    SELECT
        article_key::TEXT AS article_key,
        category::TEXT AS category,
        headline::TEXT AS headline,
        short_description::TEXT AS short_description,
        COALESCE(keywords, 'Unknown') AS keywords,
        {{ at_date('release_date') }} AS release_date
    FROM {{ ref('news_articles')}}
)
SELECT *
FROM final
