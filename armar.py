# Arma index.html: mete los íconos de img/iconos.svg dentro de fuente.html (así funcionan también abriendo el archivo).
from pathlib import Path
aqui = Path(__file__).parent
iconos = (aqui / 'img' / 'iconos.svg').read_text(encoding='utf-8')
html = (aqui / 'fuente.html').read_text(encoding='utf-8').replace('<!--ICONOS-->', iconos)
(aqui / 'index.html').write_text(html, encoding='utf-8')
print('index.html listo')
