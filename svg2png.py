import os
import sys
from pathlib import Path
from cairosvg import svg2png

def convert_svg_file(svg_path: Path):
    """Конвертирует один SVG файл в PNG"""
    try:
        png_file = svg_path.with_suffix('.png')
        svg2png(url=str(svg_path), write_to=str(png_file))
        print(f"✓ Конвертирован: {svg_path.name}")
        return True
    except Exception as e:
        print(f"✗ Ошибка с {svg_path.name}: {e}")
        return False

def convert_svg_in_directory(directory: Path):
    """Конвертирует все SVG файлы в директории и поддиректориях"""
    success_count = 0
    total_count = 0
    
    for svg_file in directory.rglob("*.svg"):
        total_count += 1
        if convert_svg_file(svg_file):
            success_count += 1
    
    return success_count, total_count

def convert_svg_to_png_simple():
    """Простая версия для конвертации в текущей папке или указанном пути"""
    if len(sys.argv) > 1:
        # Есть аргумент командной строки
        input_path = Path(sys.argv[1])
        
        if not input_path.exists():
            print(f"✗ Путь не существует: {input_path}")
            return
        
        if input_path.is_file():
            # Это файл
            if input_path.suffix.lower() == '.svg':
                convert_svg_file(input_path)
            else:
                print(f"✗ Файл не является SVG: {input_path}")
        else:
            # Это папка
            print(f"Обработка папки: {input_path}")
            success_count, total_count = convert_svg_in_directory(input_path)
            print(f"Готово! Успешно: {success_count}/{total_count}")
    else:
        # Нет аргументов - обрабатываем текущую папку
        current_dir = Path.cwd()
        print(f"Обработка текущей папки: {current_dir}")
        success_count, total_count = convert_svg_in_directory(current_dir)
        print(f"Готово! Успешно: {success_count}/{total_count}")

if __name__ == "__main__":
    convert_svg_to_png_simple()