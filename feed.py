#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import requests
import sys

xmlTemplate = "review_feed_template.xml"
xmlHeader = "review_feed_header.xml"
xmlFooter = "review_feed_footer.xml"


def parseArgs():
    parser = argparse.ArgumentParser(
        description="Feed CSV via Redash API and emit XML file with a template"
    )

    parser.add_argument("-k", "--api-key", type=str, required=True, help="RedashのAPIキー")
    parser.add_argument("-u", "--url", type=str, required=True, help="RedashのURL")
    parser.add_argument(
        "-q", "--query-id", type=int, required=True, help="RedashのクエリID"
    )
    parser.add_argument("-r", "--review-id", type=int, required=True, help="レビューID")
    parser.add_argument("-o", "--output", type=str, help="出力XMLファイル名")
    parser.add_argument(
        "-n", "--publisher-name", type=str, required=True, help="パブリッシャー名"
    )
    parser.add_argument(
        "-f",
        "--publisher-favicon",
        type=str,
        required=False,
        help="パブリッシャー favicon URL",
    )

    args = parser.parse_args()

    apiKey = args.api_key
    baseUrl = args.url.rstrip("/")
    queryId = args.query_id
    reviewId = args.review_id
    xmlFilename = args.output
    pubName = args.publisher_name
    pubFav = args.publisher_favicon

    return {
        "apiKey": apiKey,
        "baseUrl": baseUrl,
        "queryId": queryId,
        "reviewId": reviewId,
        "xmlFilename": xmlFilename,
        "pubName": pubName,
        "pubFav": pubFav,
    }

def getReviews(baseUrl, apiKey, queryId, reviewId):
    endPoint = f"{baseUrl}/api/queries/{queryId}/results"
    httpHeaders = {
        "Authorization": f"{apiKey}",
        "Content-Type": "application/json",
    }
    postData = {
        "parameters": {
            "review_id": f"{reviewId}",
        }
    }
    postJson = json.dumps(postData)

    response = requests.post(endPoint, headers=httpHeaders, data=postJson)
    if response.status_code != 200:
        print(f"Error: {response.status_code} is sent from {endPoint}")
        sys.exit(1)

    jsonResult = response.json()

    return jsonResult["query_result"]["data"]["rows"]

def getReviewTemplate():
    with open(xmlTemplate, "r") as file:
        template = file.read()
    return template

def buildReviews(reviews):
    template = getReviewTemplate()

    feedXml = ""
    for review in reviews:
        chunk = template
        for key, value in review.items():
            placeHolder = "__" + key.upper() + "__"
            chunk = chunk.replace(placeHolder, str(value))
        feedXml = feedXml + chunk

    return feedXml

def buildFeedHeader(pubName, pubFav):
    with open(xmlHeader, "r") as file:
        header = file.read()

    header.replace("__PUBLISHER_NAME__", pubName)
    if pubFav is not None:
        header.replace("__PUBLISHER_FAVICON__", pubFav)

    return header

def getFeedFooter():
    with open(xmlFooter, "r") as file:
        footer = file.read()

    return footer

def main():
    args = parseArgs()

    reviews = getReviews(
        args["baseUrl"], args["apiKey"], args["queryId"], args["reviewId"]
    )

    reviewXml = buildReviews(reviews)
    headerXml = buildFeedHeader(args['pubName'], args['pubFav'])
    footerXml = getFeedFooter()
    builtXml = headerXml + reviewXml + footerXml

    if args["xmlFilename"] is not None:
        with open(args["xmlFilename"], "w") as file:
            file.write(builtXml)
    else:
        print(builtXml)


if __name__ == "__main__":
    main()
