from playwright.sync_api import Page


class ProdutosPage:
    """Representa a página de listagem de produtos (inventory)."""

    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator('[data-test="title"]')
        self.contador_carrinho = page.locator('[data-test="shopping-cart-badge"]')
        self.link_carrinho = page.locator('[data-test="shopping-cart-link"]')
        self.botao_menu = page.locator("#react-burger-menu-btn")
        self.link_logout = page.locator('[data-test="logout-sidebar-link"]')

    def adicionar_ao_carrinho(self, produto: str):
        # produto no formato do site, ex.: "sauce-labs-backpack"
        self.page.locator(f'[data-test="add-to-cart-{produto}"]').click()

    def remover_do_carrinho(self, produto: str):
        self.page.locator(f'[data-test="remove-{produto}"]').click()

    def abrir_carrinho(self):
        self.link_carrinho.click()

    def sair(self):
        self.botao_menu.click()
        self.link_logout.click()
