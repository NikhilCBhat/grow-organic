import seaborn as sns
from matplotlib import pyplot as plt
import math
sns.set_theme()
import sys
sys.path.append('.')
from sensor_data.query_sensor_database import get_data_from_database

def plot_sensor_data():
    data = get_data_from_database()
    size = math.ceil(math.sqrt(7))
    f, axes = plt.subplots(size, size)

    for i, sensor_data in enumerate(data):
        sns.lineplot(
            x=sensor_data["timestamps"],
            y=sensor_data["values"],
            ax=axes[i%size, i//size]
        ).set_title(sensor_data["name"])
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_sensor_data()
    

