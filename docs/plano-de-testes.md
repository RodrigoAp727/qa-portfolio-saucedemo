# Plano de Testes – SauceDemo

## 1. Objetivo
Verificar se as funcionalidades principais da loja virtual [SauceDemo](https://www.saucedemo.com) funcionam corretamente, encontrar defeitos e garantir, com testes automatizados, que os fluxos críticos continuem funcionando.

## 2. Escopo

### Dentro do escopo
| Funcionalidade | Prioridade | Motivo |
|---|---|---|
| Login | Alta | Sem login, o cliente não acessa a loja |
| Listagem de produtos | Média | Cliente precisa ver o que comprar |
| Carrinho (adicionar/remover) | Alta | Etapa obrigatória para a compra |
| Checkout (finalizar compra) | Alta | É onde a loja gera receita |
| Ordenação de produtos | Baixa | Facilita, mas não impede a compra |

### Fora do escopo
- Pagamento real (o site é uma demonstração)
- Testes de segurança e de carga
- Versão mobile nativa

## 3. Abordagem
- **Testes manuais:** execução dos casos em [casos-de-teste.md](casos-de-teste.md) e sessões de teste exploratório.
- **Testes automatizados (E2E):** Python + Playwright + pytest, usando o padrão *Page Object Model*.
- **Integração contínua:** os testes automatizados rodam a cada push no GitHub Actions.

## 4. Usuários de teste
O SauceDemo fornece usuários com comportamentos diferentes (senha de todos: `secret_sauce`):

| Usuário | Comportamento |
|---|---|
| `standard_user` | Funciona normalmente |
| `locked_out_user` | Bloqueado, não consegue entrar |
| `problem_user` | Contém bugs propositais na interface |
| `performance_glitch_user` | Lentidão no login |
| `error_user` | Erros em algumas ações |
| `visual_user` | Diferenças visuais na interface |

## 5. Ambiente
- Navegador: Chromium (Playwright)
- Sistema: Windows 11 (local) e Ubuntu (GitHub Actions)

## 6. Riscos
| Risco | Impacto | Como reduzir |
|---|---|---|
| Site de demonstração fora do ar | Testes falham sem ser bug | Reexecutar e verificar o site manualmente |
| Mudança nos elementos da página | Testes automatizados quebram | Usar seletores estáveis (`data-test`) |

## 7. Critérios
- **Entrada:** site acessível e casos de teste revisados.
- **Saída:** todos os casos de prioridade alta executados e bugs encontrados registrados nas Issues.

## 8. Entregáveis
- Plano de testes (este documento)
- [Casos de teste](casos-de-teste.md)
- Bug reports (aba *Issues* do repositório)
- Testes automatizados (pasta `tests/`)
- Relatório de execução (gerado pelo GitHub Actions)
