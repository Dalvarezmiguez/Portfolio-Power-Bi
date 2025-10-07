import requests, json, os, base64, io
import matplotlib.pyplot as plt
from datetime import datetime

# --- Configuración ---
token = os.environ["GITHUB_TOKEN"]
repo = os.environ["REPO"]
headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

# --- Recoger datos de GitHub ---
views = requests.get(f"https://api.github.com/repos/{repo}/traffic/views", headers=headers).json()
clones = requests.get(f"https://api.github.com/repos/{repo}/traffic/clones", headers=headers).json()
referrers = requests.get(f"https://api.github.com/repos/{repo}/traffic/popular/referrers", headers=headers).json()
content = requests.get(f"https://api.github.com/repos/{repo}/traffic/popular/paths", headers=headers).json()

# --- Historial previo ---
history_file = "traffic-history.json"
if os.path.exists(history_file):
    with open(history_file) as f:
        history = json.load(f)
else:
    history = {"views":0,"uniques_views":0,"clones":0,"uniques_clones":0}

def trend_icon(curr, prev):
    if curr > prev: return "⬆️"
    elif curr < prev: return "⬇️"
    else: return "➡️"

# --- Crear gráficos en Base64 ---
def make_chart(data_list, color, title):
    dates = [datetime.strptime(v["timestamp"][:10], "%Y-%m-%d") for v in data_list]
    counts = [v["count"] for v in data_list]

    plt.figure(figsize=(8,4))
    plt.bar(dates, counts, color=color)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    return base64.b64encode(buf.getvalue()).decode("utf-8")

chart_views = make_chart(views.get("views", []), "#4CAF50", "Visitas diarias")
chart_clones = make_chart(clones.get("clones", []), "#2196F3", "Clones diarios")

# --- Generar HTML elegante ---
html = f"""
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      font-family: 'Segoe UI', Arial, sans-serif;
      margin: 0; padding: 20px;
      background-color: #f9f9f9;
      color: #333;
    }}
    h1 {{
      text-align: center;
      background: #4CAF50;
      color: white;
      padding: 20px;
      border-radius: 10px;
    }}
    .cards {{
      display: flex;
      justify-content: space-around;
      margin: 20px 0;
    }}
    .card {{
      background: white;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      width: 45%;
      text-align: center;
    }}
    .card h2 {{
      margin-bottom: 10px;
      color: #555;
    }}
    .metric {{
      font-size: 24px;
      font-weight: bold;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }}
    th {{
      background: #4CAF50;
      color: white;
    }}
    tr:nth-child(even) {{ background-color: #f2f2f2; }}
    img {{
      display: block;
      margin: 20px auto;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }}
  </style>
</head>
<body>
  <h1>📊 Informe semanal de tráfico — {repo}</h1>

  <div class="cards">
    <div class="card">
      <h2>Visitas</h2>
      <div class="metric">{views.get("count",0)} {trend_icon(views.get("count",0), history.get("views",0))}</div>
      <p>Visitantes únicos: {views.get("uniques",0)} {trend_icon(views.get("uniques",0), history.get("uniques_views",0))}</p>
    </div>
    <div class="card">
      <h2>Clones</h2>
      <div class="metric">{clones.get("count",0)} {trend_icon(clones.get("count",0), history.get("clones",0))}</div>
      <p>Usuarios únicos: {clones.get("uniques",0)} {trend_icon(clones.get("uniques",0), history.get("uniques_clones",0))}</p>
    </div>
  </div>

  <img src="data:image/png;base64,{chart_views}" alt="Gráfico de visitas" />
  <img src="data:image/png;base64,{chart_clones}" alt="Gráfico de clones" />

  <h2>🌍 Referrers principales</h2>
  <table>
    <tr><th>Referrer</th><th>Visitas</th></tr>
    {''.join(f"<tr><td>{r['referrer']}</td><td>{r['count']}</td></tr>" for r in referrers)}
  </table>

  <h2>📁 Archivos más visitados</h2>
  <table>
    <tr><th>Archivo</th><th>Visitas</th></tr>
    {''.join(f"<tr><td>{c['path']}</td><td>{c['count']}</td></tr>" for c in content)}
  </table>

  <p style="text-align:center; margin-top:40px; color:#888;">
    Informe generado automáticamente por GitHub Actions
  </p>
</body>
</html>
"""

with open("traffic-report.html", "w", encoding="utf-8") as f:
    f.write(html)

# --- Actualizar historial ---
new_history = {
    "views": views.get("count",0),
    "uniques_views": views.get("uniques",0),
    "clones": clones.get("count",0),
    "uniques_clones": clones.get("uniques",0)
}
with open(history_file,"w") as f:
    json.dump(new_history,f)
