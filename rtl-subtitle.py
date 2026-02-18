# Right-to-left subtitles by adding the RLE character to each sentence. Doing this is required 
#  when integrating subtitles by video editors such as ffmpeg. 
# Make sure to replace 'sample_subtitle.srt' with the path to your input SRT file and 
#  'output_subtitle.srt' with the desired output file path.
# By https://twitter.com/NabiKAZ
# Source: https://github.com/NabiKAZ/RTL-subtitle
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("outfile")
    args = parser.parse_args()
    input_file = args.infile
    output_file = args.outfile
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

