
{% docs farmers__purchases_info_table %}
A consolidation of all farmers purchases that occured in 2019 and 2020
{% enddocs %}

{% docs farmers__member_id %}
Unique indentifier of the product being sold
{% enddocs %}

{% docs farmers_purchase_id %}
The purchases identifier used to purchase the product
{% enddocs %}

{% docs farmers__purchase_date %}
The complete purchases date of a particular transaction
{% enddocs %}

{% docs farmers__purchase_year %}
The purchases year in which the transaction took place
{% enddocs %}

{% docs farmers__purchase_month %}
The purchases month in which the transaction took place
{% enddocs %}

{% docs farmers__purchase_day %}
The purchases day in which the transaction took place
{% enddocs %}

{% docs farmers__purchase_week_day %}
The week day where a purchase was rendered. This is in number notation from 0-6.
- 0 : Sunday
- 1 : Monday
- 2 : Tuesday
- 3 : Wednesday
- 4 : Thursday
- 5 : Friday
- 6 : Saturday

{% enddocs %}

{% docs prod__dairy_farmers_purchases %}
A consolidation of all dairy farmers purchases that occured in 2019 and 2020 noting a monthly analysis, a market share per month and a yearly change per month
{% enddocs %}

{% docs prod__total_sales %}
count of all sales that took place within each month
{% enddocs %}

{% docs prod__market_sale %}
count of all diary products that took place each month over all the products sold per that month
{% enddocs %}

{% docs prod__yearly_change %}
difference in all diary products in that took place each month in 2019 and 2020 over all the diary products sold per that month in 2019
{% enddocs %}

{% docs stg__articles %}
A table containing all news articles published
{% enddocs %}

{% docs articles__article_key %}
A unique ID of a particular particle
{% enddocs %}

{% docs articles__category %}
Category of all article type. This various but most notably Sports, Food & Drink, Wellness, Lifestyle etc
{% enddocs %}

{% docs articles__headline %}
Caption of each individual article which garnered user's attention
{% enddocs %}

{% docs articles__subtitle %}
A descriptive summary of a new clipping ties into the headline message
{% enddocs %}

{% docs articles__description %}
The descriptions of each article and granular detail
{% enddocs %}

{% docs articles__keywords %}
Major key words found in the description of the articles pushed. These are usually in Bold, Italics or underlined font style.
{% enddocs %}

{% docs articles__release_date %}
The date which an article was published.
{% enddocs %}

{% docs prod__articles %}
This table focuses on news clippings published, which were written by a journalist with an ID of 1754
{% enddocs %}

{% docs prod__articles_key %}
Unique ID of each article, where the first 4 digits represents the journalist ID
{% enddocs %}

{% docs prod__category %}
Category of the article, in uppercase.  'Food & Drink' and 'Wellness' should be collapsed  into a 'Lifestyle' category.
{% enddocs %}

{% docs prod__headline %}
Headline of the article, without the subtitle that appears after the colon (:).  For example, 'It Could Happen To You: A Story of SEC Overreach' becomes 'It Could Happen To You'.
{% enddocs %}

{% docs prod__subtitle %}
Subtitles of the article, without the headline that appears before the colon (:). For example, 'It Could Happen to You: A Story of SEC Overreach' becomes 'A Story of SEC Overreach'. In cases where a headline does not have a subtitle, the missing value should read ‘None’.
{% enddocs %}

{% docs prod__description %}
Description of the article. The description should be reduced to the first sentence, up to and including the first period (.) from the short_description column.
{% enddocs %}

{% docs prod__keywords %}
Keywords of the article. Multiple keywords will be seperated with a dash (-). If the keyword is missing, the value should read ‘Unknown’.
{% enddocs %}

{% docs prod__publish_date %}
Date the article was published. The data should be displayed in the format resembling the following: ‘Aug 13, 1995’.
{% enddocs %}
