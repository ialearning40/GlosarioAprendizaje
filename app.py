import streamlit as st

# ---------- LÓGICA (puedes importarla de logic.py si lo separas) ----------
def saludo(nombre="Hermanito"):
    return f"Bienvenido Hermano {nombre}"

def validar_besos(besos: int) -> int:
    if besos < 0:
        return 0
    return min(besos, 10)

def puntaje_besos(besos_validos: int) -> float:
    return ((besos_validos * 5) * 100) / 50  # 0..100

def puntaje_limosna(veces: int, monto_por_vez: int) -> float:
    bruto = (((veces * monto_por_vez) / 10.0) * 100.0) / 300.0
    return min(max(bruto, 0.0), 100.0)

def puntaje_total(p_besos: float, p_limosna: float) -> float:
    return (p_besos + p_limosna) / 2.0

def veredicto(p_total: float) -> str:
    if p_total < 41:
        return "Lo siento, no va al cielo ni cagando"
    elif 41 <= p_total < 80:
        return "Se queda en el purgatorio"
    else:
        return "¡Felicitaciones! Entraste al cielo"

# ---------- UI STREAMLIT ----------
st.set_page_config(page_title="Evaluación celestial", page_icon="✨", layout="centered")
st.title("Evaluación celestial (demo)")

with st.form("feligres_form"):
    st.subheader("Datos del feligrés")
    nombre = st.text_input("Nombre del feligrés", value="")
    st.caption("Si dejas vacío, usaremos 'Hermanito'.")

    st.subheader("Datos de interacción")
    nombremonja = st.text_input("Nombre de la monja (opcional)", value="")
    besos = st.number_input("Número de besos (0–10)", min_value=0, max_value=999999, value=0, step=1)

    st.subheader("Datos de limosna")
    veces = st.number_input("Número de veces que dio limosna", min_value=0, max_value=999999, value=0, step=1)
    monto = st.number_input("Monto por cada limosna (en pesos)", min_value=0, max_value=1_000_000_000, value=0, step=10)

    enviado = st.form_submit_button("Calcular")

if "resultados" not in st.session_state:
    st.session_state.resultados = []

if enviado:
    nom = nombre if nombre.strip() else "Hermanito"
    saludo_txt = saludo(nom)

    besos_validos = validar_besos(int(besos))
    if besos_validos != besos:
        st.warning("Los besos se caps a 10 si ingresas más.")

    p_besos = puntaje_besos(besos_validos)
    p_limosna = puntaje_limosna(int(veces), int(monto))
    p_total = puntaje_total(p_besos, p_limosna)
    msg = veredicto(p_total)

    st.success(f"{saludo_txt}")
    if nombremonja.strip():
        st.write(f"Otorgaste {besos_validos} besos a {nombremonja}.")
    else:
        st.write(f"Besos válidos: {besos_validos}")
    st.write(f"Puntaje por besos: **{p_besos:.0f}%**")
    st.write(f"Puntaje por limosna: **{p_limosna:.0f}%**")
    st.write(f"**Puntaje total:** {p_total:.0f}%")
    st.subheader(msg)

    # Guardar en una tabla de resultados
    st.session_state.resultados.append({
        "Feligrés": nom,
        "Monja": nombremonja,
        "Besos (válidos)": besos_validos,
        "Puntaje Besos %": round(p_besos, 1),
        "Veces Limosna": int(veces),
        "Monto/vez": int(monto),
        "Puntaje Limosna %": round(p_limosna, 1),
        "Total %": round(p_total, 1),
        "Veredicto": msg
    })

if st.session_state.resultados:
    st.divider()
    st.subheader("Histórico de evaluaciones (sesión)")
    st.dataframe(st.session_state.resultados, use_container_width=True)

    # Exportar CSV
    import pandas as pd
    df = pd.DataFrame(st.session_state.resultados)
    st.download_button("Descargar CSV", data=df.to_csv(index=False).encode("utf-8"), file_name="resultados.csv", mime="text/csv")
