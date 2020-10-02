import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
sns.set_theme()

def get_sensor_data():
    """
    TODO
    1) Connect to DynamoDB Table 
    2) Get the data for each sensor in the below format

    For now I just have random dummy data
    """
    return [
        {"name":"Temperature", 
        "timestamps": list(range(31)), 
        "values": [60]+[70, 75, 80, 85, 70, 77, 79, 82, 80, 77]*3
        },
         {"name":"Moisture", 
        "timestamps": list(range(10)), 
        "values": np.random.randn(1,10).tolist()[0]
        }
    ]

def plot_sensor_data():
    data = get_sensor_data()

    for sensor_data in data:
        sns.lineplot(
            x=sensor_data["timestamps"],
            y=sensor_data["values"]
        ).set_title(sensor_data["name"])
        plt.show()

if __name__ == "__main__":
    plot_sensor_data()
    

