import allure
from allure_commons.types import Severity
from selene import browser, by, have, be

@allure.tag("Web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Curasao")
@allure.feature("Задачи в репозитории")
@allure.story("Пишем простой тест на Selenide")
@allure.link("https://github.com", name="GitHub Homepage")

def test_issue_title_selene():

  with allure.step('Открываем главную страницу'):
    browser.driver.maximize_window()
    repository_name = "eroshenkoam/allure-qaguru"
    issue_name = "Пишем простой тест на Selenide"
  with allure.step('Открываем главную страницу'):
    browser.open("https://github.com")
  with allure.step('Ищем репозиторий'):
    browser.element(".search-input-container").click()
    browser.element("#query-builder-test").type(repository_name)
    browser.element("#query-builder-test").press_enter()
    browser.element(f'[href="/{repository_name}"]').click()
    browser.element("#issues-tab").click()
    browser.element(by.text(issue_name)).click()
  with allure.step('Ищем элемент'):
    browser.element("[data-testid='issue-title']").should(be.visible)
    browser.element("[data-testid='issue-title']").should(have.text(issue_name))
    browser.element("#issues-tab").click()
    browser.element(by.text("Пишем простой тест на Selenide")).click()
  with allure.step('Проверка заголовка'):
    browser.element("[data-testid='issue-title']").should(be.visible)
    browser.element("[data-testid='issue-title']").should(have.text("Пишем простой тест на Selenide"))