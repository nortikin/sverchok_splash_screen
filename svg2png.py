import os
from pathlib import Path
from cairosvg import svg2png

def convert_svg_to_png_simple():
    """Простая версия для конвертации в текущей папке"""
    current_dir = Path.cwd()
    
    for svg_file in current_dir.rglob("*.svg"):
        try:
            png_file = svg_file.with_suffix('.png')
            svg2png(url=str(svg_file), write_to=str(png_file))
            print(f"✓ Конвертирован: {svg_file.name}")
        except Exception as e:
            print(f"✗ Ошибка с {svg_file.name}: {e}")

if __name__ == "__main__":
    convert_svg_to_png_simple()
    print("Готово!")