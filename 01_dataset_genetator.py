import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_iot_dataset(output_folder="datasets"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Define sensor types and their units
    sensor_types = [
        {"typ": "teplota", "jednotka": "°C", "min_val": 15, "max_val": 35},
        {"typ": "vlhkost", "jednotka": "%", "min_val": 20, "max_val": 90},
        {"typ": "svetlo", "jednotka": "lux", "min_val": 0, "max_val": 1000},
        {"typ": "hluk", "jednotka": "dB", "min_val": 30, "max_val": 90},
        {"typ": "CO2", "jednotka": "ppm", "min_val": 400, "max_val": 2000}
    ]
    
    # Define locations
    locations = ["Třída A", "Třída B", "Chodba", "Jídelna", "Knihovna", "Tělocvična"]
    
    # Generate sensors data
    sensors = []
    for i in range(1, 21):  # Create 20 sensors
        sensor_type = random.choice(sensor_types)
        location = random.choice(locations)
        install_date = datetime.now() - timedelta(days=random.randint(30, 365))
        
        sensor = {
            "sensor_id": i,
            "nazev_senzoru": f"Senzor-{i}",
            "typ": sensor_type["typ"],
            "umisteni": location,
            "datum_instalace": install_date.strftime("%Y-%m-%d")
        }
        sensors.append(sensor)
    
    # Create DataFrame and save to CSV
    sensors_df = pd.DataFrame(sensors)
    sensors_df.to_csv(f"{output_folder}/01_senzory.csv", index=False)
    
    # Generate measurements data
    measurements = []
    mereni_id = 1
    
    # Generate data for the last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    for sensor in sensors:
        # Find the sensor type details to get units and value ranges
        sensor_type_details = next(st for st in sensor_types if st["typ"] == sensor["typ"])
        
        # Generate readings every hour for the sensor
        current_date = start_date
        while current_date < end_date:
            # Basic value based on time of day (higher in afternoon)
            hour_factor = 0.5 + 0.5 * np.sin((current_date.hour - 6) * np.pi / 12)
            
            base_value = (sensor_type_details["min_val"] + 
                         (sensor_type_details["max_val"] - sensor_type_details["min_val"]) * hour_factor)
            
            # Add some randomness
            random_factor = np.random.normal(0, 0.1)
            value = base_value * (1 + random_factor)
            value = min(max(value, sensor_type_details["min_val"]), sensor_type_details["max_val"])
            
            measurement = {
                "mereni_id": mereni_id,
                "sensor_id": sensor["sensor_id"],
                "casova_znamka": current_date.strftime("%Y-%m-%d %H:%M:%S"),
                "hodnota": round(value, 2),
                "jednotka": sensor_type_details["jednotka"]
            }
            measurements.append(measurement)
            
            mereni_id += 1
            current_date += timedelta(hours=1)
            
            # To prevent the file from getting too large, we can sample some readings
            # e.g., only add readings every 3 hours for older dates
            if (end_date - current_date).days > 7:
                current_date += timedelta(hours=2)
    
    # Create DataFrame and save to CSV
    measurements_df = pd.DataFrame(measurements)
    measurements_df.to_csv(f"{output_folder}/01_mereni.csv", index=False)
    
    # Create a smaller sample of measurements for ease of use
    sample_size = min(5000, len(measurements))
    measurements_sample = random.sample(measurements, sample_size)
    measurements_sample_df = pd.DataFrame(measurements_sample)
    measurements_sample_df.to_csv(f"{output_folder}/01_mereni_sample.csv", index=False)
    
    print(f"Generated {len(sensors)} sensors")
    print(f"Generated {len(measurements)} measurements")
    print(f"Generated a sample of {sample_size} measurements")
    print(f"Files saved to {output_folder} folder")

if __name__ == "__main__":
    generate_iot_dataset()
    