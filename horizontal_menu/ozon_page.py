from tests.config import url
from tests.config import url_help
import pytest
# ссылки для перехода ( куда жмякать пайтесту )

class OzonPage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        pytest.driver.get(url)

    def visit_help(self):
        pytest.driver.get(url_help)

    # horizontal menu

    def get_shops(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Магазины')]")

    def get_brands(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "Бренды")]')

    def get_electronics(self):
        return pytest.driver.find_elements_by_xpath('//*[contains(text(), "Электроника")]')[1]

    def get_clothes(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "Одежда и обувь")]')

    def get_live(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "LIVE")]')

    def get_stocks(self):
        return pytest.driver.find_element_by_xpath('//*[contains(text(), "Акции")]')

    def get_products_for_children(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Детские товары')]")[1]

    def get_house_and_garden(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Дом и сад')]")[1]

    def get_discount(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Dисконт')]")[1]

    def get_ozon_card(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Card')]")[1]

    def get_ozon_express(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Express')]")[1]

    def get_ozon_travel(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Travel')]")[1]

    def get_premium(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Premium')]")[1]

    def get_top_fashion(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'TOP Fashion')]")

    #navigations menu

    def get_business(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon для бизнеса')]")[0]

    def get_mob_app(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Мобильное приложение')]")

    def get_referral(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Реферальная программа')]")[0]

    def get_earn_money(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Зарабатывай с Ozon')]")

    def get_certificates(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Подарочные сертификаты')]")[0]

    def get_points_of_issue(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Пункты выдачи')]")

    def get_help(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Помощь')]")[0]

    # help menu

    def get_order_status(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как посмотреть статус заказа')]")[1]

    def get_edit_or_cancel_order(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Как редактировать и отменить заказ')]")

    def get_order_was_canceled(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Мой заказ отменили')]")[1]

    def get_pick_up_order(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как получить заказ')]")[1]

    def get_how_to_place_an_order(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Не получается сделать заказ')]")[1]

    def get_when_returned_money(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Когда вернутся деньги за отмену или возврат')]")[0]

    def get_payment_methods(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Способы оплаты')]")[1]

    def get_payment_error(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Ошибка при оплате')]")[1]

    def get_receipts_and_documents(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Чеки и документы')]")[1]

    def get_ozon_points(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Баллы Ozon и баллы Ozon.Card')]")[1]

    def get_ozon_personal_account(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Ozon.лицевой счёт для организаций')]")

    def get_fraud_in_internet(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Мошенничество в интернете')]")[1]

    def get_protection_against_hacking(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как защитить аккаунт от взлома')]")[1]

    def get_how_to_return_product(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Как вернуть товар')]")[2]

    def get_warranty(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Гарантия')]")[0]

    def get_specifications(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Характеристики и наличие')]")[1]

    def get_shiping_cost(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Стоимость доставки')]")[1]

    def get_delivery_methods(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Способы доставки')]")[1]

    def get_fitting(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Примерка одежды и обуви')]")[1]

    def get_delivery_from_abroad(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Доставка из-за рубежа')]")

    def get_delivery_abroad(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Доставка за пределы России')]")[1]

    def get_delivery_ozon_express(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Доставка Ozon Express')]")[1]

    def get_certific(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Сертификаты')]")

    def get_koupons(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Купоны и кодовые слова')]")[1]

    def get_payment_menu(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Оплата')]")[0]

    def get_installment_plan(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Ozon Рассрочка')]")

    def get_extract(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Выписки и справки')]")

    def get_delivery_menu(self):
        return pytest.driver.find_elements_by_xpath("//*[contains(text(), 'Доставка')]")[0]

    def get_regular_delivery(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Регулярная доставка')]")

    def get_purchase_as_a_gift(self):
        return pytest.driver.find_element_by_xpath("//*[contains(text(), 'Покупка в подарок')]")


