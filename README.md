# SevenSegTools
A set of tools and fonts intended to make working with Seven Segments displays easier and faster.

This project is currently on its pretty early stages, so don't expect to find something useful in here at this time.

## Fonts
The fonts are files that contain characters and their corresponding seven segment display representation.

Each line in the file is interpreted as a character, unless it begins with a `/`.

The first character of a line is the character that will be represented, and the other characters represent the segments of a SSD, in groups of 7 characters, using only `1` and `0`, with `1` meaning it should be lit and `0` meaning it shouldn't.

Each line can have multiple groups of 7 characters for alternate representations of the same character.

The available fonts are in [the ./fonts folder](fonts), and currently are [numbers](fonts/numbers) and [alphabet](fonts/alphabet).

### Segments

The following diagram represents how the segments are labeled on an SSD.

```
 ##a##
#     #
f     b
#     #
 ##g##
#     #
e     c
#     #
 ##d##  #(d)
```

Note that there are actually 8 'segments' on most seven segments displays, with the 8th segment being the decimal point (d).

That extra segment, however, isn't included in the font files, as it's not considered a part of the character itself.

### Example
```
/ abcdefg
7 1110000 1110010
```

The example above describes the character 7 (the first character of the line) as either `1110000` or `1110010`, and the first line of the example begins with `/`, so it's ignored and can be used as a comment.

## Instructions
For running the Python files, first activate the virtual environment (venv) by running `source .venv/bin/activate`.

Once done, deactivate the venv by running `deactivate`.

## Roadmap
- [x] Fonts
  - [x] Numbers
  - [x] Alphabet
- [ ] Tool
  - [ ] Font configuration
  - [ ] Font preview
  - [ ] Font editing
  - [ ] Font exporting
    - [ ] C ready
