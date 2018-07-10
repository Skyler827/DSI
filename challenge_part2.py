import os
import csv
from typing import List, Dict
import matplotlib.pyplot as plt
import numpy as np


def goal_vs_time() -> None:
    csvfile = open("DSI_kickstarterscrape_dataset.csv", errors="replace")
    data = csv.DictReader(csvfile, delimiter=',')
    # make a scatter plot of goal vs length of time
    # and another one with vector information
    project_durations:List[float] = []
    project_goals:List[float] = []
    color:List[str] = []
    for row in data:
        project_durations.append(row['duration'])
        project_goals.append(row['goal'])
        if row['status'] == 'succesfull':
            color.append('green')
        elif row['status'] == 'failed':
            color.append('red')
        else:
            color.append('black')
    csvfile.close()

    ## The following code is broken
    ## I suspect due to this bug:
    ## https://github.com/matplotlib/matplotlib/issues/10648
    plt.scatter(np.array(project_durations), np.array(project_goals), alpha=0.5, color=color)
    plt.xlabel('Days in campaign')
    plt.ylabel('Project Goal')
    plt.title('Project Goals vs length of time')
    #plt.axis([1, max_backers, 1, max(histogram_values)])
    #plt.grid(True)
    try:
        os.makedirs("output")
    except: pass
    file_path = os.path.join("output", "goals_vs_time_scatter.png")
    plt.savefig(file_path)
    plt.clf()

def part2() -> None:
    goal_vs_time()

if __name__ == "__main__":
    part2()