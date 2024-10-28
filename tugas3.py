import imageio
import numpy as np
import matplotlib.pyplot as plt
def grayscale_histogram(image_path):
# Membaca gambar
  img = imageio.imread(image_path)

# Konversi ke grayscale (menggunakan rata-rata R, G, B)
  gray_img = np.mean(img, axis=2).astype(np.uint8)

# Hitung histogram
  hist, bins = np.histogram(gray_img.flatten(), bins=256, range=(0, 255))

# Plot histogram
  plt.bar(bins[:-1], hist, width=1)
  plt.xlabel("Intensitas")
  plt.ylabel("Jumlah Piksel")
  plt.title("Histogram Gambar Grayscale")
  plt.show()

# Menampilkan jumlah total piksel untuk setiap intensitas
  for i, count in enumerate(hist):
    print(f"Intensitas {i}: {count} piksel")

# Mencari intensitas dominan (nilai maksimum dalam histogram)
  dominant_intensity = np.argmax(hist)
  print(f"Intensitas dominan: {dominant_intensity}")

# Path gambar Kita
image_path = 'gryscale.jpg'
grayscale_histogram(image_path)

# Output
"""
Intensitas 0: 937527 piksel
Intensitas 1: 4048 piksel
Intensitas 2: 2561 piksel
Intensitas 3: 1528 piksel
Intensitas 4: 881 piksel
Intensitas 5: 548 piksel
Intensitas 6: 306 piksel
Intensitas 7: 194 piksel
Intensitas 8: 126 piksel
Intensitas 9: 109 piksel
Intensitas 10: 114 piksel
Intensitas 11: 79 piksel
Intensitas 12: 75 piksel
Intensitas 13: 65 piksel
Intensitas 14: 69 piksel
Intensitas 15: 66 piksel
Intensitas 16: 54 piksel
Intensitas 17: 61 piksel
Intensitas 18: 63 piksel
Intensitas 19: 48 piksel
Intensitas 20: 47 piksel
Intensitas 21: 55 piksel
Intensitas 22: 58 piksel
Intensitas 23: 48 piksel
Intensitas 24: 66 piksel
Intensitas 25: 71 piksel
Intensitas 26: 59 piksel
Intensitas 27: 49 piksel
Intensitas 28: 48 piksel
Intensitas 29: 63 piksel
Intensitas 30: 62 piksel
Intensitas 31: 54 piksel
Intensitas 32: 43 piksel
Intensitas 33: 41 piksel
Intensitas 34: 54 piksel
Intensitas 35: 59 piksel
Intensitas 36: 49 piksel
Intensitas 37: 48 piksel
Intensitas 38: 51 piksel
Intensitas 39: 33 piksel
Intensitas 40: 47 piksel
Intensitas 41: 50 piksel
Intensitas 42: 46 piksel
Intensitas 43: 54 piksel
Intensitas 44: 47 piksel
Intensitas 45: 48 piksel
Intensitas 46: 52 piksel
Intensitas 47: 49 piksel
Intensitas 48: 58 piksel
Intensitas 49: 51 piksel
Intensitas 50: 35 piksel
Intensitas 51: 41 piksel
Intensitas 52: 40 piksel
Intensitas 53: 41 piksel
Intensitas 54: 50 piksel
Intensitas 55: 59 piksel
Intensitas 56: 55 piksel
Intensitas 57: 42 piksel
Intensitas 58: 51 piksel
Intensitas 59: 51 piksel
Intensitas 60: 52 piksel
Intensitas 61: 53 piksel
Intensitas 62: 39 piksel
Intensitas 63: 46 piksel
Intensitas 64: 45 piksel
Intensitas 65: 43 piksel
Intensitas 66: 54 piksel
Intensitas 67: 44 piksel
Intensitas 68: 42 piksel
Intensitas 69: 53 piksel
Intensitas 70: 46 piksel
Intensitas 71: 47 piksel
Intensitas 72: 54 piksel
Intensitas 73: 61 piksel
Intensitas 74: 106 piksel
Intensitas 75: 176 piksel
Intensitas 76: 451 piksel
Intensitas 77: 197 piksel
Intensitas 78: 102 piksel
Intensitas 79: 66 piksel
Intensitas 80: 69 piksel
Intensitas 81: 66 piksel
Intensitas 82: 47 piksel
Intensitas 83: 64 piksel
Intensitas 84: 64 piksel
Intensitas 85: 62 piksel
Intensitas 86: 54 piksel
Intensitas 87: 75 piksel
Intensitas 88: 72 piksel
Intensitas 89: 73 piksel
Intensitas 90: 95 piksel
Intensitas 91: 295 piksel
Intensitas 92: 525 piksel
Intensitas 93: 1149 piksel
Intensitas 94: 10389 piksel
Intensitas 95: 1095 piksel
Intensitas 96: 496 piksel
Intensitas 97: 190 piksel
Intensitas 98: 124 piksel
Intensitas 99: 101 piksel
Intensitas 100: 88 piksel
Intensitas 101: 104 piksel
Intensitas 102: 171 piksel
Intensitas 103: 152 piksel
Intensitas 104: 132 piksel
Intensitas 105: 117 piksel
Intensitas 106: 110 piksel
Intensitas 107: 116 piksel
Intensitas 108: 128 piksel
Intensitas 109: 184 piksel
Intensitas 110: 148 piksel
Intensitas 111: 225 piksel
Intensitas 112: 424 piksel
Intensitas 113: 706 piksel
Intensitas 114: 2370 piksel
Intensitas 115: 3612 piksel
Intensitas 116: 6984 piksel
Intensitas 117: 13252 piksel
Intensitas 118: 24458 piksel
Intensitas 119: 39480 piksel
Intensitas 120: 280399 piksel
Intensitas 121: 37811 piksel
Intensitas 122: 22421 piksel
Intensitas 123: 14072 piksel
Intensitas 124: 7292 piksel
Intensitas 125: 3940 piksel
Intensitas 126: 2143 piksel
Intensitas 127: 1643 piksel
Intensitas 128: 1106 piksel
Intensitas 129: 858 piksel
Intensitas 130: 968 piksel
Intensitas 131: 1545 piksel
Intensitas 132: 4029 piksel
Intensitas 133: 18082 piksel
Intensitas 134: 4074 piksel
Intensitas 135: 1466 piksel
Intensitas 136: 923 piksel
Intensitas 137: 1091 piksel
Intensitas 138: 1313 piksel
Intensitas 139: 1446 piksel
Intensitas 140: 1293 piksel
Intensitas 141: 1016 piksel
Intensitas 142: 1025 piksel
Intensitas 143: 1611 piksel
Intensitas 144: 951 piksel
Intensitas 145: 1257 piksel
Intensitas 146: 1604 piksel
Intensitas 147: 1662 piksel
Intensitas 148: 2683 piksel
Intensitas 149: 6981 piksel
Intensitas 150: 179125 piksel
Intensitas 151: 7369 piksel
Intensitas 152: 3052 piksel
Intensitas 153: 1180 piksel
Intensitas 154: 749 piksel
Intensitas 155: 440 piksel
Intensitas 156: 391 piksel
Intensitas 157: 371 piksel
Intensitas 158: 353 piksel
Intensitas 159: 322 piksel
Intensitas 160: 300 piksel
Intensitas 161: 347 piksel
Intensitas 162: 349 piksel
Intensitas 163: 339 piksel
Intensitas 164: 342 piksel
Intensitas 165: 377 piksel
Intensitas 166: 343 piksel
Intensitas 167: 354 piksel
Intensitas 168: 373 piksel
Intensitas 169: 371 piksel
Intensitas 170: 394 piksel
Intensitas 171: 378 piksel
Intensitas 172: 363 piksel
Intensitas 173: 446 piksel
Intensitas 174: 418 piksel
Intensitas 175: 396 piksel
Intensitas 176: 367 piksel
Intensitas 177: 413 piksel
Intensitas 178: 414 piksel
Intensitas 179: 603 piksel
Intensitas 180: 1293 piksel
Intensitas 181: 16389 piksel
Intensitas 182: 1511 piksel
Intensitas 183: 1045 piksel
Intensitas 184: 9093 piksel
Intensitas 185: 827 piksel
Intensitas 186: 596 piksel
Intensitas 187: 570 piksel
Intensitas 188: 650 piksel
Intensitas 189: 589 piksel
Intensitas 190: 544 piksel
Intensitas 191: 613 piksel
Intensitas 192: 805 piksel
Intensitas 193: 839 piksel
Intensitas 194: 1158 piksel
Intensitas 195: 1479 piksel
Intensitas 196: 2826 piksel
Intensitas 197: 3630 piksel
Intensitas 198: 130843 piksel
Intensitas 199: 6027 piksel
Intensitas 200: 7666 piksel
Intensitas 201: 40464 piksel
Intensitas 202: 17904 piksel
Intensitas 203: 27052 piksel
Intensitas 204: 2126625 piksel
Intensitas 205: 27421 piksel
Intensitas 206: 18159 piksel
Intensitas 207: 8995 piksel
Intensitas 208: 5190 piksel
Intensitas 209: 3499 piksel
Intensitas 210: 1996 piksel
Intensitas 211: 1129 piksel
Intensitas 212: 948 piksel
Intensitas 213: 1277 piksel
Intensitas 214: 33848 piksel
Intensitas 215: 1272 piksel
Intensitas 216: 693 piksel
Intensitas 217: 397 piksel
Intensitas 218: 165 piksel
Intensitas 219: 79 piksel
Intensitas 220: 36 piksel
Intensitas 221: 19 piksel
Intensitas 222: 9 piksel
Intensitas 223: 0 piksel
Intensitas 224: 0 piksel
Intensitas 225: 0 piksel
Intensitas 226: 0 piksel
Intensitas 227: 0 piksel
Intensitas 228: 0 piksel
Intensitas 229: 0 piksel
Intensitas 230: 0 piksel
Intensitas 231: 0 piksel
Intensitas 232: 0 piksel
Intensitas 233: 0 piksel
Intensitas 234: 0 piksel
Intensitas 235: 0 piksel
Intensitas 236: 0 piksel
Intensitas 237: 0 piksel
Intensitas 238: 0 piksel
Intensitas 239: 0 piksel
Intensitas 240: 0 piksel
Intensitas 241: 0 piksel
Intensitas 242: 0 piksel
Intensitas 243: 0 piksel
Intensitas 244: 0 piksel
Intensitas 245: 0 piksel
Intensitas 246: 0 piksel
Intensitas 247: 0 piksel
Intensitas 248: 0 piksel
Intensitas 249: 0 piksel
Intensitas 250: 0 piksel
Intensitas 251: 0 piksel
Intensitas 252: 0 piksel
Intensitas 253: 0 piksel
Intensitas 254: 0 piksel
Intensitas 255: 0 piksel
Intensitas dominan: 204 """