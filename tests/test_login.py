import pytest
from playwright.sync_api import expect

from pages.produtos_page import ProdutosPage
from tests.conftest import SENHA_PADRAO, USUARIO_PADRAO


def test_ct01_login_com_sucesso(login_page):
    login_page.entrar(USUARIO_PADRAO, SENHA_PADRAO)

    expect(ProdutosPage(login_page.page).titulo).to_have_text("Products")


@pytest.mark.parametrize(
    "caso, usuario, senha, erro_esperado",
    [
        ("CT02", USUARIO_PADRAO, "senha_errada",
         "Username and password do not match any user in this service"),
        ("CT03", "locked_out_user", SENHA_PADRAO,
         "Sorry, this user has been locked out."),
        ("CT04", "", "", "Username is required"),
        ("CT05", USUARIO_PADRAO, "", "Password is required"),
    ],
    ids=["CT02-senha-incorreta", "CT03-usuario-bloqueado",
         "CT04-campos-vazios", "CT05-sem-senha"],
)
def test_login_invalido_exibe_erro(login_page, caso, usuario, senha, erro_esperado):
    login_page.entrar(usuario, senha)

    expect(login_page.mensagem_erro).to_contain_text(erro_esperado)


def test_ct06_logout(produtos_page):
    produtos_page.sair()

    expect(produtos_page.page.locator('[data-test="login-button"]')).to_be_visible()
