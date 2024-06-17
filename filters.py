from PIL import ImageFilter

def apply_filters(img, filter_type):
    # Converte a imagem para "RGB" para evitar problemas de modo
    img = img.convert("RGB")
    
    if filter_type == 'grayscale':
        return img.convert("L")
    elif filter_type == 'blur':
        return img.filter(ImageFilter.GaussianBlur(radius=2))
    elif filter_type == 'sharpen':
        return img.filter(ImageFilter.SHARPEN)
    elif filter_type == 'edge_enhance':
        return img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == 'find_edges':
        return img.filter(ImageFilter.FIND_EDGES)
    elif filter_type == 'contour':
        return img.filter(ImageFilter.CONTOUR)
    elif filter_type == 'sepia':
        return apply_sepia(img)
    elif filter_type == 'detail':
        return img.filter(ImageFilter.DETAIL)
    elif filter_type == 'emboss':
        return img.filter(ImageFilter.EMBOSS)
    elif filter_type == 'smooth':
        return img.filter(ImageFilter.SMOOTH)
    elif filter_type == 'edge_enhance_more':
        return img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    else:
        return img

def apply_sepia(img):
    width, height = img.size
    pixels = img.load()

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return img
