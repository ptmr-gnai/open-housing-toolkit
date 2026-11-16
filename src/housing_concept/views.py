"""Raster views of a verified massing for an image tool: a street-side 3D view and a site plan. MIT.

Pure numpy (already present with the geometry dependency). The 3D view is a simple
perspective render of the massing mesh from the street side at a low viewpoint,
shaded by face direction with floor lines, so an image model can read the volume's
footprint, height, floor count and setback. It is not registered to any photo.
"""
import math
import struct
import zlib

import numpy as np

BG = np.array([248, 248, 246], dtype=float)
GROUND = np.array([214, 214, 208], dtype=float)
LOT = np.array([190, 205, 180], dtype=float)
STREET = np.array([120, 120, 120], dtype=float)
RETAIL = np.array([120, 170, 210], dtype=float)
BODY = np.array([205, 120, 80], dtype=float)
EDGE = np.array([30, 30, 30], dtype=float)


def encode_png(img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    h, w, _ = img.shape
    raw = b''.join(b'\x00' + img[y].tobytes() for y in range(h))

    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))


def _line(img, depth, p, q, color, width=2, zbias=None):
    """Draw a projected segment; when depth is given, only where it is not hidden."""
    h, w, _ = img.shape
    n = int(max(abs(q[0] - p[0]), abs(q[1] - p[1]))) + 1
    for t in np.linspace(0, 1, max(n, 2)):
        x = p[0] + (q[0] - p[0]) * t
        y = p[1] + (q[1] - p[1]) * t
        z = None if zbias is None else (p[2] + (q[2] - p[2]) * t)
        for dx in range(-(width // 2), width - width // 2):
            for dy in range(-(width // 2), width - width // 2):
                xi, yi = int(round(x)) + dx, int(round(y)) + dy
                if 0 <= xi < w and 0 <= yi < h:
                    if depth is not None and z is not None and z > depth[yi, xi] + zbias:
                        continue
                    img[yi, xi] = color


def _fill(img, depth, tri, color):
    """Z-buffered triangle fill; tri is three (x, y, z) screen points."""
    h, w, _ = img.shape
    (x0, y0, z0), (x1, y1, z1), (x2, y2, z2) = tri
    xmin, xmax = max(int(math.floor(min(x0, x1, x2))), 0), min(int(math.ceil(max(x0, x1, x2))), w - 1)
    ymin, ymax = max(int(math.floor(min(y0, y1, y2))), 0), min(int(math.ceil(max(y0, y1, y2))), h - 1)
    if xmin > xmax or ymin > ymax:
        return
    area = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if abs(area) < 1e-9:
        return
    xs, ys = np.meshgrid(np.arange(xmin, xmax + 1) + 0.5, np.arange(ymin, ymax + 1) + 0.5)
    w0 = ((x1 - xs) * (y2 - ys) - (x2 - xs) * (y1 - ys)) / area
    w1 = ((x2 - xs) * (y0 - ys) - (x0 - xs) * (y2 - ys)) / area
    w2 = 1 - w0 - w1
    inside = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)
    z = w0 * z0 + w1 * z1 + w2 * z2
    region = depth[ymin:ymax + 1, xmin:xmax + 1]
    draw = inside & (z < region)
    region[draw] = z[draw]
    img[ymin:ymax + 1, xmin:xmax + 1][draw] = color


class Camera:
    def __init__(self, eye, target, fov_deg, width, height):
        self.eye = np.array(eye, dtype=float)
        f = np.array(target, dtype=float) - self.eye
        self.f = f / np.linalg.norm(f)
        r = np.cross(self.f, [0, 0, 1.0])
        self.r = r / np.linalg.norm(r)
        self.u = np.cross(self.r, self.f)
        self.focal = (width / 2) / math.tan(math.radians(fov_deg) / 2)
        self.w, self.h = width, height

    def project(self, p):
        d = np.array(p, dtype=float) - self.eye
        z = float(d @ self.f)
        z = max(z, 1e-3)
        return (self.w / 2 + self.focal * float(d @ self.r) / z, self.h / 2 - self.focal * float(d @ self.u) / z, z)


def street_view(geometry, frame, width=1600, height=1000):
    """Three-quarter view from across the street, slightly raised, so the front, one side, the floor lines and
    the upper-floor setback all read."""
    parcel = geometry['source_geometry']['polygon_ft']
    edge, origin, u, n = frame
    u, n = np.array(u), np.array(n)
    (sx, sy), (ex, ey) = edge['start'], edge['end']
    mid = np.array([(sx + ex) / 2, (sy + ey) / 2])
    length = edge['length_ft']
    height_ft = geometry['total_height_ft']
    eye_xy = mid - n * (length * 1.4) - u * (length * 0.45)
    eye = [eye_xy[0], eye_xy[1], 22.0]
    centre = np.mean(np.array(geometry['floors'][0]['footprint_ft'][:-1], dtype=float), axis=0)
    target = [centre[0], centre[1], height_ft * 0.4]
    cam = Camera(eye, target, 52, width, height)
    img = np.tile(BG, (height, width, 1))
    flat = np.array([cam.f[0], cam.f[1], 0.0])
    horizon = cam.project(cam.eye + flat / np.linalg.norm(flat) * 1e6)[1]
    img[max(0, int(horizon)):] = GROUND
    depth = np.full((height, width), np.inf)
    reach = length * 1.5

    def quad(points, color, z=0.0):
        q = [cam.project([p[0], p[1], z]) for p in points]
        _fill(img, depth, (q[0], q[1], q[2]), color)
        _fill(img, depth, (q[0], q[2], q[3]), color)
    a, b = np.array(edge['start']), np.array(edge['end'])
    quad([a - n * 2 - u * reach, b - n * 2 + u * reach, b - n * 70 + u * reach, a - n * 70 - u * reach], STREET, 0.0)
    lot = [cam.project([x, y, 0.0]) for x, y in parcel]
    for i in range(1, len(lot) - 2):
        _fill(img, depth, (lot[0], lot[i], lot[i + 1]), LOT)
    depth[:] = np.inf
    verts = geometry['mesh']['vertices']
    light = np.array([-0.5, -0.8, 0.5])
    light = light / np.linalg.norm(light)
    for floor in geometry['floors']:
        base = RETAIL if floor['nonresidential_proxy_sf'] > 0.5 else BODY
        for ia, ib, ic in floor['faces']:
            pa, pb, pc = (np.array(verts[i], dtype=float) for i in (ia, ib, ic))
            normal = np.cross(pb - pa, pc - pa)
            if np.linalg.norm(normal) == 0:
                continue
            normal = normal / np.linalg.norm(normal)
            shade = 0.5 + 0.5 * abs(float(normal @ light))
            _fill(img, depth, (cam.project(pa), cam.project(pb), cam.project(pc)), base * shade)
    for floor in geometry['floors']:
        ring = floor['footprint_ft']
        for z in (floor['base_z_ft'], floor['top_z_ft']):
            pts = [cam.project([x, y, z]) for x, y in ring]
            for p, q in zip(pts, pts[1:]):
                _line(img, depth, p, q, EDGE, 2, zbias=1.5)
        for x, y in ring[:-1]:
            _line(img, depth, cam.project([x, y, floor['base_z_ft']]), cam.project([x, y, floor['top_z_ft']]), EDGE, 2, zbias=1.5)
    return encode_png(img), {'eye_ft': [round(float(v), 1) for v in eye], 'target_ft': [round(float(v), 1) for v in target],
                             'fov_deg': 52, 'note': 'Three-quarter view from across the street; not registered to the site photo.'}


def site_plan(geometry, frame, width=1000, height=1000):
    """Top view: lot (green), ground footprint (blue), upper footprint (orange), street edge (thick dark) and street (grey)."""
    parcel = np.array(geometry['source_geometry']['polygon_ft'], dtype=float)
    edge, origin, u, n = frame
    u, n = np.array(u), np.array(n)
    # rotate so the street edge is horizontal at the bottom of the image
    o = np.array(origin)
    to_local = lambda p: np.array([(np.array(p) - o) @ u, (np.array(p) - o) @ n])
    pts = np.array([to_local(p) for p in parcel])
    span = max(np.ptp(pts[:, 0]), np.ptp(pts[:, 1]) + 60)
    scale = (min(width, height) - 120) / span
    x0 = 60 - pts[:, 0].min() * scale
    y0 = height - 60 - 40 * scale

    def screen(p):
        lx, ly = to_local(p)
        return (x0 + lx * scale, y0 - ly * scale, 0.0)
    img = np.tile(BG, (height, width, 1))
    depth = np.full((height, width), np.inf)
    street = [(-1e4, -60), (1e4, -60), (1e4, -2), (-1e4, -2)]
    s = [(x0 + a * scale, y0 - b * scale, 0.0) for a, b in street]
    _fill(img, depth.copy(), (s[0], s[1], s[2]), STREET)
    _fill(img, depth.copy(), (s[0], s[2], s[3]), STREET)

    def poly(ring, color, z):
        p = [screen(q) for q in ring]
        d = np.full((height, width), np.inf)
        for i in range(1, len(p) - 2):
            _fill(img, d, (p[0], p[i], p[i + 1]), color)
        for a, b in zip(p, p[1:]):
            _line(img, None, a, b, EDGE, 2)
    poly(geometry['source_geometry']['polygon_ft'], LOT, 0)
    poly(geometry['floors'][0]['footprint_ft'], RETAIL, 1)
    if len(geometry['floors']) > 1:
        poly(geometry['floors'][1]['footprint_ft'], BODY, 2)
    _line(img, None, screen(edge['start']), screen(edge['end']), EDGE, 7)
    return encode_png(img), {'note': 'Street at the bottom (grey); thick dark line = street edge; green = lot; blue = ground floor; orange = upper floors.'}
