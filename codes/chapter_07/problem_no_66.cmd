> mongo							# start MongoDB shell
> db							# check used db
test							# default db name
> use artist_db						# switch to artist_db
> db							# check used db
artist_db
> db.stats()						# database's statisfic data
{
        "db" : "artist_db",
        "collections" : 1,
        "views" : 0,
        "objects" : 921337,
        "avgObjSize" : 189.68956201693842,
        "dataSize" : 174768012,
        "storageSize" : 104701952,
        "numExtents" : 0,
        "indexes" : 5,
        "indexSize" : 40226816,
        "fsUsedSize" : 57783078912,
        "fsTotalSize" : 124881256448,
        "ok" : 1
}
> show collections					# check collections
artist_col
> db.artist_col.find({"area": "Japan"}).count()             # count up area is Japan
22821
> exit							# start MongoDB shell
bye