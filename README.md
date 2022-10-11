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
+ run gen.py
+ open comment.txt

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
