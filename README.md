# ChargeGrid Intelligence

## EV Challenge 2026 — FIAP x GoodWe

### Integração SolarTrack + Smart Charging

O ChargeGrid Intelligence é um protótipo desenvolvido para demonstrar a integração entre dados de geração de energia fotovoltaica e um sistema de Smart Charging para gerenciamento inteligente do carregamento de veículos elétricos.

A solução utiliza dados simulados de geração solar para demonstrar como a potência de carregamento pode ser ajustada de acordo com a disponibilidade de energia fotovoltaica.

---

# Equipe

| Integrante | RM |
|---|---:|
| Gabriel Jurado Nogueira | 571236 |
| Guilherme Henrique de Almeida | 568708 |
| Vinicius Torralles Ferreira Conduta | 570911 |
| Mariana Carminato | 573258 |
| Guilherme Garbelini | 571150 |

---

# Objetivo do Projeto

O objetivo do ChargeGrid Intelligence é demonstrar uma solução de carregamento inteligente para veículos elétricos utilizando informações de geração de energia solar.

O protótipo busca:

- Integrar dados de geração fotovoltaica com o carregamento de veículos elétricos;
- Identificar diferentes níveis de geração solar;
- Ajustar a potência de carregamento de acordo com a disponibilidade de energia;
- Aumentar o aproveitamento da energia renovável;
- Demonstrar o funcionamento do Smart Charging;
- Apresentar os dados por meio de uma dashboard funcional;
- Demonstrar a integração entre os componentes da solução.

---

# Arquitetura da Solução

O funcionamento da solução segue o seguinte fluxo:

```text
SolarTrack
    ↓
Dados de Geração Fotovoltaica
    ↓
Smart Charging
    ↓
Controle da Potência de Carregamento
    ↓
Carregador de Veículo Elétrico
    ↓
Dashboard
```

## Componentes

### SolarTrack

Representa a fonte de dados de geração de energia fotovoltaica.

O sistema utiliza diferentes valores de geração solar ao longo do dia para simular a disponibilidade de energia renovável.

### Smart Charging

É responsável por utilizar as informações de geração solar para definir a potência de carregamento do veículo elétrico.

No protótipo, a potência varia conforme o período de geração:

```text
Baixa geração solar → 1 kW

Geração solar disponível → 3 kW

Alta geração solar → 5 kW
```

### Dashboard

A dashboard apresenta os dados da integração em tempo real durante a demonstração.

São apresentados:

- Energia solar utilizada;
- Energia total carregada;
- Demanda do veículo;
- Participação solar;
- Potência atual de carregamento;
- Status do sistema;
- Geração solar por período;
- Exemplos de operação.

---

# Funcionamento do Smart Charging

Durante a simulação, o sistema utiliza diferentes períodos do dia para representar diferentes níveis de geração fotovoltaica.

| Horário | Geração Solar | Potência de Carregamento | Status |
|---|---:|---:|---|
| 00:00 | 0.00 kW | 1.00 kW | BAIXA GERAÇÃO SOLAR |
| 04:00 | 0.00 kW | 1.00 kW | BAIXA GERAÇÃO SOLAR |
| 08:00 | 1.80 kW | 3.00 kW | GERAÇÃO SOLAR DISPONÍVEL |
| 12:00 | 3.20 kW | 5.00 kW | ALTA GERAÇÃO SOLAR |
| 16:00 | 1.80 kW | 3.00 kW | GERAÇÃO SOLAR DISPONÍVEL |
| 20:00 | 0.00 kW | 1.00 kW | BAIXA GERAÇÃO SOLAR |

Dessa forma, a demonstração apresenta a atuação do Smart Charging de acordo com a disponibilidade de energia solar.

---

# Dashboard Funcional

A dashboard foi desenvolvida em HTML, CSS e JavaScript.

Diferentemente de uma tela apenas demonstrativa, o protótipo possui uma simulação funcional na qual os indicadores são atualizados durante o funcionamento do sistema.

Os valores apresentados são alterados conforme a evolução da simulação.

## Indicadores

### Energia Solar Utilizada

Apresenta a quantidade acumulada de energia solar utilizada durante o carregamento.

### Energia Carregada

Apresenta a quantidade acumulada de energia utilizada para o carregamento do veículo.

### Demanda do Veículo

Apresenta a potência de carregamento utilizada pelo veículo.

### Participação Solar

Representa a participação da energia solar em relação à energia total carregada.

A porcentagem é calculada dinamicamente durante a execução da dashboard.

---

# Controles da Dashboard

A dashboard possui controles para demonstrar o funcionamento do protótipo.

## Iniciar Carregamento

Inicia a simulação do Smart Charging.

Durante a execução:

- A potência de carregamento é alterada;
- A energia carregada aumenta;
- A geração solar é considerada;
- A energia solar utilizada aumenta quando há geração disponível;
- A participação solar é recalculada;
- O status do sistema é atualizado.

## Parar Carregamento

Interrompe a simulação do carregamento.

## Geração Solar

Permite visualizar e controlar o estado da geração solar utilizada na demonstração.

## Resetar

Retorna os indicadores para os valores iniciais e permite realizar uma nova demonstração.

## Controle de Potência

A dashboard também possui um controle de potência que permite alterar manualmente a potência de carregamento apresentada.

---

# Resultados Funcionais

Durante a demonstração, é possível observar a atuação integrada dos componentes.

Quando a geração solar é baixa, o sistema utiliza uma potência de carregamento menor.

Quando a geração solar aumenta, o Smart Charging aumenta a potência de carregamento.

Exemplo:

```text
00:00
Solar: 0.00 kW
Carregamento: 1.00 kW

08:00
Solar: 1.80 kW
Carregamento: 3.00 kW

12:00
Solar: 3.20 kW
Carregamento: 5.00 kW

16:00
Solar: 1.80 kW
Carregamento: 3.00 kW

20:00
Solar: 0.00 kW
Carregamento: 1.00 kW
```

Além da alteração da potência, a dashboard atualiza os indicadores de energia carregada, energia solar utilizada, demanda do veículo e participação solar.

---

# Justificativa Técnica

A utilização de HTML, CSS e JavaScript permite desenvolver uma interface simples, acessível e adequada para demonstrar o funcionamento do protótipo.

O JavaScript é utilizado para controlar a lógica da simulação e atualizar dinamicamente os indicadores da dashboard.

A utilização de dados simulados permite representar diferentes condições de geração fotovoltaica e demonstrar como o Smart Charging pode responder a essas variações.

A divisão entre geração solar, controle de carregamento e visualização facilita a compreensão da arquitetura proposta.

---

# Sustentabilidade e Eficiência Energética

O projeto está relacionado à sustentabilidade por utilizar a geração de energia fotovoltaica como referência para o gerenciamento do carregamento de veículos elétricos.

A utilização de Smart Charging permite demonstrar uma estratégia na qual a potência de carregamento pode ser ajustada conforme a disponibilidade de energia renovável.

A solução busca contribuir para:

- Maior aproveitamento da energia solar;
- Uso mais eficiente da energia disponível;
- Gerenciamento inteligente do carregamento;
- Integração entre energia renovável e mobilidade elétrica;
- Automação do processo de carregamento.

---

# Conexão com os Conteúdos da Disciplina

O projeto relaciona diferentes conteúdos trabalhados durante o desenvolvimento da solução.

## Programação

Utilização de Python e JavaScript para desenvolvimento da lógica de integração, simulação e atualização dos dados.

## Integração de Sistemas

O projeto demonstra a comunicação conceitual entre geração fotovoltaica, Smart Charging, carregador de veículo elétrico e dashboard.

## Automação

A alteração da potência de carregamento de acordo com os dados de geração solar representa uma lógica automatizada de controle.

## Sustentabilidade

A solução relaciona geração de energia renovável e mobilidade elétrica, buscando melhorar o aproveitamento da energia disponível.

## Visualização de Dados

A dashboard apresenta os dados de operação de maneira visual para facilitar o acompanhamento do sistema.

---

# Estrutura do Projeto

```text
sprint2-main/
│
├── dashboard_integracao.html
├── data.json
├── integracao.json
├── integracao.py
├── README.md
├── simulation.py
└── smart_charging.py
```

## Descrição dos Arquivos

### dashboard_integracao.html

Dashboard funcional desenvolvida em HTML, CSS e JavaScript.

### data.json

Arquivo utilizado para armazenar dados da simulação.

### integracao.json

Arquivo com os dados gerados pela integração.

### integracao.py

Script responsável pela integração e geração dos dados utilizados no projeto.

### simulation.py

Script relacionado à simulação do funcionamento do sistema.

### smart_charging.py

Script responsável pela lógica relacionada ao Smart Charging.

### README.md

Documentação do projeto e instruções de funcionamento.

---

# Como Executar

## 1. Baixar o projeto

Faça o download ou clone o repositório do GitHub para o computador.

---

## 2. Abrir a pasta do projeto

Localize a pasta do projeto no computador.

Exemplo:

```text
C:\Users\Vinicius\Downloads\sprint2-main
```

---

## 3. Abrir o PowerShell

No Windows:

1. Pressione `Windows + R`;
2. Digite:

```text
powershell
```

3. Pressione `Enter`.

---

## 4. Acessar a pasta pelo PowerShell

Digite:

```powershell
cd "C:\Users\Vinicius\Downloads\sprint2-main"
```

Caso o projeto esteja em outro local, substitua o caminho pelo caminho correto da pasta.

---

## 5. Executar a integração

Execute:

```powershell
python integracao.py
```

O terminal deverá apresentar informações semelhantes a:

```text
CHARGEGRID INTELLIGENCE
INTEGRAÇÃO SOLARTRACK + SMART CHARGING

Energia solar utilizada: 3.96 kWh
Energia total carregada: 24.50 kWh
Demanda do veículo: 7.0 kW
Participação solar: 16.2%

Integração concluída!
Dados salvos em: integracao.json
```

Esse comando gera/atualiza o arquivo:

```text
integracao.json
```

---

# 6. Iniciar o servidor da Dashboard

Ainda no PowerShell, execute:

```powershell
python -m http.server 8000
```

O terminal deverá apresentar uma mensagem semelhante a:

```text
Serving HTTP on :: port 8000
```

Não feche essa janela enquanto estiver utilizando a dashboard.

---

# 7. Abrir a Dashboard

Abra o navegador e acesse:

```text
http://localhost:8000
```

Será exibida a lista de arquivos do projeto.

Clique em:

```text
dashboard_integracao.html
```

---

# 8. Iniciar a demonstração

Quando a dashboard abrir:

1. Clique em **INICIAR CARREGAMENTO**;
2. A simulação será iniciada automaticamente;
3. Os valores da dashboard começarão a mudar;
4. A potência será alterada conforme os períodos de geração solar;
5. A energia carregada será acumulada;
6. A energia solar utilizada será atualizada;
7. A participação solar será recalculada;
8. A demanda do veículo será atualizada.

Durante a demonstração, é possível observar a variação da potência:

```text
1 kW → baixa geração solar

3 kW → geração solar disponível

5 kW → alta geração solar
```

---

# 9. Parar a demonstração

Para interromper o carregamento, clique em:

```text
PARAR CARREGAMENTO
```

---

# 10. Reiniciar a demonstração

Para começar novamente do zero, clique em:

```text
RESETAR
```

Depois clique novamente em:

```text
INICIAR CARREGAMENTO
```

---

# Demonstração

A demonstração funcional deve apresentar:

```text
Geração Solar
      ↓
Identificação da disponibilidade
      ↓
Smart Charging
      ↓
Ajuste da potência
      ↓
Carregamento do veículo
      ↓
Atualização da Dashboard
```

A alteração da potência durante os diferentes períodos demonstra a atuação integrada entre geração solar e Smart Charging.

---

# Vídeo da Demonstração

**Vídeo no YouTube:** COLOCAR LINK DO VÍDEO AQUI

O vídeo apresenta o funcionamento do protótipo e a integração entre os componentes da solução.

---

# Conclusão

O ChargeGrid Intelligence demonstra um protótipo de integração entre geração fotovoltaica e Smart Charging para veículos elétricos.

A dashboard funcional permite visualizar a alteração dos principais indicadores durante a simulação e demonstrar como diferentes níveis de geração solar podem influenciar a potência de carregamento.

O projeto apresenta uma aplicação prática de programação, integração de sistemas, automação, visualização de dados, sustentabilidade e eficiência energética.