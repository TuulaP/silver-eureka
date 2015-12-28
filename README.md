# silver-eureka

Tiny tesseract wrapper.

The script runs tesseract for multiple languages, which typically give
the best results with Finnish fraktur font:

    potential_langs = ['deu_frak','fin','dan_frak']

(For some reason tesseract file.jpg -l deu_frak+fin+dan_frak didn't do
what was desired.)

## Prerequisites

* [Tesseract](https://github.com/tesseract-ocr/tesseract) in path
* Languages for tesseract, for Finnish e.g. [dan_frak](https://github.com/paalberti/tesseract-dan-fraktur)


## Running of the script

    python tesse_wrap.py -i <inputfile>

as an output you get a texts of various example languages.


## Example file

You can use the sortavala.jpg , which originally is from
13.01.1844 Maamiehen Ystävä no 2 s. 4, and can be accessed from
[Digital collections of National Library of Finland](http://digi.kansalliskirjasto.fi/sanomalehti/binding/422224/articles/1535635)


## Todo

Incorporate omorfi in order to evaluate the goodness of the OCR against different language options.
