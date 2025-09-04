import argparse
from urllib.parse import urlparse
import sys
import qrcode


def is_valid_url(url: str) -> bool:
    """Basic URL validation."""
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and parsed.netloc
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument("-u", "--url", required=True, help="URL to encode")
    args = parser.parse_args()

    if not is_valid_url(args.url):
        print("Error: Please provide a valid http(s) URL (e.g., https://example.com).")
        sys.exit(1)

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(args.url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr.png")

        print("✅ Success! QR code saved to qr.png")
    except Exception as e:
        print(f"❌ Failed to generate QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
