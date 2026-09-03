import pandas as pd
#
def calcular_kpis_fraude(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "Volumen_total": 0.0,
            "Ticket_promedio": 0.0,
            "Cantidad_de_transacciones": 0
        }

    volumen_total_procesado = df["monto_eur"].sum()
    cantidad_de_transacciones_evaluadas = len(df)

    ticket_promedio = (
        volumen_total_procesado / cantidad_de_transacciones_evaluadas
        if cantidad_de_transacciones_evaluadas > 0
        else 0.0
    )

    return {
        "Volumen_total": volumen_total_procesado,
        "Ticket_promedio": ticket_promedio,
        "Cantidad_de_transacciones": cantidad_de_transacciones_evaluadas
    }