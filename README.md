# LIP-RTVE: An Audiovisual Database for Continuous Spanish in the Wild
##### Authors: David Gimeno-Gómez & Carlos-D. Martínez-Hinarejos

### INTRODUCTION
LIP-RTVE is an audiovisual database that was primarily conceived at the first instance as a corpus focused on the Automatic Lipreading or Visual Speech Recognition (VSR) task for the Spanish language. It is composed of around 13 hours of semi-automatically collected and annotated data. In addition, it belongs to the so-called _in the wild_ philosophy, since it was extracted from TV broadcast programmes contained in a subset of the RTVE2018 database¹ which has been employed in the Albayzín evaluations². Concretely, despite the fact that this database is made up of a wide range of programmes broadcast, we compiled our corpus only from the news programme known as 20H.

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/samples_corpus.gif" width="500" alt="An extract of LIP-RTVE samples"/>
</p>

### DATA STRUCTURE & SCRIPTS
##### HOWEVER, THE COMPLETE LIP-RTVE DATABASE IS NOT AVAILABLE AT THE MOMENT.

In order to facilitate the use of our data in future reseach and taking into account a Non-Disclouse Agreement (NSA) license, we are
processing the data to ensure a proper use of this database.

In any case, we are updating the data has already been computed. Thus, our ultimate purpose is to provide it in the following structure:

- [**src/alignments.csv :**](https://github.com/david-gimeno/LIP-RTVE/blob/main/data/alignments.csv) This file states where each sample of the LIP-RTVE corpus is located in the source data (RTVE2018 database¹). In this way, there are four columns:
     - **sampleID:** identificator of the LIP-RTVE sample.
     - **sourceID:** identificator of the TV programme (MP4 format) contained in the source data
     - **startTime:** time when the LIP-RTVE sample starts in its corresponding sourceID
     - **duration:** duration in seconds of the LIP-RTVE sample
- [**src/transcriptions.zip :**]() ZIP file where text transcriptions for each LIP-RTVE sample were compressed as one-line txt files.
- [**src/landmarks/ :**]() Folder where the 68 facial landmarks³ for each sample of the LIP-RTVE are stored in pkl files. These landmarks will allow you to extract the Regions of Interest (ROIs) with complete flexibility
- [**src/splits/ :**]() Folder where partitions for both a speaker-independent and speaker-dependent scenario are defined with CSV files.
- [**src/scripts/ :**]() Folder where python scripts are shared in order to obtain and process the data of the LIP-RTVE corpus
  - [**get_samples.py :**]() script that uses the provided alignments to extract the MP4 samples of the LIP-RTVE from source data
  - [**get_ROIs.py**]() script to extract the same ROIs we employed in our research. More specifically, we worked with ROIs known as _fitMouth_, _wideMouths_ and _faces_, each of them covering from a smaller to a larger region of the speaker's face. In addition, there is an option that allows you to extract ROIs following the pattern of other authors, who have recently reached the state of the art in VSR⁴
  - [**utils.py**]() script where different functions which other scripts need are coded
  - [**resources/**]() folder containing files needed by the scripts

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/roi_extraction_process.png" alt="The ROI extraction process and the different ROIs employed in our research"/>
</p>

##### THE COMPLETE LIP-RTVE DATABASE WILL BE PUBLICLY RELEASED AS SOON AS POSSIBLE.
<p>
  <img src="https://progress-bar.dev/32/?width=150&title=Processed alignments: " /><br>
  <img src="https://progress-bar.dev/0/?width=150&title=Processed landmarks: " /><br>
  <img src="https://progress-bar.dev/100/?width=150&title=Processed transcriptions: " /><br>
</p>

Thank you. We apologize for the inconvenience.

### HOW CAN I GET THE LIP-RTVE DATABASE? 

1. Clikck [in this link](http://catedrartve.unizar.es/rtvedatabase.html). Then, request and sign the Non-Disclouse Agreement license in order to be able to download the RTVE2018 database 
2. Locate the folder containing the _train_ and _dev_ datasets from the TV programme known as 20H
3. Clone this repository: ```git clone https://github.com/david-gimeno/LIP-RTVE.git``` and ```cd LIP-RTVE``` 
4. Create a conda environment with all the necessary dependencies: ```conda env create --name liprtve-env --file=liprtve-env.yml```
5. Once activated the conda environment, run the following command: ```./main.sh $RTVE2018_path```

### CITATION
We are awaiting for a response from the LREC conference regarding our proposed article.

### REFERENCES

1. Lleida, Eduardo and Ortega, Alfonso and Miguel, Antonio and Bazán, Virginia and Pérez, Carmen and Zotano, M and de Prada, Alberto. (2018). RTVE2018 database description. URL: http://catedrartve.unizar.es/reto2018/RTVE2018DB.pdf .
2. Lleida, E., Ortega, A., Miguel, A., Bazán-Gil, V., Pérez, C., Gómez, M., and de Prada, A. (2019). Albayzin 2018 evaluation: the iberspeech-rtve challenge on speech technologies for spanish broadcast media. Applied Sciences, 9(24):5412. DOI: https://doi.org/10.3390/app9245412, URL: https://www.mdpi.com/2076-3417/9/24/5412.
3. Sagonas, C., Antonakos, E., Tzimiropoulos, G., Zafeiriou, S., and Pantic, M. (2016). 300 faces in-the-wild challenge: database and results. Image and
Vision Computing, 47:3–18. DOI: https://doi.org/10.1016/j.imavis.2016.01.002, URL: https://www.sciencedirect.com/science/article/pii/S0262885616000147 .
4. P. Ma, S. Petridis, M. Pantic, Visual Speech Recognition for Multiple Languages in the Wild, arXiv Preprint: 2202.13084 (2022). URL: https://arxiv.org/abs/2202.13084
