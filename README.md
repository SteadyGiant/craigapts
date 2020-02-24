# craigapts

Python package for scraping apartment data from Craigslist.

## Install

Stable version from PyPI:

```sh
pip install craigapts
```

```sh
conda install -c everet craigapts
```

Dev version from GitLab:

```sh
pip install git+https://gitlab.com/everetr/craigapts.git
```

## Examples

```python3

from craigapts import CLSearch

GEO   = "newjersey"
QUERY = "'no section 8'"

# get basic data available on search result pages
c1 = CLSearch(GEO, QUERY)
print(c1.data)

# get details by navigating to each individual ad
c2 = CLSearch(GEO, QUERY, deep=True)
print(c2.data)

```

## Changelog

2020.2.23.1

* First release.

## TODO

* Add list of CL geographies
* Let user specify which variables, how many pages, and how many ads to scrape
* CLI