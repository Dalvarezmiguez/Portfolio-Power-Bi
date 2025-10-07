import requests, json, os
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

# --- Crear tablas HTML ---
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

# --- Crear gráficos ---
def make_daily_plot(data_list, filename, color="#4CAF50", title=""):
    dates = [v['timestamp'][:10] for v in data_list]
    counts = [v['count'] for v in data_list]
    plt.figure(figsize=(10,4))
    plt.bar(dates, counts, color=color)
    plt.xticks(rotation=45)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Generar gráficos
make_daily_plot(views.get('views',[]), "visitas.png", color="#4CAF50", title="Visitas diarias")
make_daily_plot(clones.get('clones',[]), "clones.png", color="#2196F3", title="Clones diarios")

# --- Crear HTML completo ---
html_body = f"""
<h1>Informe semanal de tráfico: {repo}</h1>

<h2>Visitas</h2>
{make_table(
    [[compare(views.get('count',0), history.get('views',0)),
      compare(views.get('uniques',0), history.get('uniques_views',0))]],
    ['Total visitas','Visitantes únicos']
)}
<p>Gráfico de visitas adjunto: <strong>visitas.png</strong></p>

<h2>Clones</h2>
{make_table(
    [[compare(clones.get('count',0), history.get('clones',0)),
      compare(clones.get('uniques',0), history.get('uniques_clones',0))]],
    ['Total clones','Clonadores únicos']
)}
<p>Gráfico de clones adjunto: <strong>clones.png</strong></p>

<h2>Referrers principales</h2>
{make_table([[r['referrer'], r['count']] for r in referrers], ['Referrer','Visitas'])}

<h2>Archivos más visitados</h2>
{make_table([[c['path'], c['count']] for c in content], ['Archivo','Visitas'])}
"""

# --- Guardar HTML ---
with open("traffic-report.html","w") as f:
    f.write(html_body)

# --- Actualizar historial ---
history = {
    "views": views.get("count",0),
    "uniques_views": views.get("uniques",0),
    "clones": clones.get("count",0),
    "uniques_clones": clones.get("uniques_clones",0)
}
with open(history_file,"w") as f:
    json.dump(history,f)

