# Friends-TV-Show

## Description

The analysis aims to determine which character had the most lines to remember throughout the show's 10 seasons. This information can provide insights into the importance and prominence of each character in the show, as well as their overall impact on the storyline.

By counting the number of lines each character had in the show, we can see how much of an impact they had on the show's dialogue and storyline. This analysis can also reveal which characters were given more or less screen time, which can be indicative of their overall importance to the show.

Overall, this analysis can help us understand the show's dynamics and the roles of each character in shaping the show's storyline.

## Code Description

This code is performing an analysis of the TV show Friends. It uses regular expressions to search for the names of the main characters in the transcripts of each episode, counts how many times each character speaks in each episode, and then sums up the total number of lines spoken by each character across all episodes.

The main function, "main", takes a list of episode numbers as input and calls the "match_actors" function for each episode to get a dictionary of character counts for that episode. It then adds up the counts for each character across all episodes and returns the total counts in a dictionary.

The "match_actors" function takes an episode number as input and returns a dictionary of character counts for that episode. It first reads in the HTML transcript of the episode from the show's website, using the urllib library. It then uses regular expressions to search for lines in the transcript that match the names of the characters, counts the number of matches for each character, and returns the counts in a dictionary.

The code defines a list of character names and a list of regular expressions to search for those names, with both uppercase and lowercase versions of the names. It also defines a list of episode numbers for each season of the show.

Finally, the code uses the "seaborn" and "matplotlib" libraries to create a bar chart showing the total number of lines spoken by each character across all episodes. The chart is saved as a PNG file. The code also prints out the total time it took to run the analysis.

## Data Analysis and Conclusion 

Based on the output, we can see that Ross and Rachel have the highest number of lines spoken throughout all 10 seasons of Friends, with Ross having 8666 lines and Rachel having 8840 lines. This is not surprising, as the show heavily revolves around their romantic relationship.

Chandler and Monica come in at a close second with 8024 and 8022 lines respectively, followed by Joey with 7908 lines. Phoebe has the lowest number of lines spoken among the main cast with 7048 lines.

However, it's important to note that **_the number of lines spoken doesn't necessarily equate to the importance of the character or their impact on the show_**. Each character had their own unique personality and contributed to the overall dynamic of the show in their own way.

Overall, it's interesting to see the breakdown of lines spoken among the main cast and how it reflects the character's individual roles and contributions to the show.

### Graph Representaiton 

![image](https://user-images.githubusercontent.com/92218899/224563123-19ee389e-7eac-4530-8467-987bc57c9d80.png)

## Credits 

All data is collected from the website below 
https://fangj.github.io/friends/ 
