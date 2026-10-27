import pytest
from playwright.sync_api import expect

from pages.checkout_page import CarrinhoPage, CheckoutPage


@pytest.fixture
def checkout_page(produtos_page) -> CheckoutPage:
    """Adiciona um produto e avança até a tela de dados do cliente."""
    produtos_page.adicionar_ao_carrinho("sauce-labs-backpack")
    produtos_page.abrir_carrinho()
    CarrinhoPage(produtos_page.page).ir_para_checkout()
    return CheckoutPage(produtos_page.page)


def test_ct11_compra_completa(checkout_page):
    checkout_page.preencher_dados("Maria", "Silva", "01001-000")
    checkout_page.finalizar()

    expect(checkout_page.mensagem_sucesso).to_have_text("Thank you for your order!")


def test_ct12_checkout_sem_nome(checkout_page):
    checkout_page.preencher_dados("", "Silva", "01001-000")

    expect(checkout_page.mensagem_erro).to_contain_text("First Name is required")
