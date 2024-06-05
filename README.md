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

-   <ins>Image Cropping</ins>: contains two folders for image cropping one outputting an image without ARuCO markers and one outputting an image with ARuCO markers

    -   Excluding ARuCO: contains 4 files-- the JupyterNotebook file for image cropping with line annotations, the rendered HTML file, the rendered .MD file, and the outputted cropped test image
    -   Including ARuCO: contains the same 4 files as the Excluding ARuCO folder but for outputted cropped images that include the ARuCO markers
 
-   <ins> Perspective Correction</ins>: JupyterNotebook tool to correct warped field bee wing images

-   <ins> Reports </ins>: contains two JupyterNotebook scripts that explore Linear Discriminant Analysis (LDA) and Spectral Embedding with line annotations and a written report on the subjects
    -   CCBER Capstone_ Wing Morphology Exploration.pdf: written report on both LDA and Spectral Embedding
    -   CCBER Relevant Sources Report.pdf: writte report on relevant sources to our project and future research
    -   SpectralEmbedding.ipynb: JupyterNotebook script exploring Spectral Embedding initially using the MNIST dataset and then adapting it to the bee wing images
    -   LDA.ipynb: JupyterNotebook script exploring LDA with line annotations

-   <ins> VGG16 </ins>: contains 2 folders and 1 JupyterNotebook script containing the code for the neural network VVG-16
    -   Bootstrap: folder containing bootstrap.py script
    -   Gaussian Blur: folder containing GaussianBlur v2.py script
    -   vgg16_v2.ipynb: JupyterNotebook script that walks through training and testing the VGG-16 model with line annotations
 
-   <ins> Wing Length Calculation </ins>: contains two JupyterNotebook scripts--one that calculates wing length in mm from ARuCO markers, and one that calculates wing length in mm from the ruler



      
**Necessary Installations**: JupyterNotebook, VSCode (or any IDE)

The repository also contains this `README.md` file, which contains the description, contributors, abstract, contents, and references for this project.

## References 

B. -C. Kuo, H. -H. Ho, C. -H. Li, C. -C. Hung and J. -S. Taur, "A Kernel-Based Feature Selection Method for SVM With RBF Kernel for Hyperspectral Image Classification," in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 7, no. 1, pp. 317-326, Jan. 2014, doi: 10.1109/JSTARS.2013.2262926. keywords: {Support vector machines;Kernel;Training;Hyperspectral imaging;Educational institutions;Feature extraction;Feature selection;hyperspectral image classification;kernel-based feature selection;radial basis function;support vector machines}

Kavlakoglu, Eda. Implementing Linear Discriminant Analysis (LDA) in Python, 18 Mar. 2024, developer.ibm.com/tutorials/awb-implementing-linear-discriminant-analysis-python/.

Pewsey, Matt. “MNIST Handwritten Digit Classification.” Matt Pewsey, 28 Sept. 2021, mpewsey.github.io/2021/09/28/mnist-handwritten-digit-classification.html.

Rodrigues PJ, et all (2022). DeepWings©: Automatic Wing Geometric Morphometrics Classification of Honey Bee (Apis mellifera) Subspecies Using Deep Learning for Detecting Landmarks. Big Data and Cognitive Computing.
