from PIL import Image, ImageDraw, ImageFont
import textwrap
from argparse import ArgumentParser
import os

def run(meme_temp_path, top_text, bottom_text):

  # Taking the meme template
  meme_temp = Image.open(meme_temp_path)
  draw_meme_temp = ImageDraw.Draw(meme_temp)
  meme_temp_width, meme_temp_height = meme_temp.size
  font = ImageFont.truetype(font="/font/impact.ttf", size=int(meme_temp_height/20))

  # Taking argument
  top_text = top_text.upper()
  bottom_text = bottom_text.upper()
  char_width, char_height = font.getsize('A')
  chars_per_line = meme_temp_width // char_width
  top_lines = textwrap.wrap(top_text, width=chars_per_line)
  bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

  # where to write text
  y = 10
  for line in top_lines:
      line_width, line_height = font.getsize(line)
      # to make the line on center
      x = (meme_temp_width - line_width)/2
      draw_meme_temp.text((x,y), line, fill='white', font=font)
      y += line_height

  y = meme_temp_height - char_height * len(bottom_lines) - 15
  for line in bottom_lines:
      line_width, line_height = font.getsize(line)
      x = (meme_temp_width - line_width)/2
      draw_meme_temp.text((x,y), line, fill='white', font=font)
      y += line_height
  meme_temp.show()
  return meme_temp.save('meme generated - ' + meme_temp.filename.split('/')[-1])

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("--path", type=str)
  parser.add_argument("--top_text", type=str)
  parser.add_argument("--bottom_text", type=str)
  args = parser.parse_args()
  run(meme_temp_path = args.path,
      top_text = args.top_text,
      bottom_text = args.bottom_text)
