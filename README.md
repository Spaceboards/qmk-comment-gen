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
python3 gen.py ../qmk_firmware/keyboards/planck/keymaps/default/
```
