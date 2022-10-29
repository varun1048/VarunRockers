from .soupPage import makeSoup


def filterWithLinkPage(url) -> bool:
    return url[-1] == "0"


def getAllLinks(URL: str) -> list:
    soup = makeSoup(URL)
    links = [link.get("href") for link in soup.find_all("a")]
    return [*filter(filterWithLinkPage, links)]
