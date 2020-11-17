import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
sns.set_theme()
import sys
sys.path.append('.')
from sensor_data.query_sensor_database import get_data_from_database

def plot_sensor_data():
    data = get_data_from_database()

    for sensor_data in data:
        sns.lineplot(
            x=sensor_data["timestamps"],
            y=sensor_data["values"]
        ).set_title(sensor_data["name"])
        plt.show()

if __name__ == "__main__":
    plot_sensor_data()
    

