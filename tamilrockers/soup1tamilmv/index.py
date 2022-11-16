from .thread import thread
from .singlePage import getMoveInfo
from .homePage import getAllLinks


def movieList(domain, length):
    print("varun rockers")
    mainURL = f"https://www.1tamilmv.{domain}"
    links = getAllLinks(mainURL)
    return [*filter(None, thread(links[:length]))]
