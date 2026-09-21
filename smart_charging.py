from dataclasses import dataclass


@dataclass
class ChargingResult:
    potencia_solar_kw: float
    demanda_veiculo_kw: float
    potencia_disponivel_kw: float
    potencia_carregamento_kw: float
    energia_solar_utilizada_kwh: float
    percentual_solar: float
    status: str


class SmartChargingEngine:

    def __init__(
        self,
        potencia_maxima_carregador_kw: float = 7.4,
        potencia_minima_carregamento_kw: float = 1.0,
    ):
        self.potencia_maxima_carregador_kw = potencia_maxima_carregador_kw
        self.potencia_minima_carregamento_kw = potencia_minima_carregamento_kw

    def calcular(
        self,
        potencia_solar_kw: float,
        demanda_veiculo_kw: float,
    ) -> ChargingResult:

        potencia_solar_kw = max(0.0, potencia_solar_kw)

        demanda_limitada = min(
            demanda_veiculo_kw,
            self.potencia_maxima_carregador_kw
        )

        potencia_disponivel = min(
            potencia_solar_kw,
            self.potencia_maxima_carregador_kw
        )

        if potencia_disponivel >= demanda_limitada:
            potencia_carregamento = demanda_limitada
            status = "CARREGAMENTO COM ENERGIA SOLAR"

        elif potencia_disponivel >= self.potencia_minima_carregamento_kw:
            potencia_carregamento = potencia_disponivel
            status = "CARREGAMENTO OTIMIZADO"

        else:
            potencia_carregamento = self.potencia_minima_carregamento_kw
            status = "BAIXA GERAÇÃO SOLAR"

        energia_solar_utilizada = min(
            potencia_carregamento,
            potencia_solar_kw
        )

        percentual_solar = (
            energia_solar_utilizada / potencia_carregamento * 100
            if potencia_carregamento > 0
            else 0
        )

        return ChargingResult(
            potencia_solar_kw=round(potencia_solar_kw, 2),
            demanda_veiculo_kw=round(demanda_veiculo_kw, 2),
            potencia_disponivel_kw=round(potencia_disponivel, 2),
            potencia_carregamento_kw=round(potencia_carregamento, 2),
            energia_solar_utilizada_kwh=round(
                energia_solar_utilizada,
                2
            ),
            percentual_solar=round(
                percentual_solar,
                1
            ),
            status=status,
        )


if __name__ == "__main__":

    engine = SmartChargingEngine(
        potencia_maxima_carregador_kw=7.4
    )

    potencia_solar = 5.2
    demanda_veiculo = 7.0

    resultado = engine.calcular(
        potencia_solar_kw=potencia_solar,
        demanda_veiculo_kw=demanda_veiculo
    )

    print("=" * 50)
    print("CHARGEGRID INTELLIGENCE")
    print("SMART CHARGING ENGINE")
    print("=" * 50)

    print(f" Energia solar disponível: "
          f"{resultado.potencia_solar_kw:.2f} kW")

    print(f" Demanda do veículo: "
          f"{resultado.demanda_veiculo_kw:.2f} kW")

    print(f" Potência disponível: "
          f"{resultado.potencia_disponivel_kw:.2f} kW")

    print(f" Potência de carregamento: "
          f"{resultado.potencia_carregamento_kw:.2f} kW")

    print(f" Participação solar: "
          f"{resultado.percentual_solar:.1f}%")

    print(f" Status: {resultado.status}")

    print("=" * 50)