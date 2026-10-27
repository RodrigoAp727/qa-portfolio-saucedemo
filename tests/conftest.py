import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage

# Credenciais públicas de demonstração do SauceDemo
USUARIO_PADRAO = "standard_user"
SENHA_PADRAO = "secret_sauce"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Abre o site e entrega a tela de login pronta para uso."""
    tela = LoginPage(page)
    tela.abrir()
    return tela


@pytest.fixture
def produtos_page(login_page: LoginPage) -> ProdutosPage:
    """Faz login com o usuário padrão e entrega a página de produtos."""
    login_page.entrar(USUARIO_PADRAO, SENHA_PADRAO)
    return ProdutosPage(login_page.page)
