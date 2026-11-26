# Craigslist Pittsburgh Apartments Scraper

Minimal Scrapy spider that extracts apartment listings (title, price, location) from the Pittsburgh Craigslist search page.

## Status of the Original Solution

The original exercise solution uses this selector:

```python
response.xpath("//li[@class='cl-static-search-result']")
```

This **no longer works**. Craigslist has changed the page structure. Current results use:

```html
<div class="cl-search-result" data-pid="..." title="...">
```

## Updated Spider

See `craigslist-scraper.py` for a version with current selectors.

## Requirements

```bash
pip install scrapy
```

## Run

```bash
scrapy runspider craigslist-scraper.py -O out.csv
```

## Output Fields

- `title`
- `price`
- `location`
- `pid` (posting ID)
- `url`

## Notes

- Craigslist changes its HTML often — selectors may need updating again.
- Basic Scrapy may miss dynamically loaded results.
- For educational use only. Respect Craigslist’s terms of service.
