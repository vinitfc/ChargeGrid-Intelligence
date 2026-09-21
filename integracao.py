import json

print("=" * 60)
print("CHARGEGRID INTELLIGENCE")
print("INTEGRAÇÃO SOLARTRACK + SMART CHARGING")
print("=" * 60)

energia_solar_utilizada = 3.96
energia_total_carregada = 24.50
demanda_veiculo = 7.0

exemplos_operacao = [
    {
        "hora": "00:00",
        "solar_kw": 0.00,
        "carregamento_kw": 1.00,
        "status": "BAIXA GERAÇÃO SOLAR"
    },
    {
        "hora": "04:00",
        "solar_kw": 0.00,
        "carregamento_kw": 1.00,
        "status": "BAIXA GERAÇÃO SOLAR"
    },
    {
        "hora": "08:00",
        "solar_kw": 1.80,
        "carregamento_kw": 3.00,
        "status": "GERAÇÃO SOLAR DISPONÍVEL"
    },
    {
        "hora": "12:00",
        "solar_kw": 3.20,
        "carregamento_kw": 5.00,
        "status": "ALTA GERAÇÃO SOLAR"
    },
    {
        "hora": "16:00",
        "solar_kw": 1.80,
        "carregamento_kw": 3.00,
        "status": "GERAÇÃO SOLAR DISPONÍVEL"
    },
    {
        "hora": "20:00",
        "solar_kw": 0.00,
        "carregamento_kw": 1.00,
        "status": "BAIXA GERAÇÃO SOLAR"
    },
    {
        "hora": "24:00",
        "solar_kw": 0.00,
        "carregamento_kw": 1.00,
        "status": "BAIXA GERAÇÃO SOLAR"
    }
]

dados = {
    "sistema": "ChargeGrid Intelligence",
    "integracao": "SolarTrack + Smart Charging",
    "energia_solar_utilizada_kwh": energia_solar_utilizada,
    "energia_total_carregada_kwh": energia_total_carregada,
    "demanda_veiculo_kw": demanda_veiculo,
    "exemplos_operacao": exemplos_operacao
}

with open("integracao.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

participacao = (
    energia_solar_utilizada / energia_total_carregada
) * 100

print()
print(f"Energia solar utilizada: {energia_solar_utilizada:.2f} kWh")
print(f"Energia total carregada: {energia_total_carregada:.2f} kWh")
print(f"Demanda do veículo: {demanda_veiculo:.1f} kW")
print(f"Participação solar: {participacao:.1f}%")

print()
print("Exemplos de operação:")

for item in exemplos_operacao:
    print(
        f"{item['hora']} | "
        f"Solar: {item['solar_kw']:.2f} kW | "
        f"Carregamento: {item['carregamento_kw']:.2f} kW | "
        f"{item['status']}"
    )

print()
print("Integração concluída!")
print("Dados salvos em: integracao.json")
print("=" * 60)