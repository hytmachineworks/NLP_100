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
> db.artist_col.find({name: "Queen"})			# query all name "Queen"
{'_id': ObjectId('5b5036f6268ff23b3c62cdf0'),
 'aliases': [{'name': 'Queen', 'sort_name': 'Queen'}],
 'area': 'Japan',
 'ended': True,
 'gender': 'Female',
 'gid': '420ca290-76c5-41af-999e-564d7c71f1a7',
 'id': 701492,
 'name': 'Queen',
 'sort_name': 'Queen',
 'tags': [{'count': 1, 'value': 'kamen rider w'},
          {'count': 1, 'value': 'related-akb48'}],
 'type': 'Character'}
{'_id': ObjectId('5b5036fa268ff23b3c63949c'),
 'aliases': [{'name': '女王', 'sort_name': '女王'}],
 'area': 'United Kingdom',
 'begin': {'date': 27, 'month': 6, 'year': 1970},
 'ended': True,
 'gid': '0383dadf-2a4e-4d10-a46a-e9e041da8eb3',
 'id': 192,
 'name': 'Queen',
 'rating': {'count': 24, 'value': 92},
 'sort_name': 'Queen',
 'tags': [{'count': 2, 'value': 'hard rock'},
          {'count': 1, 'value': '70s'},
          {'count': 1, 'value': 'queen family'},
          {'count': 1, 'value': '90s'},
          {'count': 1, 'value': '80s'},
          {'count': 1, 'value': 'glam rock'},
          {'count': 4, 'value': 'british'},
          {'count': 1, 'value': 'english'},
          {'count': 2, 'value': 'uk'},
          {'count': 1, 'value': 'pop/rock'},
          {'count': 1, 'value': 'pop-rock'},
          {'count': 1, 'value': 'britannique'},
          {'count': 1, 'value': 'classic pop and rock'},
          {'count': 1, 'value': 'queen'},
          {'count': 1, 'value': 'united kingdom'},
          {'count': 1, 'value': 'langham 1 studio bbc'},
          {'count': 1, 'value': 'kind of magic'},
          {'count': 1, 'value': 'band'},
          {'count': 6, 'value': 'rock'},
          {'count': 1, 'value': 'platinum'}],
 'type': 'Group'}
{'_id': ObjectId('5b503705268ff23b3c654ef4'),
 'ended': True,
 'gid': '5eecaf18-02ec-47af-a4f2-7831db373419',
 'id': 992994,
 'name': 'Queen',
 'sort_name': 'Queen'}
> db.artist_col.find({name: "Queen"},{name:1})		# query all name "Queen", but only shows name and id
{ "_id" : ObjectId("5b4b2533268ff2340c1baa52"), "name" : "Queen" }
{ "_id" : ObjectId("5b4b2535268ff2340c1c70fe"), "name" : "Queen" }
{ "_id" : ObjectId("5b4b2539268ff2340c1e2b56"), "name" : "Queen" }
> db.artist_col.find({name: "Queen"},{_id:0, name:1})	# query all name "Queen", but only shows name
{ "name" : "Queen" }
{ "name" : "Queen" }
{ "name" : "Queen" }
> exit							# start MongoDB shell
bye