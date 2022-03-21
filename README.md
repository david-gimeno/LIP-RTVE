# LIP-RTVE: An Audiovisual Database for Continuous Spanish in the Wild
### Authors: David Gimeno-Gómez & Carlos-D. Martínez-Hinarejos

LIP-RTVE is an audiovisual database that was primarily conceived at the first instance as a corpus focused on the Automatic Lipreading or Visual Speech Recognition task for the Spanish language. 
https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/samples_corpus.png

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/samples_corpus.png" alt="An extract of LIP-RTVE samples"/>
</p>

It is composed of around 13 hours of semi-automatically collected and annotated data. In addition, it belongs to the so-called _in the wild_ philosophy, since it was extracted from TV broadcast programmes contained in a subset of the RTVE database¹ which has been employed in the Albayzín evaluations². Concretely, despite the fact that this database is made up of a wide range of programmes broadcast, we compiled our only from the news programme 20H.

##### HOWEVER, THE COMPLETE LIP-RTVE DATABASE IS NOT AVAILABLE AT THE MOMENT.
In order to facilitate the use of our data in future reseach and taking into account a Non-Disclouse Agreement (NSA) license, we are
processing the data to ensure a proper use of this database.

In any case, we are updating the data has already been computed. Thus, our ultimate purpose is to provide it in the following structure:

- **alignments.csv :** This file states where each sample of the LIP-RTVE corpus is located in the source data (RTVE database¹). In this way, there are four columns:
     - sampleID: identificator of the LIP-RTVE sample
     - sourceID: identificator of the TV programme (MP4 format) contained in the source data
     - startTime: time when the LIP-RTVE sample starts in sourceID
     - duration: duration of the LIP-RTVE sample
- **landmarks/\*/\*.pkl :** Folder where the 68 facial landmarks³ for each sample of the LIP-RTVE are stored in pkl files. These landmarks will allow you to extract the Regions of Interest (ROIs) with complete flexibility.
- **scripts/\*.py :** Folder where python scripts are shared in order to extract the same ROIs we employed in our research. More specifically, we worked with ROIs known as _fitMouth_, _wideMouths_ and _faces_, each of them covering from a smaller to a larger region of the speaker's face.

<p align="center">
  <img src="https://github.com/david-gimeno/LIP-RTVE/blob/main/docs/roi_extraction_process.png" alt="The ROI extraction process and the different ROIs employed in our research"/>
</p>

##### THE COMPLETE LIP-RVTE DATABASE WILL BE PUBLICLY RELEASED AS SOON AS POSSIBLE.

Thank you. We apologize for the inconvenience.

1. @article{11lleida2018rtve2018,
     Author = {Lleida, Eduardo and Ortega, Alfonso and Miguel, Antonio and Baz{\'a}n, Virginia and P{\'e}rez, Carmen and Zotano, M and de Prada, Alberto},
     Journal = {Vivolab and Corporaci{\'o}n Radiotelevisi{\'o}n Espa{\~n}ola, Zaragoza, Spain},
     Title = {RTVE2018 database description},
     Year = {2018},
     Note = {[Online] Available: \url{ http://catedrartve.unizar.es/reto2018/RTVE2018DB.pdf }
   }
}

2. @article{12lleida2019albayzin,
     title={Albayzin 2018 evaluation: the iberspeech-RTVE challenge on speech technologies for spanish broadcast media},
     author={Lleida, Eduardo and Ortega, Alfonso and Miguel, Antonio and Baz{\'a}n-Gil, Virginia and P{\'e}rez, Carmen and G{\'o}mez, Manuel and de Prada, Alberto},
     journal={Applied Sciences},
     volume={9},
     number={24},
     pages={5412},
     year={2019},
     url={https://www.mdpi.com/2076-3417/9/24/5412},
     issn={2076-3417},
     doi={10.3390/app9245412}
     publisher={Multidisciplinary Digital Publishing Institute}
   }

3. @article{sagonas2016,
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
