# Lesson Plan Suggestion API from PDF Content using GPT-3.5 API

## Introduction

This project provides an API that suggests lesson plans based on the content of a PDF using GPT-3.5 API. The API is designed to generate insightful and useful lesson plan suggestions by processing the content of the provided PDF.

To use the API, you'll need to install the required dependencies listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```
## Usage

After installing the requirements, you can access the API endpoint using a GET request at the following URL format:
http://localhost:8000/course_plan/?url={pdf_url}
Replace {pdf_url} with the URL of the PDF you want to process. For example:
http://localhost:8000/course_plan/?url=https://www.ucl.ac.uk/teaching-learning/sites/teaching-learning/files/20161207-ucl-developing-short-courses-v4.pdf

Please note that the url query parameter must be a valid URL and should point to a valid PDF file. Additionally, this API is optimized for small PDF files and may not perform optimally with large ones.
