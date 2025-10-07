import requests, json, os, base64
from io import BytesIO
import matplotlib.pyplot as plt

# --- Configuración ---
token = os.environ["GITHUB_TOKEN"]
repo = os.environ["REPO"]
headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

# --- Recoger datos ---
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

# --- Comparativa ---
def compare(current, previous):
    if current > previous: return f"{current} ⬆️"
    elif current < previous: return f"{current} ⬇️"
    else: return f"{current} ➡️"

# --- Tablas HTML ---
def make_table(data, headers):
    html = '<table style="border-collapse: collapse; width: 100%;">'
    html += '<tr style="background-color: #4CAF50; color: white;">'
    for h in headers:
        html += f'<th style="border: 1px solid #ddd; padding: 8px;">{h}</th>'
    html += '</tr>'
    for i, row in enumerate(data):
        bg = '#f2f2f2' if i % 2 == 0 else 'white'
        html += f'<tr style="background-color:{bg}">'
        for val in row:
            html += f'<td style="border: 1px solid #ddd; padding: 8px;">{val}</td>'
        html += '</tr>'
    html += '</table>'
    return html

# --- Generar gráfico diario como imagen base64 ---
def make_daily_bars_plot(daily_data, title, color="#4CAF50"):
    dates = [v['timestamp'][:10] for v in daily_data]
    counts = [v['count'] for v in daily_data]
    if not dates:
        dates = ["—"]
        counts = [0]

    fig, ax = plt.subplots(figsize=(8,2))
    ax.bar(dates, counts, color=color)
    ax.set_title(title, fontsize=10)
    ax.set_ylabel("Cantidad", fontsize=8)
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(dates, rotation=45, fontsize=8)
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    return f'<img src="data:image/png;base64,{img_base64}"/>'

# --- Crear HTML completo ---
html_body = f"""
<h1>📊 Informe semanal de tráfico: {repo}</h1>

<h2>Visitas</h2>
{make_table(
    [[compare(views.get('count',0), history.get('views',0)),
      compare(views.get('uniques',0), history.get('uniques_views',0))]],
    ['Total visitas','Visitantes únicos']
)}
{make_daily_bars_plot(views.get('views',[]), "Gráfico diario de visitas", "#4CAF50")}

<h2>Clones</h2>
{make_table(
    [[compare(clones.get('count',0), history.get('clones',0)),
      compare(clones.get('uniques',0), history.get('uniques_clones',0))]],
    ['Total clones','Clonadores únicos']
)}
{make_daily_bars_plot(clones.get('clones',[]), "Gráfico diario de clones", "#2196F3")}

<h2>🌍 Referrers principales</h2>
{make_table([[r['referrer'], r['count']] for r in referrers], ['Referrer','Visitas'])}

<h2>📁 Archivos más visitados</h2>
{make_table([[c['path'], c['count']] for c in content], ['Archivo','Visitas'])}

<p style="font-size:10px;color:gray;">Informe generado automáticamente por GitHub Actions</p>
"""

# --- Guardar HTML ---
with open("traffic-report.html","w") as f:
    f.write(html_body)

# --- Actualizar historial ---
history = {
    "views": views.get("count",0),
    "uniques_views": views.get("uniques",0),
    "clones": clones.get("count",0),
    "uniques_clones": clones.get("uniques",0)
}
with open(history_file,"w") as f:
    json.dump(history,f)
