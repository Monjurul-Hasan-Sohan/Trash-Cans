from machine import Pin, SPI
import st7796
import time

# --- Setup Pins for ESP32-3248S035C ---
SCK_PIN = 14
MOSI_PIN = 13
MISO_PIN = 12
CS_PIN = 15
DC_PIN = 2
RST_PIN = 12
BL_PIN = 27

# Colors
COLOR_GREEN = 0x07E0
COLOR_WHITE = 0xFFFF
COLOR_BLACK = 0x0000

def main():
    print("Initializing SPI...")
    spi = SPI(1, baudrate=60000000, polarity=0, phase=0, sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))

    print("Initializing Display...")
    tft = st7796.ST7796(
        spi=spi,
        cs=Pin(CS_PIN),
        dc=Pin(DC_PIN),
        rst=Pin(RST_PIN),
        bl=Pin(BL_PIN),
        rotation=1 
    )

    # 1. Background Green
    print("Filling Green...")
    tft.fill(COLOR_GREEN)

    # 2. Draw Text "GREENSYNC" (No space)
    # Logic for perfect centering:
    # Font Width per char = 6 (5 pixels + 1 spacing)
    # Total Chars = 9 ("GREENSYNC")
    
    # We use Size 7.
    # Total Width = 9 chars * 6 width * 7 size = 378 pixels.
    # Screen Width = 480 pixels.
    # Margin X = (480 - 378) / 2 = 51 pixels.
    
    # Height = 8 pixels * 7 size = 56 pixels.
    # Margin Y = (320 - 56) / 2 = 132 pixels.
    
    size = 7
    start_x = 51
    start_y = 132
    
    print("Drawing Text...")
    
    # Draw "GREEN"
    curr_x = tft.text("GREEN", start_x, start_y, COLOR_WHITE, COLOR_GREEN, size)
    
    # Draw "SYNC" immediately after (no space added)
    tft.text("SYNC", curr_x, start_y, COLOR_BLACK, COLOR_GREEN, size)

    print("Done!")

if __name__ == "__main__":
    main()