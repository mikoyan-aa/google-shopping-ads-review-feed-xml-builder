# Build a review feed XML for Google Shopping Ads
## Required
- Python >= 3.6
- requests
    - How to install
        ```shell
        pip install requests
        ```

## Help
```shell
./feed.py --help
usage: feed.py [-h] -k API_KEY -u URL -q QUERY_ID -r REVIEW_ID [-o OUTPUT] -n PUBLISHER_NAME [-f PUBLISHER_FAVICON]

Feed CSV via Redash API and emit XML file with a template

options:
  -h, --help            show this help message and exit
  -k API_KEY, --api-key API_KEY
                        RedashのAPIキー
  -u URL, --url URL     RedashのURL
  -q QUERY_ID, --query-id QUERY_ID
                        RedashのクエリID
  -r REVIEW_ID, --review-id REVIEW_ID
                        レビューID
  -v REVIEW_VIEW_ID, --review-view-id REVIEW_VIEW_ID
                        レビュービューID
  -o OUTPUT, --output OUTPUT
                        出力XMLファイル名
  -n PUBLISHER_NAME, --publisher-name PUBLISHER_NAME
                        パブリッシャー名
  -f PUBLISHER_FAVICON, --publisher-favicon PUBLISHER_FAVICON
                        パブリッシャー favicon URL
```

## How to run
```shell
./feed.py --query-id <RedashのクエリID> --api-key "<RedashのAPIキー>" -u "RedashのURL" --review-id <対象のレビューID> --review-view-id <対象のレビュービューID> --publisher-name <パブリッシャー名> --output <出力ファイル名>
```

## How to validate for created review feed XML file
- You need to install libxml2 open source library for using the `xmllint` command
```shell
xmllint --schema http://www.google.com/shopping/reviews/schema/product/2.3/product_reviews.xsd --noout /path/to/test.xml
```

## Files
### feed.py
The command.

### review_feed_header.xml
The header part of a review feed.

### review_feed_footer.xml
The footer part of a review feed.

### review_feed_template.xml
The template XML part file for a review feed.
