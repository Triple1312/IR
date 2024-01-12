# Search engine for papers using Pagerank

## Requirements
- venv required
- flask required
  - (inside activated venv run) `pip install flask`

## Setup
Environment variables:
```
FLASK_APP = search_engine/application.py:app
FLASK_ENV = development
FLASK_DEBUG = 0
```
Run from the root directory:

`python -m flask run --host=127.0.0.2 --port=1234 `


## Usage:
Homepage: http://127.0.0.2:1234

On the homepage you can input a search query, the page will redirect you to http://127.0.0.2:1234/search/your_search_query

That page will display the results ordered from most to least relevant according to pagerank. Shown are the name, a link
to the publication and the DOI.
