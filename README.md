# Data Science Capstone 2024: Bee Species Identification
## Cheadle Center for Biodiversity and Ecological Restoration
### Student Team: *Rohit Kavuluru, Dannah Golich, Jennifer Rink, Patrick Moon, Navneet Rajagopal, and Jiashu Huang*
### Sponsors and Mentor: *Dr. Katja Seltmann, Dr. Madeleine Ostwald, and Dr. Laura Baracaldo Lancheros*

The Cheadle Center for Biodiversity and Ecological Restoration’s data science capstone project aims to mitigate the critical decline in bee populations by enhancing the efficiency and accuracy of population monitoring techniques by creating an automated classification system. In order to identify specific regions where bee populations are vulnerable, scientists and researchers need an accurate species identification method so they can focus on their efforts to save these essential pollinators that are crucial for ecosystem stability.

Experimenting with both neural networks and landmarking to create the models, this project utilized the promising results of a previous CCBER study on geometric morphometrics in assessing subtle phenotypic differences. The study analyzed specimens from a reproductively isolated population on Santa Cruz Island and compared them to mainland populations, where significant differentiation in wing venation was identified. These results not only support bee conservation efforts but also expand our understanding of complex geometric variations in nature, offering wider applications in biological research.

The project’s deliverables include:
1) A species identification tool that can identify varying bee species based on wing characteristics with a high accuracy rate (>90%).
2) A thorough investigation into various approaches for quantifying differences in wing morphology, including the use of landmarks and other methods.
3) A reliable wing length measurement tool that provides accurate and consistent results, particularly focusing on images with Aruco markers.
4) A pipeline for standardizing field images, including processes such as perspective correction, cropping, and any other necessary pre-processing steps in order to aid local population research and analysis.


## Repository Contents

In this repository, there are several folders:

-   Bee winglength calculation: contains two JupyterNotebook scripts--one that calculates wing length in mm from ARuCO markers, and one that calculates wing length in mm from the ruler

-   Image Cropping: contains two folders for image cropping one outputting an image without ARuCO markers and one outputting an image with ARuCO markers

    -   Excluding ARuCO: contains 4 files-- the JupyterNotebook file for image cropping with line annotations, the rendered HTML file, the rendered .MD file, and the outputted cropped test image
    -   Including ARuCO: contains the same 4 files as the Excluding ARuCO folder but for outputted cropped images that include the ARuCO markers

-   Reports: contains two JupyterNotebook scripts that explore Linear Discriminant Analysis (LDA) and Spectral Embedding with line annotations and a written report on the subjects
  -   CCBER Capstone_ Wing Morphology Exploration.pdf: written report on both LDA and Spectral Embedding
  -   SpectralEmbedding.ipynb: JupyterNotebook script exploring Spectral Embedding initially using the digits dataset and then adapting it to the bee wing images
  -   LDA.ipynb: JupyterNotebook script exploring LDA with line annotations

-   Preprocessing-Landmarks:
-   VGG16:
-   perspective_correction

The repository also contains this `README.md` file, which contains the description, contributors, abstract, contents, and references for this project.
