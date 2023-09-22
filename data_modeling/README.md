Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

## 1. Farmers' Market Expansion
<p>You have been hired by a farming organisation that helps local farmers sell their products. They want to know whether they should open up a new farmers' market to sell dairy products from nearby farmers. They have supplied you with daily shopping data from a panel of local households from 2019 to 2020. </p>
<p>The organization will make their decision based on whether dairy products are popular in the area, and whether sales are trending in a positive direction. To answer these questions, they want three pieces of data:</p>
<ol>
<li>What was the total number of purchases of dairy products for each month of 2020 (i.e., the <code>total_sales</code>)?</li>
<li>What was the total share of dairy products (out of all products purchased) for each month of 2020 (i.e., the <code>market_share</code>)?</li>
<li>For each month of 2020, what was the percentage increase or decrease in total monthly dairy purchases compared to the same month in 2019 (i.e., the <code>year_change</code>)?</li>
</ol>
<p>The organization handles not only dairy farmers, but also those with chicken farms. As a result, they are only interested in these three categories (which they treat as dairy): ‘whole milk’, 'yogurt' and 'domestic eggs'.</p>
<p>The data you need is available in the tables shown in the database schema below.</p>
<h5 id="databaseschema">Database Schema</h5>
<p><img src="https://assets.datacamp.com/production/repositories/5960/datasets/463543c8c38957ca5b95d93b02f2cb1bec53334f/diagram.PNG" alt="Database Schema" width="400px"></p>