import sys, os, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent.resolve()
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
times = [float(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None
with sync_playwright() as p:
    b = p.chromium.launch(channel='msedge')
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto((HERE / 'index.html').as_uri())
    pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(800)
    if times:
        for t in times:
            pg.evaluate(f'render({t})'); pg.wait_for_timeout(60)
            pg.screenshot(path=str(OUT / f'p{t:05.2f}.png'))
    else:
        for i in range(450):
            pg.evaluate(f'render({i/30})')
            pg.screenshot(path=str(OUT / f'f{i:04d}.png'))
    b.close()
