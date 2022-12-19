from argparse import ArgumentParser
from pathlib import Path

from .qmkcommentgen import gen_comment, paste_to_clipboard


def main():
    parser = ArgumentParser(description='Generate QMK firmware keymap comments')
    parser.add_argument('-i','--keymap-path', type=str, default='./', help='Path to keymap.c')
    parser.add_argument('-o', '--output-file', type=str, default='comment.txt', help='Comment file that is used to store keymap comments')
    parser.add_argument('--clipboard', action="store_true", help='Paste keymap to clipboard')
    parser.set_defaults(clipboard=False)

    args = parser.parse_args()

    keymap_path = Path(args.keymap_path)
    if keymap_path.is_dir():
        keymap_path = keymap_path / 'keymap.c'
    
    if not keymap_path.exists():
        print(f"Keymap path does not exist or is not readable ({args.keymap_path})")
        exit(1)
    
    output_file = Path(args.output_file)
    gen_comment(keymap_path, output_file)
    print(f'Done printing Keymap to: {output_file}')

    if args.clipboard:
        paste_to_clipboard(output_file)
        print('Added to Clipboard')
