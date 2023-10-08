#Read mzml file in python
#Extract MS2 scan 
#Plot 

from pyteomics import mzml 
from matplotlib import pyplot as plt

#Read mzml file in python
mzml_file = mzml.read("C:/Users/aditi.sharma2/Documents/GitHub/MS2_annotate_TUM/HelaDigest.mzML")

#Extract MS2 scan 
for spectrum in mzml_file:
	if spectrum['index'] == 0:
		intensities = spectrum['intensity array']
		m_over_z = spectrum['m/z array']
		break

#print(intensities)
#print(m_over_z)
#Plot the centroid data

plt.title("MS2 scan")
plt.xlabel("m/z")
plt.ylabel("Intensity")
plt.stem(m_over_z, intensities, markerfmt=" ")
plt.show()


