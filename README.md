# qmk-comment-gen
Generates fancy layout comments for qmk keymaps

## Requirements
+ Python 3.6+
+ Keymap starts on a new line. Example:

```
[_HOME] = LAYOUT(

KC_NO, etc...
```

## How to use
### No install
```
git clone https://github.com/Spaceboards/qmk-comment-gen.git
cp /path/to/keymap.c qmk-comment-gen/keymap.c
./gen.py
```
The file `comment.txt` will be created with the generated comment
### Install with pip from source
```
git clone https://github.com/Spaceboards/qmk-comment-gen.git
cd qmk-comment-gen
pip install -U .
```
Then from anywhere
```
qgen -i ~/bin/qmk_firmware/keyboards/planck/keymaps/default/ -o planck_keymap_comment.txt
```

## What's new?
+ added support for multiple layers
+ Better boxes
+ Clipboard support

## Example
```
# Generate comments for the default planck keymap
python3 gen.py -i ../qmk_firmware/keyboards/planck/keymaps/default/
# Change the output file to planck.txt
python3 gen.py -i ../qmk_firmware/keyboards/planck/keymaps/default/ -o planck.txt
```

## Featured Fork
https://github.com/sjungq/qmk-comment-gen/tree/sjung
