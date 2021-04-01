# FFmpeg
## video from image and audio
```
ffmpeg -loop 1 -i beef-jerky.png -i beef-jerky.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 4.6 beef-jerky.mp4
```
stolen from [here](https://superuser.com/a/1041818)

used
[here](https://youtu.be/H6tRUa6dtZ8)
and
[here](https://youtu.be/qU5nELi_D_A)

## scale volume
```
ffmpeg -i mclp-lab2.mp4 -filter:a "volume=4.0" out.mp4
```
stolen from [here](https://trac.ffmpeg.org/wiki/AudioVolume)

used [here](https://youtu.be/g0ekDsVZfao)

## burn subtitles
```
ffmpeg -i mclp-lab3.mp4 -vf subtitles=front.srt out.mp4
```
stolen from [here](https://trac.ffmpeg.org/wiki/HowToBurnSubtitlesIntoVideo)

used [here](https://youtu.be/Cnu2-CKAoQc)

## transpose
```
ffmpeg -i owo.mp4 -vf "transpose=2" uwu.mp4
```
stolen from [here](https://stackoverflow.com/a/9570992)

used [here](https://youtu.be/Fl8sh9ZEO1c)

## gif from images
```
ffmpeg -i %d.png unknown.gif
```
stolen from [here](https://unix.stackexchange.com/a/24103)

used to show off phased-bars

## trim
```
ffmpeg -i mclp-lab6-pre.mkv -ss 00:00:04 -to 00:00:25 mclp-lab6.mkv
```
stolen from
[here](https://www.arj.no/2018/05/18/trimvideo/)
and
[here](https://superuser.com/a/377407)

used [here](https://youtu.be/Ez2xXMEVg40)

## re-encode as mp3
```
ffmpeg -i hi_this_is_healslug.mp3 -c:a libmp3lame -b:a 192k mikle-healslug.mp3
```
stolen from [here](https://askubuntu.com/a/1200496)

used... where?

## get video dimensions
```
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 input.mkv
```
stolen from [here](https://superuser.com/a/841379)

used to check Open Broadcaster Software output
