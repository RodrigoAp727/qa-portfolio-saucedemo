# Casos de Teste – SauceDemo

Legenda de status: ✅ Passou · ❌ Falhou · ⏳ Não executado
Coluna **Auto**: 🤖 = automatizado em `tests/`

## Login

| ID | Cenário | Passos | Resultado esperado | Prioridade | Auto | Status |
|---|---|---|---|---|---|---|
| CT01 | Login com sucesso | 1. Abrir o site 2. Usuário `standard_user` 3. Senha `secret_sauce` 4. Clicar em Login | Exibe a página "Products" | Alta | 🤖 | ⏳ |
| CT02 | Login com senha incorreta | 1. Usuário `standard_user` 2. Senha `errada` 3. Login | Mensagem: "Username and password do not match any user in this service" | Alta | 🤖 | ⏳ |
| CT03 | Login com usuário bloqueado | 1. Usuário `locked_out_user` 2. Senha `secret_sauce` 3. Login | Mensagem: "Sorry, this user has been locked out." | Alta | 🤖 | ⏳ |
| CT04 | Login com campos vazios | 1. Deixar usuário e senha vazios 2. Login | Mensagem: "Username is required" | Média | 🤖 | ⏳ |
| CT05 | Login sem senha | 1. Usuário `standard_user` 2. Senha vazia 3. Login | Mensagem: "Password is required" | Média | 🤖 | ⏳ |
| CT06 | Logout | 1. Fazer login 2. Abrir menu ☰ 3. Clicar em Logout | Volta para a tela de login | Média | 🤖 | ⏳ |

## Carrinho

| ID | Cenário | Passos | Resultado esperado | Prioridade | Auto | Status |
|---|---|---|---|---|---|---|
| CT07 | Adicionar produto ao carrinho | 1. Login 2. Clicar em "Add to cart" na mochila | Ícone do carrinho mostra "1" | Alta | 🤖 | ⏳ |
| CT08 | Remover produto na listagem | 1. Adicionar mochila 2. Clicar em "Remove" | Contador do carrinho desaparece | Alta | 🤖 | ⏳ |
| CT09 | Produto aparece no carrinho | 1. Adicionar mochila 2. Abrir carrinho | Mochila listada no carrinho | Alta | 🤖 | ⏳ |
| CT10 | Adicionar vários produtos | 1. Adicionar 3 produtos diferentes | Contador mostra "3" | Média | | ⏳ |

## Checkout

| ID | Cenário | Passos | Resultado esperado | Prioridade | Auto | Status |
|---|---|---|---|---|---|---|
| CT11 | Compra completa | 1. Adicionar produto 2. Carrinho → Checkout 3. Preencher nome, sobrenome e CEP 4. Continue 5. Finish | Mensagem "Thank you for your order!" | Alta | 🤖 | ⏳ |
| CT12 | Checkout sem nome | 1. Ir até o checkout 2. Deixar nome vazio 3. Continue | Mensagem: "First Name is required" | Alta | 🤖 | ⏳ |
| CT13 | Checkout sem CEP | 1. Ir até o checkout 2. Preencher nome e sobrenome, CEP vazio 3. Continue | Mensagem: "Postal Code is required" | Média | | ⏳ |
| CT14 | Valor total correto | 1. Adicionar 2 produtos 2. Ir até o resumo do checkout | Total = soma dos preços + imposto | Alta | | ⏳ |

## Produtos

| ID | Cenário | Passos | Resultado esperado | Prioridade | Auto | Status |
|---|---|---|---|---|---|---|
| CT15 | Ordenar por preço (menor → maior) | 1. Login 2. Selecionar "Price (low to high)" | Produtos em ordem crescente de preço | Baixa | | ⏳ |
| CT16 | Ordenar por nome (Z → A) | 1. Login 2. Selecionar "Name (Z to A)" | Produtos em ordem alfabética inversa | Baixa | | ⏳ |
| CT17 | Abrir detalhes do produto | 1. Login 2. Clicar no nome de um produto | Página do produto com nome, descrição e preço | Média | | ⏳ |

---

> 💡 **Exercício:** repita os casos acima usando o usuário `problem_user`. Vários vão falhar. Cada falha é um bug para registrar na aba *Issues* usando o modelo de bug report.
