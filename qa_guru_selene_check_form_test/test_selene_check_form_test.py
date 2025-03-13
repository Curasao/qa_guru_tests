
import os
from selene import browser, have, be


def test_complete_todo():
    browser.open('/automation-practice-form')
    #проверка имени
    browser.element('#userName-wrapper').element('#firstName').should(be.blank).type('Dasha')
    #проверка фамилии
    browser.element('#userName-wrapper').element('#lastName').should(be.blank).type('Lenina')
    #проверка емейл
    browser.element('#userEmail-wrapper').element('#userEmail').should(be.blank).type('lenina5@email.com')
    #проверка чекбокса гендера
    browser.element('#genterWrapper').element('[for=gender-radio-2]').click()
    #проверка юзернейм
    browser.element('#userNumber-wrapper').element('#userNumber').should(be.blank).type('17123456784')
    #проверка календаря (датапикер)
    browser.element("#dateOfBirthInput").click()

    browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()

    browser.element('.react-datepicker__year-select').click().element('option[value="2008"]').click()

    browser.element('.react-datepicker__day--005').click()
    #проверка поля хобби
    browser.element("#hobbiesWrapper").click()

    browser.element('#hobbiesWrapper').element('[for=hobbies-checkbox-3]').click()
    #проверка поля subjects
    browser.element('#subjectsWrapper').element('#subjectsInput').should(be.blank).type('Lenina')
    #проверка поля текущий адрес
    browser.element('#currentAddress-wrapper').element('#currentAddress').should(be.blank).type('Lenina')
    #проверка кнопки "Загрузить фото"
    browser.element('#uploadPicture').type(os.path.abspath('water.jpg'))
    #проверка дропдаун списков город и штат

    #отправка формы
    browser.element('#submit').click()


    # проверяем данные в таблице

    browser.element(".table").should(have.text('Dasha'))
    browser.element(".table").should(have.text('Lenina'))
    browser.element(".table").should(have.text('Female'))
    browser.element(".table").should(have.text('17123456784'))
    browser.element(".table").should(have.text('05 March,2008'))
    browser.element(".table").should(have.text('Lenina'))
    browser.element(".table").should(have.text('Reading'))
    browser.element(".table").should(have.text('water.jpg'))
    browser.element(".table").should(have.text('Lenina'))
    browser.element(".table").should(have.text('Uttar Pradesh Lucknow'))

    browser.element('#state').click().element('#react-select-3-option-1').click()

    browser.element('#city').click().element('#react-select-4-option-2').click()
