import  pytest
from selene import browser,be,have
@pytest.fixture(autouse=True)

def test_browser_set_size():
   browser.config.window_width = 1080
   browser.config.window_height = 1920
   yield
   print('Закрываем браузер')
   browser.quit()


def test_browser_search(test_browser_set_size):
   browser.open('https://duckduckgo.com/')
   browser.element('[name="q"]').should(be.blank).type('hkvlfhlflfflfe').press_enter()
   browser.element('html').should(have.text('результаты не найдены'))