# LIP-RTVE: An Audiovisual Database for Continuous Spanish in the Wild
##### Authors: David Gimeno-Gómez & Carlos-D. Martínez-Hinarejos

### INTRODUCTION
LIP-RTVE is an audiovisual database that was primarily conceived at the first instance as a corpus focused on the Automatic Lipreading or Visual Speech Recognition (VSR) task for the Spanish language. It is composed of around 13 hours of semi-automatically collected and annotated data. In addition, it belongs to the so-called _in the wild_ philosophy, since it was extracted from TV broadcast programmes contained in a subset of the RTVE2018 database¹ which has been employed in the Albayzín evaluations². Concretely, despite the fact that this database is made up of a wide range of programmes broadcast, we compiled our corpus only from the news programme known as 20H.

In order to obtain the LIP-RTVE corpus, you must first get access to the original RTVE database which is protected by an Non-Disclouse Agreement (NDA) license. Once you have solved this matter, by using our software and CSV files you will be able to extract the samples that define our compiled LIP-RTVE database. Detailed instructions described below.

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/samples_corpus.gif" width="500" alt="An extract of LIP-RTVE samples"/>
</p>

### DATA STRUCTURE & SCRIPTS

In order to facilitate the use of our data in future reseach and taking into account a Non-Disclouse Agreement (NSA) license, we are
processing the data to ensure a proper use of this database.

In any case, we are updating the data has already been computed. Thus, our ultimate purpose is to provide it in the following structure:

- [**src/alignments.csv :**](https://github.com/david-gimeno/LIP-RTVE/blob/main/src/alignments.csv) This file states where each sample of the LIP-RTVE corpus is located in the source data (RTVE2018 database¹). In this way, there are four columns:
     - **sampleID:** identificator of the LIP-RTVE sample.
     - **sourceID:** identificator of the TV programme (MP4 format) contained in the source data
     - **startTime:** timestamp when the LIP-RTVE sample starts in its corresponding sourceID
     - **duration:** duration in seconds of the LIP-RTVE sample
- [**src/transcriptions.zip :**](https://github.com/david-gimeno/LIP-RTVE/tree/main/src) ZIP file where text transcriptions for each LIP-RTVE sample were compressed as one-line txt files.
- [**src/landmarks.zip :**](https://github.com/david-gimeno/LIP-RTVE/tree/main/src) ZIP file where the 68 facial landmarks³ for each sample of the LIP-RTVE are stored in pkl files. These landmarks, computed by using open-source software<sup>4,5</sup>, will allow you to extract the Regions of Interest (ROIs) with complete flexibility
- [**src/splits/ :**](https://github.com/david-gimeno/LIP-RTVE/tree/main/src/splits) Folder where partitions for both a speaker-independent and speaker-dependent scenario are defined with CSV files.
- [**src/LM/textLM.txt :**](https://github.com/david-gimeno/LIP-RTVE/tree/main/src/LM/) Text file where around 80k senteces were collected from different TV newcasts broadcast by RTVE during the same dates as the data that make up the LIP-RTVE corpus. 
- [**src/scripts/ :**](https://github.com/david-gimeno/LIP-RTVE/tree/main/src/scripts) Folder where python scripts are shared in order to obtain and process the data of the LIP-RTVE corpus
  - [**get_samples.py :**](https://github.com/david-gimeno/LIP-RTVE/blob/main/src/scripts/get_samples.py) script that uses the provided alignments to extract the MP4 samples of the LIP-RTVE from source data
  - [**get_ROIs.py**](https://github.com/david-gimeno/LIP-RTVE/blob/main/src/scripts/get_ROIs.py) script to extract the same ROIs we employed in our research. More specifically, we worked with ROIs known as _fitMouth_, _wideMouths_ and _faces_, each of them covering from a smaller to a larger region of the speaker's face. In addition, there is an option that allows you to extract ROIs following the pattern of other authors, who have recently reached the state of the art in VSR⁶
  - [**utils.py**](https://github.com/david-gimeno/LIP-RTVE/blob/main/src/scripts/utils.py) script where different functions which other scripts need are coded
  - [**resources/**](https://github.com/david-gimeno/LIP-RTVE/tree/main/src/scripts/resources) folder containing files needed by the scripts

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/roi_extraction_process.png" width="500" alt="An extract of LIP-RTVE samples"/>
</p>

### HOW CAN I GET THE LIP-RTVE DATABASE? 

1. Clikck [this link](http://catedrartve.unizar.es/rtvedatabase.html). Then, request and sign the Non-Disclouse Agreement license in order to be able to download the RTVE2018 database 
2. Locate the folder containing the `train/` and `dev/` datasets (i.e. directories) from the TV programme known as 20H
3. Clone this repository: ```git clone https://github.com/david-gimeno/LIP-RTVE.git```
4. Create a conda environment with all the necessary dependencies: ```cd LIP-RTVE; conda env create -f liprtve-env.yml```
5. Once activated the conda environment, run the following command: ```./main.sh $RTVE2018_path```

### CITATION

If you use the LIP-RTVE database in your research, please consider citing the following paper:

```
@InProceedings{liprtve2022lrec,
  author = {Gimeno-Gómez, David  and  Martínez-Hinarejos, Carlos-D.},
  title = {LIP-RTVE: An Audiovisual Database for Continuous Spanish in the Wild},
  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
  month = {June},
  year = {2022},
  address = {Marseille, France},
  publisher = {European Language Resources Association},
  pages = {2750--2758},
  url = {https://aclanthology.org/2022.lrec-1.294}
}
```
## ACKNOWLEDGEMENTS

This work was partially supported by Generalitat Valenciana under project DeepPattern (PROMETEO/2019/121) and by Ministerio de Ciencia under project MIRANDA-DocTIUM (RTI2018-095645-B-C22). The authors who compiled the database were working at Pattern Recognition and Human Language Technology (PRHLT) research center which belongs to the Universitat Politècnica de València.

### REFERENCES

1. Lleida, Eduardo and Ortega, Alfonso and Miguel, Antonio and Bazán, Virginia and Pérez, Carmen and Zotano, M and de Prada, Alberto. (2018). RTVE2018 database description. URL: http://catedrartve.unizar.es/reto2018/RTVE2018DB.pdf .
2. Lleida, E., Ortega, A., Miguel, A., Bazán-Gil, V., Pérez, C., Gómez, M., and de Prada, A. (2019). Albayzin 2018 evaluation: the iberspeech-rtve challenge on speech technologies for spanish broadcast media. Applied Sciences, 9(24):5412. DOI: https://doi.org/10.3390/app9245412, URL: https://www.mdpi.com/2076-3417/9/24/5412.
3. Sagonas, C., Antonakos, E., Tzimiropoulos, G., Zafeiriou, S., and Pantic, M. (2016). 300 faces in-the-wild challenge: database and results. Image and
Vision Computing, 47:3–18. DOI: https://doi.org/10.1016/j.imavis.2016.01.002, URL: https://www.sciencedirect.com/science/article/pii/S0262885616000147 .
4. https://github.com/hhj1897/face_detection
5. https://github.com/hhj1897/face_alignment
6. P. Ma, S. Petridis, M. Pantic, Visual Speech Recognition for Multiple Languages in the Wild, arXiv Preprint: 2202.13084 (2022). URL: https://arxiv.org/abs/2202.13084
