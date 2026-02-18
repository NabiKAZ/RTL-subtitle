# Right-to-left subtitles
This script solves the problem of formatting subtitles in right-to-left languages, making them compatible with video editing software like `FFmpeg`. By adding the `RLE` character at the beginning of each text line while preserving the timestamps, it ensures that the subtitles display correctly in the intended right-to-left direction when overlaid on video content. This formatting is crucial for maintaining the legibility and visual integrity of subtitles in languages that use a right-to-left writing system.

The UTF-16 encoding character `0x202B` (`RLE`) (which stands for the "RIGHT-TO-LEFT EMBEDDING" control character) is only added to text-containing lines and not to timestamp lines in your `SRT` file.

## Usage
To convert `input_subtitle.srt` to `output_subtitle.srt`, run:
```
python rtl-subtitle.py input_subtitle.srt output_subtitle.srt
```

## FFmpeg
Integrate right-to-left subtitles with ffmpeg if you want. Use this simple command:
```
ffmpeg -i "sample.mp4" -vf "subtitles='output_subtitle.srt'" "sample_output.mp4"
```
Or this more advanced command:
```
ffmpeg -i "sample.mp4" -vf "subtitles='output_subtitle.srt':force_style='FontName=vazir,Fontsize=30,PrimaryColour=&Hffffff&'" -ss 00:00:00 -to 00:00:20 -c:v libx264 -c:a aac -b:v 300k -b:a 48k -y "sample_output.mp4"
```

## Sample
Before:

![mpc-hc64_3FRBHbsOTc](https://github.com/NabiKAZ/RTL-subtitle/assets/246721/9a1f3316-2ba3-4cc2-ae17-35325b5fd8d9)

After RTL:

![mpc-hc64_WPTwJY4e5X](https://github.com/NabiKAZ/RTL-subtitle/assets/246721/8842f66a-1b20-4f89-98ca-75d938867a10)

## License
By https://twitter.com/NabiKAZ

MIT License

## Donation
If this project was useful for you and you are willing, you can make me happy by giving a Star at the top of this GitHub page. \
Also this is my wallet address for Donate: \
USDT (TRC20): `TEHjxGqu5Y2ExKBWzArBJEmrtzz3mgV5Hb`
