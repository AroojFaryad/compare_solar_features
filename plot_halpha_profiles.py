######################ploting doifferent between Ellerman Bombs and sunspot and other bright point######
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Step 1: Load the FITS file
fits_file = #dataset file location
hdul = fits.open(fits_file)
data = hdul[0].data 
hdul.close()

# Step 2: Select one slice for the 2nd dimension (we will use index 10 here, adjust as needed)
slit_index = 10  # Adjust this based on what represents a typical view

# Step 3: Select four points for Quiet Sun, Sunspot, EB, and Bright Point on the Sun
# Ensure that the points are within the bounds of (362, 350)
quiet_sun_coords = (83, 273)  # Example coordinates within bounds, adjust as necessary
sunspot_coords = (77, 204)
eb_coords = (143, 171)
bright_point_coords = (189, 221)

# Step 4: Extract the Hα profiles at these positions for the chosen slit index
quiet_sun_profile = data[:, slit_index, quiet_sun_coords[0], quiet_sun_coords[1]]
sunspot_profile = data[:, slit_index, sunspot_coords[0], sunspot_coords[1]]
eb_profile = data[:, slit_index, eb_coords[0], eb_coords[1]]
bright_point_profile = data[:, slit_index, bright_point_coords[0], bright_point_coords[1]]

# Step 5: Generate wavelength array from -1.3 Å to 1.3 Å
wavelength = np.linspace(-1.3, 1.3, data.shape[0])  # Adjust wavelength based on data shape

# Step 6: Plot the profiles
plt.figure(figsize=(8, 6))
plt.plot(wavelength, quiet_sun_profile, label='Quiet Sun', color='blue')
plt.plot(wavelength, sunspot_profile, label='Sunspot', color='green')
plt.plot(wavelength, eb_profile, label='Ellerman Bomb', color='orange')
plt.plot(wavelength, bright_point_profile, label='Bright Point', color='red')

# Labels and legend
plt.xlabel('Wavelength [Å]')
plt.ylabel('Intensity [AU]')
plt.title('Hα Profiles for Different Solar Features')
plt.legend()

# Show the plot
plt.show()
