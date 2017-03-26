# Stackoverflow Documentation to PDF

Scrape Stackoverflow documentation website to convert each topic of a desired language to the formatted and printable PDF

**Python Documentation (185 topics) as PDF has already scraped and formatted**

Go to /pdf to print the complete stackoverflow documentation for Python, cheers :)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Use requirements.txt for package information and versions

```
[requirements.txt](/requirements.txt)
```

### Configuration

Use config.py for package configuration for the following variables.

```
LOG_FILE: Path of log file
default: .log
```

```
LOG_FORMAT: For logging format of logger
default: %(asctime)s | %(name)s | %(levelname)s | %(funcName)s | %(lineno)d | %(message)s
```

```
**Change URL according to the documentation you may require as PDF**

URL: Python Documentation to scrape, read main.py docstring for further info.
default: http://stackoverflow.com/documentation/python/topics
```

```
PDF_OPTIONS: Formatiing options for PDF
default:
{
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'javascript-delay': 1000
}
```

### Installing

Nothing out of the box, just run the main python script as following

```
python main.py
```

And then, wait for get finished and PDFs are ready to print in ` /pdf ` folder

## Built With

* [PDFkit](https://pypi.python.org/pypi/pdfkit) - Python wrapper to convert html to pdf
* [Requests](http://docs.python-requests.org/en/master/) - For HTTP requests
* [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4) - Screen scraping library

## Contributing

Please read [CONTRIBUTING](/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Abhinav Walia** - *Initial work* - [Abhinav @ Github](https://github.com/abhinavwalia95)

## Acknowledgments

* Inspired by e-satis
