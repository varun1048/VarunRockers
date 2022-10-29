from .soupPage import makeSoup


def getMoveInfo(URL) -> dict:
    soup = makeSoup(URL)
    title = soup.find("title").text
    if (title.find("Watch") != -1):
        return {}
    try:
        print(soup.find("title").text.split(" - ")[0])
        className = "ipsType_normal ipsType_richText ipsPadding_bottom ipsContained"
        div = soup.find("div", {"class", className})
        images = [x.get("src") for x in div.find_all("img")]
        downloadLinks = div.find_all("a", {"data-fileext": "torrent"})
        downloadLinks = list(
            map(lambda a: {"size": a.text, "link": a.get("href"), }, downloadLinks))
        # for x in downloadLinks:
        #     print(x)
        return {
            "title": soup.find("title").text.split(" - ")[0],
            "image": images[0],
            "downloadLinks": downloadLinks[0],
            # "allDownloadLinks":downloadLinks,
            # "allImage":images,
            # "fullTitle": soup.find("title").text,
        }
    except Exception as err:
        print(URL)
        print(err)
        return {}

# def getMoveInfo(URL) -> dict:
#     soup = makeSoup(URL)
#     title = soup.find("title").text
#     print(title)
#     print(title.find("Watch")==-1)
#     print()
#     return {}
