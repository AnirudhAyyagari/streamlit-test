# visualization.py

import matplotlib.pyplot as plt

def generate_bar_chart(data, labels):
    plt.bar(labels, data)
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.title('Simple Bar Chart')
    plt.savefig('chart.png')
