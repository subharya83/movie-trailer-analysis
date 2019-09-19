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
