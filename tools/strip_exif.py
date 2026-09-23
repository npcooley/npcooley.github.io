#!/usr/bin/env python3
"""Strip ALL embedded metadata (EXIF, including GPS location) from an image.

Usage:
    python3 tools/strip_exif.py INPUT OUTPUT [--force]

Behavior, stated explicitly:
  * INPUT is never modified.
  * OUTPUT is not overwritten unless --force is given.
  * The image is rebuilt from raw pixel data only, so no metadata can be
    carried over by accident. Camera orientation is applied to the pixels
    first, so the picture does not end up rotated.
  * The result is re-opened and verified to contain no EXIF before the
    script reports success. If verification fails, OUTPUT is deleted and the
    script exits non-zero.
  * JPEG output is re-encoded (quality 92), which is slightly lossy.

Requires: Pillow  (pip install pillow)
"""
import argparse
import os
import sys

from PIL import Image, ImageOps

GPS_IFD_TAG = 0x8825  # standard EXIF tag that points at the GPS block


def strip_metadata(src_path, dst_path, force):
    if not os.path.isfile(src_path):
        raise FileNotFoundError("Input file not found: %s" % src_path)
    if os.path.abspath(src_path) == os.path.abspath(dst_path):
        raise ValueError("INPUT and OUTPUT must be different files.")
    if os.path.exists(dst_path) and not force:
        raise FileExistsError("Output exists (use --force to overwrite): %s" % dst_path)

    with Image.open(src_path) as original:
        oriented = ImageOps.exif_transpose(original)
        # Copy pixels only; nothing from original.info / original.getexif().
        clean = Image.frombytes(oriented.mode, oriented.size, oriented.tobytes())
        save_kwargs = {}
        if dst_path.lower().endswith((".jpg", ".jpeg")):
            if clean.mode not in ("RGB", "L"):
                clean = clean.convert("RGB")
            save_kwargs = {"quality": 92, "optimize": True}
        clean.save(dst_path, **save_kwargs)

    # Verify rather than assume.
    with Image.open(dst_path) as check:
        exif = check.getexif()
        if len(exif) != 0 or bool(exif.get_ifd(GPS_IFD_TAG)):
            os.remove(dst_path)
            raise RuntimeError("Verification failed: metadata still present; output removed.")


def main():
    parser = argparse.ArgumentParser(description="Strip EXIF/GPS metadata from an image.")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--force", action="store_true", help="overwrite OUTPUT if it exists")
    args = parser.parse_args()
    try:
        strip_metadata(args.input, args.output, args.force)
    except (OSError, ValueError, RuntimeError) as err:
        print("ERROR: %s" % err, file=sys.stderr)
        return 1
    print("OK: wrote %s (verified: no EXIF or GPS data)" % args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
