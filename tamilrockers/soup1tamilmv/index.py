from .thread import thread
from .singlePage import getMoveInfo
from .homePage import getAllLinks

def movieList(length):
    mainURL = "https://www.1tamilmv.cfd"
    links = getAllLinks(mainURL)
    print("Varun Rockers")
    # moviesInfo = [getMoveInfo(movie) for movie in links[:10]]
    # moviesInfo = [*filter(None, moviesInfo)]  # removing emty dict
    # return moviesInfo
    return  [*filter(None, thread(links[:length]))]


