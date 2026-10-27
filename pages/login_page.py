from playwright.sync_api import Page


class LoginPage:
    """Representa a tela de login do SauceDemo."""

    def __init__(self, page: Page):
        self.page = page
        self.campo_usuario = page.locator('[data-test="username"]')
        self.campo_senha = page.locator('[data-test="password"]')
        self.botao_login = page.locator('[data-test="login-button"]')
        self.mensagem_erro = page.locator('[data-test="error"]')

    def abrir(self):
        self.page.goto("/")

    def entrar(self, usuario: str, senha: str):
        self.campo_usuario.fill(usuario)
        self.campo_senha.fill(senha)
        self.botao_login.click()
