import json
from soup1tamilmv.index import movieList

mList = movieList()
result = json.dumps(mList,indent=3)
print(result)
