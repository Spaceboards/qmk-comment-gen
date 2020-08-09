from argparse import ArgumentParser
from pathlib import Path

import qmkcommentgen


if __name__ == "__main__":
    parser = ArgumentParser(description='Generate QMK firmware keymap comments')
    parser.add_argument('keymappath', type=str, help='Path to keymap.c')
    parser.add_argument('-o', '--output-file', type=str, default='comment.txt', help='Comment file that is used to store keymap comments')
    parser.add_argument('--clipboard', action="store_true", help='Paste keymap to clipboard')

    args = parser.parse_args()

    keymap_path = Path(args.keymappath, 'keymap.c')
    if not keymap_path.exists():
        print(f"Keymap path does not exist or is not readable ({keymap_path})")
        exit(1)
    
    output_file = Path(args.output_file)
    qmkcommentgen.gen_comment(keymap_path, output_file)
    print(f'Done printing Keymap to: {output_file}')

    if args.clipboard:
        qmkcommentgen.paste_to_clipboard(output_file)
        print('Added to Clipboard')
