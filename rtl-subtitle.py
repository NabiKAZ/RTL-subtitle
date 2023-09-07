# This script solves the problem of formatting subtitles in right-to-left languages, making them compatible with video editing software 
#  like FFmpeg. By adding the RLE character at the beginning of each text line while preserving the timestamps, it ensures that 
#  the subtitles display correctly in the intended right-to-left direction when overlaid on video content. This formatting is crucial 
#  for maintaining the legibility and visual integrity of subtitles in languages that use a right-to-left writing system.
# Add the UTF-16 encoding character 0x202B (RLE) (which represents the "RIGHT-TO-LEFT EMBEDDING" control character) only to the lines 
#  containing text and not to the timestamp lines in your SRT file.
# Make sure to replace 'sample_subtitle.srt' with the path to your input SRT file and 'output_subtitle.srt' with the desired 
#  output file path.
# By https://twitter.com/NabiKAZ
# MIT License

def add_rle_to_paragraphs(srt_content, rle_char):
    paragraphs = srt_content.strip().split('\n\n')
    modified_paragraphs = []

    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        modified_lines = []

        for i, line in enumerate(lines):
            # Check if the line contains text (not a timestamp line)
            if i == 0 or (i == 1 and '-->' in line):
                modified_lines.append(line)
            else:
                modified_lines.append(f"{rle_char}{line}")

        modified_paragraphs.append('\n'.join(modified_lines))

    return '\n\n'.join(modified_paragraphs)

def main():
    input_file = 'sample_subtitle.srt'
    output_file = 'output_subtitle.srt'
    rle_char = '\u202B'  # Use the UTF-16 encoding character.

    with open(input_file, 'r', encoding='utf-8') as file:
        srt_content = file.read()

    modified_srt_content = add_rle_to_paragraphs(srt_content, rle_char)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_srt_content)

    print(f"RLE character '{rle_char}' added to the beginning of each text line in paragraphs.")
    print(f"Modified content saved to '{output_file}'.")

if __name__ == "__main__":
    main()
