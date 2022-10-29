import threading
import numpy as np

from .singlePage import getMoveInfo


class ThreadWithResult(threading.Thread):
    def __init__(self, target=None,  args=()):
        def function():
            self.result = target(args)
        super().__init__( target=function)


def getMovieInfoByList(links):
    return [getMoveInfo(movie) for movie in links]


def thread(links):
    threadsArr = np.array_split(links, round(len(links)/4))
    mainThred = [ThreadWithResult(target=getMovieInfoByList, args=links) for links in threadsArr]

    for x in mainThred:
        x.start()

    for x in mainThred:
        x.join()

    return [movie for movieArr in mainThred for movie in movieArr.result ]
