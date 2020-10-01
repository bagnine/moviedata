# Movie Data Analysis for Profitability

**Authors**: David Shin, Nick Subic

## Overview

For this project, we've been prompted to gather and analyze data about the movie industry in order to find insights on what makes a movie studio successful.

## The Studio

Microsoft has decided to join other tech giants like Apple and Amazon by creating its own movie studio. Because it will be creating a new brand, Microsoft wants to produce market research to describe the making of a successful movie and translate that into a series of guidelines for reproducing that success.

## Data

For this project we were provided 4 datasets and we created a 5th using the internet-
* Box Office Mojo- This set includes both foreign and domestic gross sales but lacks any budget info. We largely passed over this set.
* IMDb- This massive database includes release information, titles, ratings and a wide variety of data about cast, crew and director. 
* Rotten Tomatoes- This set includes information about ratings, genre, and some box office numbers. Because it's notably lacking in titles, we were only able to gather correlary data and not join with the other databases.
* The Numbers- This set includes budgets plus foreign and domestic gross for a large number of movies. Because our company is motivated by profit, this set proved instrumental in calculating investment returns.
* Rotten Tomatoes (web scraped)- Because the provided RT data lacked titles and the ratings weren't normalized, we decided to pull the 'Freshness' percentage ratings directly from the website.

## Our Hypotheses

There is an optimum season to release movies, and we can break that down to month.

Some genres of movies are inherently more profitable than others. We can find out which, and use our findings to recommend content creation.

Budget is a predictor of which movies are most profitable. We can isolate a production budget window that is more likely to produce a good return.

Ratings are a driver for reviews, attention, press and word of mouth. We believe we can find a correlation between ratings and profitability, and if so, use that correlation to further explore the factors of a highly rated film using our other metrics.

## Methods

We believe the biggest determining factor in the success of a movie studio is profit. We used the difference between International Gross and budget and calculated it as a percentage of profit, or ROI. 

Next, we seperated our movies by the categories from our hypotheses and analyzed the data for patterns or trends. By reducing our sample size to recent movies that are relevant to our questions and aggregating our data, we were able to plot data from each of the four categories.

## Results

We calculated correlations between out four metrics and ROI and used a series of data visualizations to describe the data.

### Hypothesis 1- There is an optimal season to release movies.
![ROI by Month](./images/roi_by_month.png)
Our first hypothesis proved solid. Our data yeilded a group of four months with higher profits than the rest, which occur at three month increments, allowing a movie studio to release new titles throughout the year while maximizing profit through smart timing. 

### Hypothesis 2- Some genres are more profitable in the box office than others
![ROI by Genre](./images/ROI_genre.png)
Again, our hypothesis proved solid. Horror far out performed all other genres, while Thriller and Romance movies both showed solid average returns.

### Hypothesis 3- Budget is a predictor of profit
![ROI by Budget](./images/ROI_budget_fulldata.png)
This time our hypothesis was not vindicated by the initial inspection of the data. We can see from our initial analysis a negative trend as budgets increase. Because our dataset had so many outliers, we chose to dig a bit deeper and see what profitability looked like inside a narrower window.

![Budget outliers](./images/budget_outliers.png)
By removing outlying data, then narrowing our data to the central 70%, we see the trend line flatten and then move toward positive, signalling a window of more likely profit. While this still doesn't look like a strong indicator, it does give us some parameters to guide movie budgets in order to improve the likelihood of higher profit.

### Hypothesis 4- Ratings are a predictor of profit
![ROI vs Ratings](./images/ROI_vs_rating.png)
This hypothesis proved to be the least predictive of profit. Because ratings were such a poor measure of a movie's box office success, we chose not to fully explore ratings across our other factors, though we did compare with genre.

![Ratings by Genre](./images/genre_ratings.png)
Our most profitable genre, Horror, also had the lowest average ratings. While we thing quality and ratings are important to making and promoting movies, they are clearly not an important predictor of profit.

## Conclusion


## Links to notebook and presentation slides

## Repo structure