# TODO

* single quotes don't work in CL searches. Must use double quotes only. Is there
a way to clean input so single quotes are treated as double quotes? Or perhaps
add a `exact_phrase` boolean option?

* Let user specify ALL possible CL search options: Price range, ZIP code, beds,
baths, etc. Don't forget: Availability and Open House (sale_date) dates.

* Let user specify which variables, how many pages, and how many ads to scrape.

* Decide: Should timestamps reflect when each ad was scraped, or when the search
began? The former differs across *pages* when `deep=False` and differs across
*ads* when `deep=True`. But `post_id` already uniquely IDs ads and I don't need
an identifer for pages. If I change timestamps to reflect search begin time,
they'll differ across search objects. Is that desirable?

* Replace `requests` dependency with `urllib3`? Because minimalism.

* CLI
