import seaborn as sns
from matplotlib import pyplot as plt
import math
sns.set_theme()
import sys
sys.path.append('.')
from sensor_data.query_sensor_database import get_data_from_database

sensor_type_to_units = {
    "MOISTURE": "Relative Moisture",
    "IR": "Wavelength (nm)",
    "TEMPERATURE": "Degrees (C)",
    "WIND": "Speed (mph)",
    "VISIBLE": "Wavelength (nm)",
    "HUMIDITY": "% water in air"
}

def plot_sensor_data():
    data = get_data_from_database()
    size = math.ceil(math.sqrt(7))
    _, axes = plt.subplots(size, size)

    for i, sensor_data in enumerate(data):
        g = sns.lineplot(
            x=[x/3600-min(sensor_data["timestamps"])/3600 for x in sensor_data["timestamps"]],
            y=sensor_data["values"],
            ax=axes[i%size, i//size],
            hue=sensor_data["plant_id"],
            marker="o"
        )
        g.set_title(sensor_data["name"])
        g.set(ylabel=sensor_type_to_units.get(sensor_data["name"], sensor_data["name"]))
        leg = g.axes.get_legend()
        if leg is not None:
            leg.set_title("plant id")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_sensor_data()


