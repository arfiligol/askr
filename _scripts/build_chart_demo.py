"""Rebuild the public mathematical chart fixture; no solver or runtime CDN."""

import base64
import hashlib
import io
import json
import math
import tarfile
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.1.0"
URL = (
    "https://registry.npmjs.org/plotly.js-basic-dist-min/-/"
    f"plotly.js-basic-dist-min-{VERSION}.tgz"
)
TARBALL_SHA512 = (
    "LEB0VGnW2XMXvW89qi8jXe+GBZTp6VwBYn+kMDM77LSbSXtPikPnh7nZY5ZBnLd"
    "LMzP0Q88skEY7C0LiVdB9ZA=="
)
SCRIPT_SHA256 = "80d756297ee4b5e701cee4e5c88aa52ec822c3ed84fd23bda6e20b03d10492a6"


def main() -> None:
    with urllib.request.urlopen(URL) as response:
        archive = response.read()
    actual = base64.b64encode(hashlib.sha512(archive).digest()).decode("ascii")
    if actual != TARBALL_SHA512:
        raise ValueError("Plotly fixture archive differs from its pinned integrity")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as tar:
        script = tar.extractfile("package/plotly-basic.min.js").read()
        license_text = tar.extractfile("package/LICENSE").read()
    if hashlib.sha256(script).hexdigest() != SCRIPT_SHA256:
        raise ValueError("Plotly fixture script differs from its pinned SHA-256")

    x = [round(i * math.pi / 40, 12) for i in range(161)]
    trace = {
        "type": "scatter",
        "mode": "lines",
        "name": "sin(x)",
        "x": x,
        "y": [round(math.sin(value), 12) for value in x],
        "line": {"color": "#284b63", "width": 3},
        "hovertemplate": "x = %{x:.3f}<br>sin(x) = %{y:.3f}<extra></extra>",
    }
    layout = {
        "title": {"text": "Illustrative mathematical curve: y = sin(x)", "font": {"size": 18}},
        "xaxis": {"title": {"text": "x (radians)"}, "gridcolor": "#e5e5e5", "zerolinecolor": "#b8b8b8"},
        "yaxis": {"title": {"text": "sin(x)"}, "range": [-1.2, 1.2], "gridcolor": "#e5e5e5", "zerolinecolor": "#b8b8b8"},
        "font": {"family": "system-ui, sans-serif", "color": "#2b2b2b"},
        "paper_bgcolor": "#faf8f8",
        "plot_bgcolor": "#faf8f8",
        "margin": {"l": 65, "r": 25, "t": 80, "b": 60},
        "dragmode": "zoom",
        "showlegend": False,
    }
    config = {"responsive": True, "displaylogo": False, "displayModeBar": True, "scrollZoom": True}
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Illustrative sine curve — Askr chart viewer demo</title>
<style>
html, body { width: 100%; height: 100%; margin: 0; background: #faf8f8; }
#chart { width: 100%; height: 100%; min-height: 240px; }
</style>
</head>
<body>
<div id="chart" role="img" aria-label="Interactive illustrative sine curve. Use Plotly controls to inspect values, zoom, pan and reset."></div>
<!-- Plotly.js basic 3.1.0; MIT license in plotly-example.LICENSE.txt. -->
<script>""" + script.decode("utf-8").replace("</script", "<\\/script") + "</script>\n<script>\n"
    html += "Plotly.newPlot('chart', " + json.dumps([trace], separators=(",", ":")) + ", "
    html += json.dumps(layout, separators=(",", ":")) + ", " + json.dumps(config, separators=(",", ":")) + ");\n"
    html += "</script>\n</body>\n</html>\n"
    directory = ROOT / "components" / "images"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "plotly-example.html").write_text(html, encoding="utf-8")
    (directory / "plotly-example.LICENSE.txt").write_bytes(license_text)
    print(f"Wrote self-contained Plotly {VERSION} sine fixture and upstream MIT license")


if __name__ == "__main__":
    main()
