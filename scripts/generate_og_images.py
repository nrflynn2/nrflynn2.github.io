"""Generate branded OG social sharing images (1200x630) for key pages."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "assets" / "img"
BRAND_DIR = IMG_DIR / "brand"
OG_DIR = IMG_DIR / "og"
OG_DIR.mkdir(parents=True, exist_ok=True)

WIDTH, HEIGHT = 1200, 630

# Teal gradient colors
TEAL_DARK = (10, 100, 95)
TEAL_MID = (13, 148, 136)
TEAL_LIGHT = (20, 184, 166)
WHITE = (255, 255, 255)
WHITE_DIM = (255, 255, 255, 180)


def teal_gradient(width: int, height: int) -> Image.Image:
    """Create a left-to-right teal gradient background."""
    img = Image.new("RGB", (width, height))
    for x in range(width):
        t = x / width
        r = int(TEAL_DARK[0] + (TEAL_LIGHT[0] - TEAL_DARK[0]) * t)
        g = int(TEAL_DARK[1] + (TEAL_LIGHT[1] - TEAL_DARK[1]) * t)
        b = int(TEAL_DARK[2] + (TEAL_LIGHT[2] - TEAL_DARK[2]) * t)
        ImageDraw.Draw(img).line([(x, 0), (x, height)], fill=(r, g, b))
    return img


def paste_ark_mark(base: Image.Image, x: int, y: int, size: int, opacity: int = 180):
    """Overlay the ark illustration at (x, y) scaled to `size` px wide, at given opacity."""
    ark_path = BRAND_DIR / "02_ark_illustration_transparent.png"
    if not ark_path.exists():
        return
    ark = Image.open(ark_path).convert("RGBA")
    w, h = ark.size
    new_h = int(size * h / w)
    ark = ark.resize((size, new_h), Image.LANCZOS)
    # Apply opacity
    r, g, b, a = ark.split()
    a = a.point(lambda v: int(v * opacity / 255))
    ark = Image.merge("RGBA", (r, g, b, a))
    base.paste(ark, (x, y), ark)


def load_font(size: int) -> ImageFont.FreeTypeFont:
    """Load a system font, falling back to default."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
    ]
    for fp in font_paths:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def load_font_regular(size: int) -> ImageFont.FreeTypeFont:
    """Load a regular weight system font."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ]
    for fp in font_paths:
        if Path(fp).exists():
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def circular_crop(img: Image.Image, size: int) -> Image.Image:
    """Crop an image into a circle."""
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size, size], fill=255)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(img, mask=mask)
    return result


def generate_default():
    """Default OG image: name, title, profile photo."""
    img = teal_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)

    # Ark mark in top-right corner
    paste_ark_mark(img, WIDTH - 240, 20, size=220)

    # Profile photo (circular, right side)
    try:
        prof = Image.open(IMG_DIR / "prof_pic.jpg")
        prof_circle = circular_crop(prof, 200)
        img.paste(prof_circle, (WIDTH - 280, HEIGHT // 2 - 100), prof_circle)
    except Exception:
        pass

    # Text
    font_title = load_font(56)
    font_subtitle = load_font_regular(28)
    font_url = load_font_regular(22)

    draw.text((80, 180), "Noah Flynn", fill=WHITE, font=font_title)
    draw.text((80, 260), "Applied Scientist, AWS AI Labs", fill=WHITE_DIM, font=font_subtitle)
    draw.text(
        (80, 310),
        "Author of Machine Learning for Drug Discovery",
        fill=WHITE_DIM,
        font=font_subtitle,
    )
    draw.text((80, HEIGHT - 70), "noahrflynn.com", fill=WHITE_DIM, font=font_url)

    img.save(OG_DIR / "default.png", "PNG")
    print(f"  Created {OG_DIR / 'default.png'}")


def generate_book():
    """Book page OG image: book cover + title."""
    img = teal_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)

    paste_ark_mark(img, WIDTH - 240, 20, size=220)

    # Book cover (left side) — use Manning cover PNG if available, fall back to JPEG
    try:
        cover_path = IMG_DIR / "book_cover_manning.png"
        if not cover_path.exists():
            cover_path = IMG_DIR / "book_cover.jpg"
        cover = Image.open(cover_path)
        cover_h = 420
        cover_w = int(cover.width * cover_h / cover.height)
        cover = cover.resize((cover_w, cover_h), Image.LANCZOS)
        img.paste(cover, (80, (HEIGHT - cover_h) // 2))
        text_x = 80 + cover_w + 60
    except Exception:
        text_x = 80

    font_title = load_font(42)
    font_subtitle = load_font_regular(24)
    font_url = load_font_regular(22)

    draw.text((text_x, 160), "Machine Learning", fill=WHITE, font=font_title)
    draw.text((text_x, 215), "for Drug Discovery", fill=WHITE, font=font_title)
    draw.text(
        (text_x, 290),
        "Hands-on ML and deep learning",
        fill=WHITE_DIM,
        font=font_subtitle,
    )
    draw.text(
        (text_x, 325),
        "for pharmaceutical research",
        fill=WHITE_DIM,
        font=font_subtitle,
    )
    draw.text((text_x, 390), "Noah Flynn", fill=WHITE, font=font_subtitle)
    draw.text((80, HEIGHT - 70), "noahrflynn.com/book", fill=WHITE_DIM, font=font_url)

    img.save(OG_DIR / "book.png", "PNG")
    print(f"  Created {OG_DIR / 'book.png'}")


def generate_publications():
    """Publications page OG image."""
    img = teal_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)

    # Ark marks as background pattern (three at different sizes/positions)
    paste_ark_mark(img, WIDTH - 260, 20, size=240)
    paste_ark_mark(img, WIDTH - 420, 360, size=190, opacity=120)
    paste_ark_mark(img, WIDTH - 160, 320, size=150, opacity=100)

    font_title = load_font(56)
    font_subtitle = load_font_regular(28)
    font_url = load_font_regular(22)

    draw.text((80, 200), "Publications", fill=WHITE, font=font_title)
    draw.text((80, 280), "Noah Flynn", fill=WHITE_DIM, font=font_subtitle)
    draw.text(
        (80, 325),
        "ML for drug discovery, NLU, foundation models",
        fill=WHITE_DIM,
        font=font_subtitle,
    )
    draw.text((80, HEIGHT - 70), "noahrflynn.com/publications", fill=WHITE_DIM, font=font_url)

    img.save(OG_DIR / "publications.png", "PNG")
    print(f"  Created {OG_DIR / 'publications.png'}")


if __name__ == "__main__":
    print("Generating OG images...")
    generate_default()
    generate_book()
    generate_publications()
    print("Done!")
