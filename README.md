# Sampling-Theory Studio

## Description
**Sampling-Theory Studio** is a user-friendly desktop application designed to illustrate the Nyquist–Shannon sampling theorem. This application provides an interactive platform for users to explore signal sampling, recovery, and the significance of the Nyquist rate.

### Key Features
1. Sample & Recover:
    - Visualize and sample signals at various frequencies.
    - Use Whittaker–Shannon interpolation to recover the original signal.
    - Observe the effects of different sampling frequencies on signal recovery.
2. Load & Compose:
    - Load signals from files or create custom signals using a built-in signal mixer.
    - Easily add or remove sinusoidal components to design complex signals.
3. Additive Noise:
    - Inject customizable noise into signals.
    - Explore how noise affects signals with varying frequencies.
4. Real-Time Processing:
    - All operations are performed in real-time, without the need for manual updates.
5. Resizable UI:
    - The application adapts to changes in window size while maintaining a user-friendly interface.
6. Different Sampling Scenarios:
    - Includes predefined scenarios to help users understand the Nyquist rate's importance and challenges in signal processing.

### Getting Started
To run the application, make sure you have Python and the required libraries (including PyQt and any additional libraries) installed. 
### Libraries

- **scipy.fft**
- **scipy.signal**
- **numpy**
- **pandas**
- **os**
- **scipy.interpolate**
- **pyqtgraph**
- **matplotlib.figure**
- **PyQt5.QtWidgets**
- **matplotlib.backends.backend_qt5agg**
- **sys**

Execute the main Python script to launch the application.

Doing this by:

1. Install python any version

2. In the cmd write the following commands to satisfy the compile requirment:
   - install pyqt by the command "pip install pqyt5"
   - install numpy by the command "pip install numpy"
   - install pyqt graph by the command "pip install pyqtgraph"

3. Put the files index.py and main.ui in same location that containg the downloaded python package

4. To determine the location write this command in the cmd "pip show pyqt5"

5. Open the index.py by any ide with python interpreter and run the code

### Team Members
* Rana Hany Mahmoud Tawfiq
* Sarah Ibrahim Abdelfattah
* Basmala Tarek Mohamed
