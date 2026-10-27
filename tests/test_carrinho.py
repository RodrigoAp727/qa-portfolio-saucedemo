from playwright.sync_api import expect

from pages.checkout_page import CarrinhoPage

MOCHILA = "sauce-labs-backpack"


def test_ct07_adicionar_produto_ao_carrinho(produtos_page):
    produtos_page.adicionar_ao_carrinho(MOCHILA)

    expect(produtos_page.contador_carrinho).to_have_text("1")


def test_ct08_remover_produto_na_listagem(produtos_page):
    produtos_page.adicionar_ao_carrinho(MOCHILA)
    produtos_page.remover_do_carrinho(MOCHILA)

    expect(produtos_page.contador_carrinho).to_be_hidden()


def test_ct09_produto_aparece_no_carrinho(produtos_page):
    produtos_page.adicionar_ao_carrinho(MOCHILA)
    produtos_page.abrir_carrinho()

    expect(CarrinhoPage(produtos_page.page).itens).to_have_text(["Sauce Labs Backpack"])
