# LIP-RTVE: An Audiovisual Database for Continuous Spanish in the Wild
##### Authors: David Gimeno-Gómez & Carlos-D. Martínez-Hinarejos

### INTRODUCTION
LIP-RTVE is an audiovisual database that was primarily conceived at the first instance as a corpus focused on the Automatic Lipreading or Visual Speech Recognition (VSR) task for the Spanish language. It is composed of around 13 hours of semi-automatically collected and annotated data. In addition, it belongs to the so-called _in the wild_ philosophy, since it was extracted from TV broadcast programmes contained in a subset of the RTVE database¹ which has been employed in the Albayzín evaluations². Concretely, despite the fact that this database is made up of a wide range of programmes broadcast, we compiled our corpus only from the news programme known as 20H.

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/samples_corpus.gif" width="500" alt="An extract of LIP-RTVE samples"/>
</p>

### DATA STRUCTURE & SCRIPTS
##### HOWEVER, THE COMPLETE LIP-RTVE DATABASE IS NOT AVAILABLE AT THE MOMENT.
##### IT WILL BE PUBLICLY RELEASED AS SOON AS POSSIBLE.
<p>
  <img src="https://progress-bar.dev/30/?width=150&title=Processed samples: " /><br>
  <img src="https://progress-bar.dev/0/?width=150&title=Processed landmarks: " /><br>
</p>
##### Thank you. We apologize for the inconvenience.

In order to facilitate the use of our data in future reseach and taking into account a Non-Disclouse Agreement (NSA) license, we are
processing the data to ensure a proper use of this database.

In any case, we are updating the data has already been computed. Thus, our ultimate purpose is to provide it in the following structure:

- [**data/alignments.csv :**](https://github.com/david-gimeno/LIP-RTVE/blob/main/data/alignments.csv) This file states where each sample of the LIP-RTVE corpus is located in the source data (RTVE database¹). In this way, there are four columns:
     - **sampleID:** identificator of the LIP-RTVE sample.
     - **sourceID:** identificator of the TV programme (MP4 format) contained in the source data
     - **startTime:** time when the LIP-RTVE sample starts in its corresponding sourceID
     - **duration:** duration in seconds of the LIP-RTVE sample
- [**data/landmarks/ :**]() Folder where the 68 facial landmarks³ for each sample of the LIP-RTVE are stored in pkl files. These landmarks will allow you to extract the Regions of Interest (ROIs) with complete flexibility.
- [**data/scripts/ :**]() Folder where python scripts are shared in order to obtain and process the data of the LIP-RTVE corpus.
  - [**get_samples.py :**]() script to 
  - [**get_ROIs.py**]() script to extract the same ROIs we employed in our research. More specifically, we worked with ROIs known as _fitMouth_, _wideMouths_ and _faces_, each of them covering from a smaller to a larger region of the speaker's face. In addition, there is an option that allows you to extract ROIs following the pattern of other authors, who have recently reached the state of the art in VSR⁴. 

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/roi_extraction_process.png" alt="The ROI extraction process and the different ROIs employed in our research"/>
</p>

### Citation
We are awaiting for a response from the LREC conference regarding our proposed article.

### References

1.
```
@article{11lleida2018rtve2018,
   Author = {Lleida, Eduardo and Ortega, Alfonso and Miguel, Antonio and Baz{\'a}n, Virginia and P{\'e}rez, Carmen and Zotano, M and de Prada, Alberto},      Journal = {Vivolab and Corporaci{\'o}n Radiotelevisi{\'o}n Espa{\~n}ola, Zaragoza, Spain},<br/>
   Title = {RTVE2018 database description},
   Year = {2018},
   Note = {[Online] Available: \url{ http://catedrartve.unizar.es/reto2018/RTVE2018DB.pdf }}
}
```
2.
```
@article{12lleida2019albayzin,
   title={Albayzin 2018 evaluation: the iberspeech-RTVE challenge on speech technologies for spanish broadcast media},
   author={Lleida, Eduardo and Ortega, Alfonso and Miguel, Antonio and Baz{\'a}n-Gil, Virginia and P{\'e}rez, Carmen and G{\'o}mez, Manuel and de Prada, Alberto},
   journal={Applied Sciences},
   volume={9},
   number={24},
   pages={5412},
   year={2019},
   url={https://www.mdpi.com/2076-3417/9/24/5412},
   issn={2076-3417},
   doi={10.3390/app9245412},
   publisher={Multidisciplinary Digital Publishing Institute}
}
```
3.
```
@article{sagonas2016,
   title = {300 Faces In-The-Wild Challenge: database and results},
   journal = {Image and Vision Computing},
   volume = {47},
   pages = {3-18},
   year = {2016},
   note = {300-W, the First Automatic Facial Landmark Detection in-the-Wild Challenge},
   issn = {0262-8856},
   doi = {https://doi.org/10.1016/j.imavis.2016.01.002},
   url = {https://www.sciencedirect.com/science/article/pii/S0262885616000147},
   author = {Christos Sagonas and Epameinondas Antonakos and Georgios Tzimiropoulos and Stefanos Zafeiriou and Maja Pantic}
}
```
4.
```
@article{ma2022visual,
   title={{Visual Speech Recognition for Multiple Languages in the Wild}},
   author={Ma, Pingchuan and Petridis, Stavros and Pantic, Maja},
   journal={{arXiv Preprint: 2202.13084}},
   year={2022}
}
```
