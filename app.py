import argparse
from urllib.parse import urlparse
import sys
import qrcode


def is_valid_url(url: str) -> bool:
    """Basic URL validation."""
    try:
        parsed = urlparse(url)
        return all([parsed.scheme in ("http", "https"), parsed.netloc])
    except Exception:
        return False


def build_qr(
    data: str,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
):
    """
    Build a QR code image object using qrcode.
    Returns a PIL.Image instance.
    """
    qr = qrcode.QRCode(
        version=None,              # let the library pick the best version
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # good default
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument("-u", "--url", required=True, help="URL to encode")
    parser.add_argument(
        "-o", "--out", default="qr.png", help="Output image filename (e.g., qr.png)"
    )
    parser.add_argument("--box-size", type=int, default=10, help="Box size (pixels)")
    parser.add_argument("--border", type=int, default=4, help="Border width (boxes)")
    parser.add_argument("--fill", default="black", help="Foreground color")
    parser.add_argument("--back", default="white", help="Background color")

    args = parser.parse_args()

    if not is_valid_url(args.url):
        print("Error: Please provide a valid http(s) URL (e.g., https://example.com).")
        sys.exit(1)

    try:
        img = build_qr(
            data=args.url,
            box_size=args.box_size,
            border=args.border,
            fill_color=args.fill,
            back_color=args.back,
        )
        img.save(args.out)
        print(f"Success! QR code saved to: {args.out}")
    except Exception as e:
        print(f"Failed to generate QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()