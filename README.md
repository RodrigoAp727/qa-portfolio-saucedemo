# 🧪 QA Portfolio – SauceDemo

![Testes E2E](https://github.com/RodrigoAp727/qa-portfolio-saucedemo/actions/workflows/testes.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-E2E-green)

Projeto de **Quality Assurance** aplicado à loja virtual de demonstração [SauceDemo](https://www.saucedemo.com).
O objetivo é mostrar o ciclo completo de trabalho de um QA: **planejar, testar manualmente, reportar bugs e automatizar**.

---

## 📌 O que tem neste projeto

| Entregável | Onde está |
|---|---|
| Plano de testes | [`docs/plano-de-testes.md`](docs/plano-de-testes.md) |
| Casos de teste (17 cenários) | [`docs/casos-de-teste.md`](docs/casos-de-teste.md) |
| Bug reports | Aba [Issues](../../issues) |
| Testes automatizados (E2E) | [`tests/`](tests) |
| Integração contínua | [`.github/workflows/testes.yml`](.github/workflows/testes.yml) |

## 🛠️ Tecnologias

- **Python**: linguagem dos testes
- **Playwright**: automação do navegador
- **pytest**: execução dos testes e asserções
- **pytest-html**: relatório de execução
- **GitHub Actions**: roda os testes automaticamente a cada push

## 🧱 Estrutura

```
├── docs/               # Plano e casos de teste
├── pages/              # Page Objects (uma classe por tela)
├── tests/              # Testes automatizados
├── .github/workflows/  # Pipeline de CI
├── pytest.ini          # Configuração do pytest
└── requirements.txt    # Dependências
```

O projeto usa o padrão **Page Object Model**: cada tela do site tem uma classe em `pages/` com seus elementos e ações. Os testes só descrevem *o que* fazer, e as páginas sabem *como*. Se o site mudar, só a página precisa ser ajustada.

## ▶️ Como executar

```bash
# 1. Criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/Mac

# 2. Instalar dependências
pip install -r requirements.txt
python -m playwright install chromium

# 3. Rodar os testes
pytest

# Ver o navegador funcionando
pytest --headed --slowmo 500
```

O relatório fica em `reports/relatorio.html`.

## ✅ Cobertura automatizada

| Funcionalidade | Casos |
|---|---|
| Login | CT01–CT06 |
| Carrinho | CT07–CT09 |
| Checkout | CT11–CT12 |

## 🐞 Bugs encontrados

Os bugs foram encontrados em testes manuais com o usuário `problem_user` e estão registrados na aba [Issues](../../issues).

| ID | Resumo | Severidade |
|---|---|---|
| _em andamento_ | | |

## 🚀 Próximos passos

- [ ] Automatizar CT10, CT13–CT17
- [ ] Testes de API
- [ ] Testes de performance com k6

---

👤 **Rodrigo Campos**: [LinkedIn](https://linkedin.com/in/SEU_PERFIL)
