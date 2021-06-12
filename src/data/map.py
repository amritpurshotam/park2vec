import math
from typing import Tuple

import requests
from PIL import Image


def deg2num(lat_deg: float, lon_deg: float, zoom: int) -> Tuple[int, int]:
    """Converts degrees decimal to Slippy Map tile numbers.

    See https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_2 # noqa: B950

    Parameters
    ----------
    lat_deg : float
        Latitude in degrees decimal format
    lon_deg : float
        Longitude in degrees decimal format
    zoom : int
        Zoom level from 1 - 20.
        See https://wiki.openstreetmap.org/wiki/Zoom_levels

    Returns
    -------
    Tuple[int, int]
        The x and y tiles respectively that contains the lat/lon at the
        specified zoom level
    """
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    x_tile = int((lon_deg + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return x_tile, y_tile


def get_map_image(x_tile: int, y_tile: int, zoom: int) -> Image.Image:
    url = f"http://localhost:8080/tile/{zoom}/{x_tile}/{y_tile}.png"
    image = Image.open(requests.get(url, stream=True).raw)
    return image


def get_neighbourhood(x_tile: int, y_tile: int, zoom: int, neighbours: int):
    LENGTH = 256

    full_length = LENGTH * (neighbours * 2 + 1)
    full_image = Image.new("RGB", (full_length, full_length))

    y_offset = 0
    for y in range(y_tile - neighbours, y_tile + neighbours + 1):
        x_offset = 0
        for x in range(x_tile - neighbours, x_tile + neighbours + 1):
            im = get_map_image(x, y, zoom)
            full_image.paste(im, (x_offset, y_offset))
            x_offset += LENGTH
        y_offset += LENGTH

    return full_image


if __name__ == "__main__":
    lat = -26.063356
    lon = 28.088179
    zoom = 16
    x_tile, y_tile = deg2num(lat, lon, zoom)
    im = get_neighbourhood(x_tile, y_tile, zoom, 2)
    im.show()
