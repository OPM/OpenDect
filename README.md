# OpenDect
Core simulation tool based on CT-images
## Structure
Here are described the major steps in the code:

1. Read CT scan DICOM file using the pydicom library
2. Select an area of interest, typically where rock samples were taken for core analysis.
3. The porosity, density and photoelectric factor are derived for each pixel in this region.
4. A 3D grid model is built based on upscaled porosity from the CT scan. Permeability is user-defined or picked from a trend.
5. The flowing experiment is chosen and an eclipse file is run using OPM Flow
6. The relative permeabilities are history-matched using ERT Ensemble
