import numpy as np
import pandas as pd

# Define parameters
num_points = 1000  # Total number of data points
num_segments = 5   # Number of frequency segments

# Create an empty DataFrame
data = {'Time': [], 'ECG_Signal': [], 'Frequency': []}

# Generate ECG data with varying frequencies
for segment in range(num_segments):
    start_time = segment * num_points // num_segments
    end_time = (segment + 1) * num_points // num_segments
    time = np.linspace(start_time, end_time, end_time - start_time)
    ecg_amplitude = 1.0  # Amplitude of the ECG signal
    ecg_frequency = 0.5 + segment * 0.2  # Varying frequency
    ecg_signal = ecg_amplitude * np.sin(2 * np.pi * ecg_frequency * time)

    # Append data to the DataFrame
    data['Time'] += time.tolist()
    data['ECG_Signal'] += ecg_signal.tolist()
    data['Frequency'] += [ecg_frequency] * len(time)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_filename = 'ecg_dataset_with_varying_frequencies.csv'
df.to_csv(csv_filename, index=False)

print(f'ECG dataset with varying frequencies saved to {csv_filename}')
