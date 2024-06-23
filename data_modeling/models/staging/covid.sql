
WITH raw_data AS (
    SELECT *
    FROM {{ source('datalake', 'covidData')}}
),
clean_data AS(
    SELECT
        index::INTEGER AS case_upload_id,
        COALESCE(date_of_interest,  '{{run_started_at.strftime("%Y-%m-%d")}}'  )::DATE AS date_of_interest,
        case_count::INTEGER AS case_count,
        probable_case_count::INTEGER AS death_count,
        hospitalized_count::INTEGER AS hospitalized_count

    FROM raw_data
),
final AS (
    SELECT
        case_upload_id,
        date_of_interest,
        case_count,
        death_count,
        hospitalized_count
    FROM clean_data
)
SELECT *
FROM final
