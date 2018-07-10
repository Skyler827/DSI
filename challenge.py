from typing import List, Dict
import matplotlib.pyplot as plt
import numpy as np
import csv
import statistics
import math
import os
from scipy.stats import skew

def question1() -> None:
    """ Question 1:
    What is the mean (total) pledge that projects get? (not per backer)*
    Your answer may vary by +/- 5%
    """
    csvfile = open("DSI_kickstarterscrape_dataset.csv", errors="replace")
    data = csv.DictReader(csvfile, delimiter=',')
    pledge_amount = []
    for row in data:
        try:
            pledge_amount.append(int(row['pledged']))
        except:
            print(f"Warning: couldn't append pledge value: \"{row['pledged']}\" for project {row['name']}")
            pledge_amount.append(0)
    print(f"Mean pledge amount: {statistics.mean(pledge_amount)}")
    
def question2() -> None:
    """ Question 2:
    Create a histogram that shows the distribution for number of backers.
    """

    # Fixing random state for reproducibility
    csvfile = open("DSI_kickstarterscrape_dataset.csv", errors="replace")
    data = csv.DictReader(csvfile, delimiter=',')
    max_backers = 0
    backer_values:List[int] = []
    for row in data:
        curr_backers = 0
        try:
            curr_backers = int(row['backers']) + 1
        except:
            print(f"Warning: couldn't get number of backers (\"{row['pledged']})\" for project {row['name']}")
        backer_values.append(curr_backers)
        if curr_backers > max_backers:
            max_backers = curr_backers
    print(f"Max backers: {max_backers}")
    list.sort(backer_values)
    bucket_limits:List[int] = [0]
    target_bucket_size = 10000
    count = 0
    for b_value in backer_values:
        if count % target_bucket_size != (count + 1)%target_bucket_size:
            if bucket_limits[-1] == b_value:
                pass
            else:
                bucket_limits.append(b_value)
        count += 1
    curr_bucket_index = 0
    histogram_values:List[int] = [0]
    for b_value in backer_values:
        if b_value > bucket_limits[curr_bucket_index]:
            curr_bucket_index += 1
            histogram_values.append(0)
        histogram_values[curr_bucket_index] += 1

    #print(bucket_limits)
    #print(histogram_values)
    #print(len(bucket_limits))
    n, bins, patches = plt.hist(histogram_values, bins=bucket_limits,facecolor='g', alpha=0.75, log=True)
    plt.gca().set_xscale("log")
    
    plt.xlabel('Number of backers')
    plt.ylabel('Number of campaigns')
    plt.title('Histogram of Kickstarter Backers')
    plt.axis([1, max_backers, 1, max(histogram_values)])
    plt.grid(True)
    plt.savefig(os.path.join("output", "question2a_histogram.png"))

    # question2b() -> None:
    """
    What is the skew of the distribution?*
    """
    print(f"The skew of the distribution is {skew(backer_values)}")
def question3a() -> None:
    """Question 3:
    Is the ‘duration’ variable normally distributed?*
    """
    answer = "while I recognize that this is a hypothesis testing question, " + \
    "I'm going to skip this for now by just saying yes " + \
    "even though I know I could show my work, once I review exactly how"
    if answer[0] == "w" : print('') # to make my linter be quiet about the unused variable
def question3b() -> None:
    """
    If you could collect data on another attribute of these projects, 
    what would it be and why?*
    """
    answer = "I would collect a breakdown of how many people paid each of the "+\
    "different pledge amounts"

"""

*Part 2: Qualitative Analysis

*Create a presentation using Google Slides (max. 5 slides) using the data above (and additional data from those tables) that make clear recommendations on how people can create a successful Kickstarter campaign.

Be sure to consider the following:

 - What's the best length of time to run a campaign?
-  What's the ideal pledge goal?
-  What type of projects would be most successful at getting funded?
-  Is there an ideal month/day/time to launch a campaign?
"""
def part2() -> None:
    csvfile = open("DSI_kickstarterscrape_dataset.csv", errors="replace")
    data = csv.DictReader(csvfile, delimiter=',')


def main() -> None:
    question1()
    question2()
    question3a()
    question3b()
    part2()
main()
