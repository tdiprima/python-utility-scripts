1) Load data into mongodb

```
 9182  mongoimport --host 127.0.0.1 --port 27017 --db camic --collection tumor_annotations < tumor_annotations1.json
 9183  mongoimport --host 127.0.0.1 --port 27017 --db camic --collection tumor_annotations < tumor_annotations2.json
 
```

Here's the Fix

```
 # Failed: error unmarshaling bytes on document #0: JSON decoder out of sync - data changing underfoot?
 mongoimport --jsonArray --host 127.0.0.1 --port 27017 --db camic --collection tumor_annotations < tumor_annotations1.json
 # do only for first file
```

396 records total.

 1a) Do some kind of conversion?
 
 ```
 9829  cp "hack.json" idk/tumor_annotations2.json
 ```

2) Export and load to mongo in container?

``` 
9186  mongoexport --host localhost --port 27017 --db camic --collection mark --out loadtumor2.json
9188  mongoexport --host localhost --port 27017 --db camic --collection mark --out loadtumor1.json
```

And then there was:

```
9839  mongoexport --host localhost --port 27017 --db camic --collection quip_tahsin_tumor_all --out quip_tahsin_tumor_all1.json
```

<hr>

```
db.tumor_annotations.distinct("provenance.image.case_id")

db.tumor_annotations.find().forEach(function(data) {
    //print(data.provenance.image.case_id.replace("VTRPDAC_Test_", ""))
    db.tumor_annotations.update({
        "_id": data._id
    }, {
        "$set": {
            "provenance.image.imageid": data.provenance.image.case_id.replace("VTRPDAC_Test_", ""),
            "provenance.image.study": data.provenance.image.case_id.replace("VTRPDAC_Test_", ""),
            "provenance.image.subject": data.provenance.image.case_id.replace("VTRPDAC_Test_", "")
        }
    });
    
})

```

```
root@904f2cadc585:/# mongoimport --host 127.0.0.1 --port 27017 --db camic --collection mark < tumor_annotations.json
2019-06-04T15:33:49.725+0000	connected to: 127.0.0.1:27017
2019-06-04T15:33:52.645+0000	imported 396 documents
root@904f2cadc585:/# rm tumor_annotations.json
```


<hr>

Nan Li<br>
For the human annotations, you don't need to convert to 3.0.<br>
We support 2.0 model.

But you need to add 3 fields.


I do get results for this though /data/Mark/types?slide="13"

What does rs look like?<br>
$D.overlayers

check a `dataloaders.js` -> `OverlayersLoader` method

error is on line 70

$CAMIC.store.findMarkTypes($D.params.data.name)

