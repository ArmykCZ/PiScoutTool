#import time
#from smbus2 import SMBus
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
#import epd2in13_V4

# OBRAZOVKA
# x = 250 sloupců, čím větší x, tim více jdeme doprava
# y = 122 řádků, čím větší y, tim více jdeme dolů
# střed cca (125, 61)

# KRESLENÍ
# bit 1 = bílé pozadí/barva
# bit 0 = černé pozadí/barva
# image = Image.new('1', (250, 122), 255)
# funkce Image = data v paměti
# ImageDraw = malování tvarů, textu...
# Font = písmo, které se použije pro text
#      canvas = Image.new('1', (250, 122), 255) # plátno
#      draw = ImageDraw.Draw(canvas)            # štětec napojený na plátno

# TVARY
# bod = draw.point((x, y), fill=0) | x, y = souřadnice bodu
# čára = draw.line((x1, y1, x2, y2), fill=0) | x1, y1 = počáteční souřadnice, x2, y2 = koncové souřadnice
# kruh = draw.ellipse((x1, y1, x2, y2), fill=0) | x1, y1 = levý horní roh, x2, y2 = pravý dolní roh
# obdelník = draw.rectangle((x1, y1, x2, y2), fill=0) | x1, y1 = levý horní roh, x2, y2 = pravý dolní roh

# TEXT
# Imagefont.load_default() = defaultní písmo
# draw.text((x, y), "text", fill=0, font=font)

# Obrázek
# canvas.paste(icon_image, (x, y))

SLOZKA = Path(__file__).parent / "pictures"

def test_main():
    font = ImageFont.load_default()
    velky_text = ImageFont.load_default(20)
    canvas = Image.new("1", (250, 122), 255)
    draw = ImageDraw.Draw(canvas)
    tools = [ {
            "name": "Wifi Scan",
            "icon": "wifi.png",
            "description": "Wifi Scan",
        },
        {
            "name": "BLE Recon",
            "icon": "ble.png",
            "description": "BLE Recon",
        },
        {
            "name": "Shutdown",
            "icon": "zigbee.png",
            "description": "Shutdown",
        },
        ]
    i = 1
    i = (i + 1) % len(tools)
    
    draw.line((0, 20, 249, 20), fill=0, width=1)
    draw.text((10, 4), "PiScoutTool V0.0.1", fill=0, font=font)
    draw.text((175, 4), "Zde baterie", fill=0, font=font)
    canvas.paste(Image.open(SLOZKA / tools[i]["icon"]), (10, 45))
    draw.text((70, 45), tools[i]["name"], fill=0, font=velky_text)
    draw.text((70, 70), tools[i]["description"], fill=0, font=font)


    canvas.save("test.png")

if __name__ == "__main__":
    test_main()