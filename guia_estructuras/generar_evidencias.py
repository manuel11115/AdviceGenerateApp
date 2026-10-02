"""Ejecuta cada programa, captura la salida y genera evidencias.html (-> PDF)."""
import html, subprocess, sys, pathlib, datetime

AQUI = pathlib.Path(__file__).parent
TITULOS = {
 "01_listas": "Sección 2 – Listas (operaciones, recorrido, registro de compras)",
 "02_tuplas": "Sección 3 – Tuplas",
 "03_conjuntos": "Sección 4 – Conjuntos",
 "04_diccionarios": "Sección 5 – Diccionarios",
 "05_estructuras_combinadas": "Sección 6 – Estructuras combinadas",
 "06_ejercicio1_encuestas": "Ejercicio 1 – Análisis de encuestas",
 "07_ejercicio2_agenda": "Ejercicio 2 – Agenda digital",
 "08_ejercicio3_inventario": "Ejercicio 3 – Control de inventario",
 "09_struct_clase": "Struct 1 – Clases",
 "10_struct_namedtuple": "Struct 2 – namedtuple",
 "11_struct_dataclass": "Struct 3 – dataclasses",
 "12_struct_modulo": "Struct 4 – módulo struct (binario)",
 "13_ejemplo_combinado": "Ejemplo práctico combinado (veterinaria)",
 "14_integrador_veterinaria": "Ejercicio integrador final – Veterinaria",
}
e = html.escape
partes = []
for py in sorted(AQUI.glob("[0-9][0-9]_*.py")):
    ent = AQUI / "entradas" / (py.stem + ".txt")
    datos = ent.read_text() if ent.exists() else None
    r = subprocess.run([sys.executable, str(py)], input=datos, capture_output=True, text=True, cwd=AQUI)
    salida = r.stdout + r.stderr
    if datos:  # mostrar tambien lo que se tecleo
        salida = "[Entradas tecleadas: " + ", ".join(datos.split()) + "]\n\n" + salida
    partes.append(f"""<section><h2>{e(TITULOS[py.stem])}</h2>
<p class=f>Archivo: <b>{py.name}</b> · código de salida: {r.returncode}</p>
<h3>Código</h3><pre>{e(py.read_text())}</pre>
<h3>Corrida</h3><pre class=out>{e(salida)}</pre></section>""")
    print("ejecutado", py.name, r.returncode)

doc = f"""<!doctype html><meta charset=utf-8><title>Evidencias</title><style>
body{{font-family:Arial,sans-serif;font-size:11px}} h1{{text-align:center}}
pre{{background:#f4f4f4;border:1px solid #ccc;padding:6px;white-space:pre-wrap;font-size:10px}}
pre.out{{background:#111;color:#8f8}} section{{page-break-before:always}} .f{{color:#555}}
h2{{background:#e5e5e5;padding:4px}}</style>
<h1>Guía de Estudio – Estructuras de Datos y Simulación (STRUCT)</h1>
<p style="text-align:center">Programación Básica · Evidencias de código y corridas<br>
Alumno: ______________________ · Fecha de ejecución: {datetime.date.today()} · Python {sys.version.split()[0]}</p>
<h2>Índice de programas</h2><ol>{''.join(f'<li>{e(t)} – {k}.py</li>' for k,t in TITULOS.items())}</ol>
{''.join(partes)}"""
(AQUI / "evidencias.html").write_text(doc)
