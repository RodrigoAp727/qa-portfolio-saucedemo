from playwright.sync_api import Page


class CarrinhoPage:
    """Representa a página do carrinho."""

    def __init__(self, page: Page):
        self.page = page
        self.itens = page.locator('[data-test="inventory-item-name"]')
        self.botao_checkout = page.locator('[data-test="checkout"]')

    def ir_para_checkout(self):
        self.botao_checkout.click()


class CheckoutPage:
    """Representa as etapas do checkout: dados do cliente, resumo e confirmação."""

    def __init__(self, page: Page):
        self.page = page
        self.campo_nome = page.locator('[data-test="firstName"]')
        self.campo_sobrenome = page.locator('[data-test="lastName"]')
        self.campo_cep = page.locator('[data-test="postalCode"]')
        self.botao_continuar = page.locator('[data-test="continue"]')
        self.botao_finalizar = page.locator('[data-test="finish"]')
        self.mensagem_erro = page.locator('[data-test="error"]')
        self.mensagem_sucesso = page.locator('[data-test="complete-header"]')

    def preencher_dados(self, nome: str, sobrenome: str, cep: str):
        self.campo_nome.fill(nome)
        self.campo_sobrenome.fill(sobrenome)
        self.campo_cep.fill(cep)
        self.botao_continuar.click()

    def finalizar(self):
        self.botao_finalizar.click()
