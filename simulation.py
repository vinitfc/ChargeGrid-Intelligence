"""
SolarTrack — Simulação de Sistema Fotovoltaico Residencial
Sprint 2 — Prova de Conceito Funcional
Disciplina: Soluções em Energias Renováveis e Sustentáveis — FIAP 2026

Modelo físico simplificado baseado em irradiância solar horária.
Gera dados realistas de geração fotovoltaica para um dia típico.
"""

import math
import json
from datetime import datetime, timedelta

# ──────────────────────────────────────────────
# PARÂMETROS DO SISTEMA FOTOVOLTAICO
# ──────────────────────────────────────────────
NUM_PAINEIS = 4
AREA_PAINEL_M2 = 1.5               # m² por painel (padrão residencial)
EFICIENCIA_PAINEL = 0.20           # 20% — monocristalino moderno
FATOR_TEMPERATURA = 0.95           # perda por aquecimento (~5%)
IRRADIANCIA_PICO_W_M2 = 1000       # W/m² em STC (Standard Test Conditions)

# Localização: São Paulo, SP
LATITUDE_RAD = math.radians(-23.55)

# Tarifa de energia elétrica (R$/kWh) — ANEEL 2024
TARIFA_R_KWH = 0.90

# Fator de emissão de CO₂ da rede elétrica brasileira — IPCC 2021
FATOR_CO2_KG_KWH = 0.0816

# Carbono sequestrado por árvore por ano (kg CO₂/árvore/ano)
CO2_POR_ARVORE_KG_ANO = 21.77


def calcular_declinacao_solar(dia_do_ano: int) -> float:
    """
    Calcula a declinação solar em radianos para um dado dia do ano.
    Equação de Cooper (1969).
    """
    return math.radians(23.45 * math.sin(math.radians(360 / 365 * (dia_do_ano - 81))))


def calcular_angulo_horario(hora_decimal: float) -> float:
    """
    Converte hora do dia (0–24) em ângulo horário em radianos.
    Meio-dia solar = ângulo 0.
    """
    return math.radians(15 * (hora_decimal - 12))


def calcular_cos_zenital(hora_decimal: float, declinacao: float, latitude: float) -> float:
    """
    Calcula o cosseno do ângulo zenital solar.
    Quando cos_z <= 0, o sol está abaixo do horizonte.
    """
    angulo_horario = calcular_angulo_horario(hora_decimal)
    cos_z = (
        math.sin(latitude) * math.sin(declinacao)
        + math.cos(latitude) * math.cos(declinacao) * math.cos(angulo_horario)
    )
    return max(0.0, cos_z)


def calcular_irradiancia(hora_decimal: float, declinacao: float) -> float:
    """
    Estima irradiância solar incidente (W/m²) para uma hora do dia.
    Aplica fator atmosférico simplificado (0,75) para perdas de absorção.
    """
    cos_z = calcular_cos_zenital(hora_decimal, declinacao, LATITUDE_RAD)
    fator_atmosferico = 0.75
    return IRRADIANCIA_PICO_W_M2 * cos_z * fator_atmosferico


def calcular_potencia_w(irradiancia: float) -> float:
    """
    Calcula potência gerada pelo sistema fotovoltaico (W).
    P = Irradiância × Área_total × Eficiência × Fator_temperatura
    """
    area_total = NUM_PAINEIS * AREA_PAINEL_M2
    return irradiancia * area_total * EFICIENCIA_PAINEL * FATOR_TEMPERATURA


def simular_dia(dia_do_ano: int = 172, intervalo_minutos: int = 30) -> list:
    """
    Simula a geração fotovoltaica ao longo de um dia inteiro.

    Args:
        dia_do_ano: Número do dia (1–365). Padrão = 172 (21/jun, solstício)
        intervalo_minutos: Resolução temporal em minutos

    Returns:
        Lista de dicionários com dados por intervalo de tempo
    """
    declinacao = calcular_declinacao_solar(dia_do_ano)
    registros = []
    energia_acumulada_wh = 0.0

    hora = 0.0
    while hora <= 24.0:
        irradiancia = calcular_irradiancia(hora, declinacao)
        potencia_w = calcular_potencia_w(irradiancia)

        # Integração trapezoidal simples: energia no intervalo (Wh)
        energia_intervalo_wh = potencia_w * (intervalo_minutos / 60)
        energia_acumulada_wh += energia_intervalo_wh

        # Conversão para kWh
        energia_acumulada_kwh = energia_acumulada_wh / 1000

        # Métricas de sustentabilidade
        co2_evitado_kg = energia_acumulada_kwh * FATOR_CO2_KG_KWH
        economia_reais = energia_acumulada_kwh * TARIFA_R_KWH
        arvores_equiv = co2_evitado_kg / CO2_POR_ARVORE_KG_ANO * 365  # proporcional ao dia

        # Formata hora para HH:MM
        horas_int = int(hora)
        minutos_int = int((hora - horas_int) * 60)
        hora_str = f"{horas_int:02d}:{minutos_int:02d}"

        registros.append({
            "hora": hora_str,
            "hora_decimal": round(hora, 2),
            "irradiancia_w_m2": round(irradiancia, 1),
            "potencia_w": round(potencia_w, 1),
            "energia_acumulada_kwh": round(energia_acumulada_kwh, 4),
            "co2_evitado_kg": round(co2_evitado_kg, 4),
            "economia_reais": round(economia_reais, 2),
            "arvores_equivalentes": round(arvores_equiv, 4)
        })

        hora += intervalo_minutos / 60

    return registros


def gerar_resumo(registros: list) -> dict:
    """Gera resumo do dia com totais e pico de geração."""
    ultimo = registros[-1]
    pico = max(registros, key=lambda r: r["potencia_w"])

    return {
        "energia_total_kwh": ultimo["energia_acumulada_kwh"],
        "co2_total_evitado_kg": ultimo["co2_evitado_kg"],
        "economia_total_reais": ultimo["economia_reais"],
        "potencia_pico_w": pico["potencia_w"],
        "hora_pico": pico["hora"],
        "arvores_equivalentes": ultimo["arvores_equivalentes"],
        "num_paineis": NUM_PAINEIS,
        "area_total_m2": NUM_PAINEIS * AREA_PAINEL_M2,
        "eficiencia_percentual": EFICIENCIA_PAINEL * 100,
    }


def main():
    print("=" * 55)
    print("  SolarTrack — Simulação Fotovoltaica Residencial")
    print("  FIAP 2026 — Sprint 2")
    print("=" * 55)

    # Simula o dia 172 (21 de junho — solstício de inverno no hemisfério sul)
    print("\n📡 Simulando geração para 21/junho (dia 172)...")
    registros = simular_dia(dia_do_ano=172, intervalo_minutos=30)
    resumo = gerar_resumo(registros)

    # Salva JSON para consumo pelo dashboard
    output = {
        "metadata": {
            "projeto": "SolarTrack",
            "sprint": "Sprint 2 — Prova de Conceito",
            "data_simulacao": "21/06/2026",
            "localizacao": "São Paulo, SP",
            "fator_emissao_co2_kg_kwh": FATOR_CO2_KG_KWH,
            "tarifa_energia_r_kwh": TARIFA_R_KWH
        },
        "sistema": {
            "num_paineis": NUM_PAINEIS,
            "area_painel_m2": AREA_PAINEL_M2,
            "eficiencia_percentual": EFICIENCIA_PAINEL * 100,
            "potencia_pico_instalada_wp": round(
                NUM_PAINEIS * AREA_PAINEL_M2 * EFICIENCIA_PAINEL * IRRADIANCIA_PICO_W_M2, 0
            )
        },
        "resumo_do_dia": resumo,
        "series_horaria": registros
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Exibe resumo no terminal
    print("\n✅ Simulação concluída! Resultados do dia:")
    print(f"   ⚡ Energia gerada:        {resumo['energia_total_kwh']:.2f} kWh")
    print(f"   🌡️  Potência de pico:      {resumo['potencia_pico_w']:.0f} W (às {resumo['hora_pico']})")
    print(f"   🌱 CO₂ evitado:           {resumo['co2_total_evitado_kg']:.3f} kg")
    print(f"   🌳 Equiv. em árvores/dia: {resumo['arvores_equivalentes']:.2f} árvores")
    print(f"   💰 Economia estimada:     R$ {resumo['economia_total_reais']:.2f}")
    print("\n📄 Dados salvos em: data.json")
    print("🌐 Abra o arquivo dashboard.html no navegador para visualizar.")
    print("=" * 55)


if __name__ == "__main__":
    main()
