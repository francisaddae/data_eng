
{% macro at_date(col) %}
    -- Convert text to date
    {{ col }}::DATE
{% endmacro %}

{% macro at_date_with_format(col, format_method) %}
    -- Cast a date into a string format, based on the notation given
    TO_CHAR({{ col }}::DATE, '{{ format_method }}' )
{% endmacro %}
