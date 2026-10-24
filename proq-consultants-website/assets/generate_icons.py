from PIL import Image, ImageDraw, ImageFilter

NAVY = (10, 31, 61)
TEAL = (10, 155, 138)
SKY = (79, 184, 232)

src = Image.open("logo.png").convert("RGBA")

# --- Crop just the icon mark (left portion before the wordmark starts) ---
icon_crop = src.crop((0, 0, 138, 47))
bbox = icon_crop.getbbox()
icon_crop = icon_crop.crop(bbox)

def square_canvas(img, size, bg=None, pad_ratio=0.16):
    pad = int(size * pad_ratio)
    avail = size - pad * 2
    w, h = img.size
    scale = min(avail / w, avail / h)
    new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), bg if bg else (0, 0, 0, 0))
    canvas.paste(resized, ((size - new_w) // 2, (size - new_h) // 2), resized)
    return canvas

# Transparent favicons (crisp on any browser chrome)
favicon_16 = square_canvas(icon_crop, 16, pad_ratio=0.08)
favicon_32 = square_canvas(icon_crop, 32, pad_ratio=0.08)
favicon_16.save("favicon-16x16.png")
favicon_32.save("favicon-32x32.png")

ico_sizes = [(16, 16), (32, 32), (48, 48)]
ico_imgs = [square_canvas(icon_crop, s[0], pad_ratio=0.08) for s in ico_sizes]
ico_imgs[0].save("favicon.ico", sizes=ico_sizes)

# Solid-background app icons (navy, so iOS/Android masks look intentional)
apple_touch = square_canvas(icon_crop, 180, bg=NAVY + (255,), pad_ratio=0.22)
apple_touch.convert("RGB").save("apple-touch-icon.png")

android_192 = square_canvas(icon_crop, 192, bg=NAVY + (255,), pad_ratio=0.22)
android_512 = square_canvas(icon_crop, 512, bg=NAVY + (255,), pad_ratio=0.22)
android_192.convert("RGB").save("android-chrome-192x192.png")
android_512.convert("RGB").save("android-chrome-512x512.png")

# --- Open Graph / social share image (1200x630) ---
W, H = 1200, 630
grad_mask = Image.linear_gradient("L").rotate(90, expand=True).resize((W, H))
bg_a = Image.new("RGB", (W, H), NAVY)
bg_b = Image.new("RGB", (W, H), (7, 110, 120))
og = Image.composite(bg_b, bg_a, grad_mask).convert("RGBA")

# soft glow accents
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((W - 420, -220, W + 180, 260), fill=SKY + (60,))
gd.ellipse((-220, H - 260, 240, H + 220), fill=TEAL + (60,))
glow = glow.filter(ImageFilter.GaussianBlur(90))
og = Image.alpha_composite(og, glow)

# white card with the logo centered
card_w, card_h = 760, 190
card = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
cd = ImageDraw.Draw(card)
cd.rounded_rectangle((0, 0, card_w, card_h), radius=28, fill=(255, 255, 255, 255))

logo_scale = 2.0
logo_resized = src.resize((int(src.width * logo_scale), int(src.height * logo_scale)), Image.LANCZOS)
card.paste(
    logo_resized,
    ((card_w - logo_resized.width) // 2, (card_h - logo_resized.height) // 2),
    logo_resized,
)

og.alpha_composite(card, ((W - card_w) // 2, (H - card_h) // 2))
og.convert("RGB").save("og-image.jpg", quality=92)

print("done")
