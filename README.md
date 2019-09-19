# Dataset Creation 

## Videos
1. Downloading videos IDs from YouTube for a given channel id:
```
youtube-dl -i --get-id https://www.youtube.com/user/MovieclipsTrailers | tee output.txt
```
2. Downloading videos IDs uploaded after a particular date (YYYYMMDD):
```
youtube-dl -i --dateafter 20180701 --get-id https://www.youtube.com/user/MovieclipsTrailers | tee <output.txt>
```
3. Getting videos from YouTube according to a file containing YouTube Ids
```
youtube-dl -i --output "YTID_%(id)s.%(ext)s" -a output.txt -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
```
4. Converting videos in other formats to mp4
```
for i in `ls *.webm`; do x=`echo $i|sed 's/\.webm/\.mp4/g'`; ffmpeg -y -i $i -crf 5 -strict -2 $x; done
```
## Statistics


## Cleaning up Metadata index file 

### Extract years from Title Field
```
import pandas as pd
import re
df = pd.read_csv('MTMI.tsv', sep='\t')
ttl = df.iloc[:, -1]
_years = [y.group(0) if y is not None else None for y in (re.search('\([1-9][0-9][0-9][0-9]\)', t) for t in ttl)]
_years = [int(y.replace('(', '').replace(')', '')) if y is not None else None for y in _years]
```

### Clean up VideoId Title field to extract movie title
```
#!/bin/bash
#Initial Clean-up
for x in `seq 0 5202`; 
  do x=`jq .Title.\"$x\" MTMI.json|sed -e 's/\(Official\|International\|Final\|Comic-Con\|Teaser\|Red Band\|Movie\).* Trailer.*$//g'`;
  echo $x; 
done |tee  Titles-only.txt
```

#Followup clean up
