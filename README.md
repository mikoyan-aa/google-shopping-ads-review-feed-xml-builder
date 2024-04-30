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
usage: feed.py [-h] -k API_KEY [-u URL] -q QUERY_ID [-o OUTPUT]

Feed CSV via Redash API and emit XML file with a template

options:
  -h, --help            show this help message and exit
  -k API_KEY, --api-key API_KEY
                        RedashのAPIキー
  -u URL, --url URL     RedashのURL
  -q QUERY_ID, --query-id QUERY_ID
                        RedashのクエリID
  -o OUTPUT, --output OUTPUT
                        出力XMLファイル名
```

## How to run
```shell
./feed.py --query-id <RedashのクエリID> --api-key "<RedashのAPIキー>" -u "RedashのURL" > <出力ファイル名.xml>
```

## How to validate for created review feed XML file
- You need to install libxml2 open source library for using the `xmllint` command
```shell
xmllint --schema http://www.google.com/shopping/reviews/schema/product/2.3/product_reviews.xsd --noout test.xml
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