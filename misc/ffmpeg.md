# FFmpeg
## Video from Picture and Audio
```
ffmpeg -loop 1 -i beef-jerky.png -i beef-jerky.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -t 4.6 beef-jerky.mp4
```
stolen from [here](https://superuser.com/a/1041818)

used
[here](https://youtu.be/H6tRUa6dtZ8)
and
[here](https://youtu.be/qU5nELi_D_A)
