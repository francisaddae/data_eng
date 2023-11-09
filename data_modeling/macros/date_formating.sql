
{% macro at_date(col) %}
    -- Convert text to date
    {{ col }}::DATE
{% endmacro %}

{% macro at_date_with_format(col, format_method) %}
    -- Cast a date into a string format, based on the notation given
    TO_CHAR({{ col }}::DATE, '{{ format_method }}' )
{% endmacro %}

{% macro at_date_with_format_op_2(col, format_method) %}
    -- Another format used to format a date into a paritcular format
    to_date( {{ col }}::DATE, '{{ format_method }}')
{% endmacro %}
