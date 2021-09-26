import pytest

from pages.horizontal_menu.ozon_page import OzonPage
#tests of horizontal menu
from pages.horizontal_menu.shops_page import ShopPage
from pages.horizontal_menu.brands_page import BrandsPage
from pages.horizontal_menu.electronics_page import ElectronicsPage
from pages.horizontal_menu.clothes_page import ClothesPage
from pages.horizontal_menu.live_pages import LivePage
from pages.horizontal_menu.stocks_pages import StocksPage
from pages.horizontal_menu.product_for_children_page import Products_For_Children
from pages.horizontal_menu.house_and_garden_page import House_And_Garden
from pages.horizontal_menu.discount_page import Discount
from pages.horizontal_menu.ozon_card_page import Ozon_Card
from pages.horizontal_menu.ozon_express_page import Ozon_Express
from pages.horizontal_menu.ozon_travel_page import Ozon_Travel
from pages.horizontal_menu.premium_page import Premium
from pages.horizontal_menu.top_fashion_page import TOP_Fashion
#tests of navigations menu
from pages.navigation_menu.business_page import Business
from pages.navigation_menu.mob_app_page import Mob_App
from pages.navigation_menu.referral_page import Referral
from pages.navigation_menu.earn_money_page import Earn_money
from pages.navigation_menu.certificates_page import Certificates
from pages.navigation_menu.points_of_issue_page import Points_Of_Issue
from pages.navigation_menu.help_page import Help
#tests of help menu
from pages.help_menu.order_status_page import Order_Status
from pages.help_menu.edit_or_cancel_order_page import Edit_Or_Cancel_Order
from pages.help_menu.order_was_canceled_page import Order_Was_Canceled
from pages.help_menu.pick_up_order_page import Pick_Up_Order
from pages.help_menu.how_to_place_an_order_page import How_To_Place_An_Order
from pages.help_menu.when_returned_money_page import When_Returned_Money
from pages.help_menu.payment_methods_page import Payment_Methods
from pages.help_menu.payment_error_page import Payment_Error
from pages.help_menu.receipts_and_documents_page import Receipts_And_Documents
from pages.help_menu.ozon_points_page import Ozon_Points
from pages.help_menu.ozon_personal_account_page import Ozon_Personal_Account
from pages.help_menu.fraud_in_internet_page import Fraud_In_Internet
from pages.help_menu.protection_against_hacking_page import Protection_Against_Hacking
from pages.help_menu.how_to_return_product_page import How_To_Return_Product
from pages.help_menu.warranty_page import Warranty
from pages.help_menu.specifications_page import Specifications
from pages.help_menu.shipping_cost_page import Shiping_Cost
from pages.help_menu.delivery_methods_page import Delivery_methods
from pages.help_menu.fitting_page import Fitting
from pages.help_menu.delivery_from_abroad_page import Delivery_From_Abroad
from pages.help_menu.delivery_abroad_page import Delivery_Abroad
from pages.help_menu.delivery_ozon_express_page import Delivery_Ozon_Express
from pages.help_menu.certific_page import Сertific
from pages.help_menu.coupons_page import Koupons
from pages.help_menu.installment_plan_page import Installment_Plan
from pages.help_menu.extract_page import Extract
from pages.help_menu.regular_delivery_page import Regular_Delivery
from pages.help_menu.purchase_as_a_gift_page import Purchase_As_A_Gift


def test_visit(driver): #тест 1.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_shops().is_displayed()

#tests of horizontal menu

def test_shops(driver): #тест 2.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_shops().click()
    shop_page = ShopPage(driver)
    pytest.driver.implicitly_wait(5)
    assert shop_page.get_shops()[1].is_displayed()

def test_brands(driver): #тест 3.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_brands().click()
    brand_page = BrandsPage(driver)
    pytest.driver.implicitly_wait(5)
    assert brand_page.get_brands()[0].is_displayed()

def test_electronics(driver): #тест 4.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_electronics().click()
    electronics_page = ElectronicsPage(driver)
    pytest.driver.implicitly_wait(5)
    assert electronics_page.get_electronics()[3].is_displayed()

def test_clothes(driver): #тест 5.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_clothes().click()
    clothes_page = ClothesPage(driver)
    pytest.driver.implicitly_wait(5)
    assert clothes_page.get_clothes().is_displayed()

def test_live(driver): #тест 6.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_live().click()
    live_page = LivePage(driver)
    pytest.driver.implicitly_wait(5)
    assert live_page.get_live().is_displayed()

def test_stocks(driver): #тест 7.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_stocks().click()
    stocks_page = StocksPage(driver)
    pytest.driver.implicitly_wait(5)
    assert stocks_page.get_stocks().is_displayed()

def test_products_for_children(driver): #тест 8.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_products_for_children().click()
    products_for_children = Products_For_Children(driver)
    pytest.driver.implicitly_wait(5)
    assert products_for_children.get_products_for_children()[0].is_displayed()

def test_house_and_garden(driver): #тест 9.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_house_and_garden().click()
    house_and_garden = House_And_Garden(driver)
    pytest.driver.implicitly_wait(5)
    assert house_and_garden.get_house_and_garden()[2].is_displayed()

def test_discount(driver): #тест 10.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_discount().click()
    discount = Discount(driver)
    pytest.driver.implicitly_wait(5)
    assert discount.get_discount().is_displayed()

def test_ozon_card(driver): #тест 11.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_ozon_card().click()
    ozon_card = Ozon_Card(driver)
    pytest.driver.implicitly_wait(5)
    assert ozon_card.get_ozon_card()[0].is_displayed()

def test_ozon_express(driver): #тест 12.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_ozon_express().click()
    ozon_express = Ozon_Express(driver)
    pytest.driver.implicitly_wait(5)
    assert ozon_express.get_ozon_express().is_displayed()

def test_ozon_travel(driver): #тест 13.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_ozon_travel().click()
    ozon_travel = Ozon_Travel(driver)
    pytest.driver.implicitly_wait(5)
    assert ozon_travel.get_ozon_travel()[0].is_displayed()

def test_premium(driver): #тест 14.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_premium().click()
    premium = Premium(driver)
    pytest.driver.implicitly_wait(5)
    assert premium.get_premium().is_displayed()

def test_top_fashion(driver): #тест 15.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_top_fashion().click()
    top_fashion = TOP_Fashion(driver)
    pytest.driver.implicitly_wait(5)
    assert top_fashion.get_top_fashion().is_displayed()

#tests of navigations menu

def test_business(driver): #тест 16. Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_business().click()
    business = Business(driver)
    pytest.driver.implicitly_wait(5)
    assert business.get_business().is_displayed()

def test_mob_app(driver): #тест 17.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_mob_app().click()
    mob_app = Mob_App(driver)
    pytest.driver.implicitly_wait(5)
    assert mob_app.get_mob_app().is_displayed()

def test_referral(driver): #тест 18.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_referral().click()
    referral = Referral(driver)
    pytest.driver.implicitly_wait(5)
    assert referral.get_referral()[0].is_displayed()

def test_earn_money(driver): #тест 19.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_earn_money().click()
    earn_money = Earn_money(driver)
    pytest.driver.implicitly_wait(5)
    assert earn_money.get_earn_money().is_displayed()

def test_certificates(driver): #тест 20.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_certificates().click()
    certificates = Certificates(driver)
    pytest.driver.implicitly_wait(5)
    assert certificates.get_certificates().is_displayed()

def test_points_of_issue(driver): #тест 21.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_points_of_issue().click()
    points_of_issue = Points_Of_Issue(driver)
    pytest.driver.implicitly_wait(5)
    assert points_of_issue.get_points_of_issue()[2].is_displayed()

def test_help(driver): #тест 22.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_help().click()
    help = Help(driver)
    pytest.driver.implicitly_wait(5)
    assert help.get_help()[0].is_displayed()

#tests of help menu

def test_help(driver): #тест 23.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_order_status().click()
    order_status = Order_Status(driver)
    pytest.driver.implicitly_wait(5)
    assert order_status.get_order_status()[1].is_displayed()

def test_edit_or_cancel_order(driver):  # тест 24.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_edit_or_cancel_order().click()
    edit_or_cancel_order = Edit_Or_Cancel_Order(driver)
    pytest.driver.implicitly_wait(5)
    assert edit_or_cancel_order.get_edit_or_cancel_order()[1].is_displayed()

def test_order_was_canceled(driver):  # тест 25.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_order_was_canceled().click()
    order_was_canceled = Order_Was_Canceled(driver)
    pytest.driver.implicitly_wait(5)
    assert order_was_canceled.get_order_was_canceled()[2].is_displayed()

def test_pick_up_order(driver):  # тест 26.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_pick_up_order().click()
    pick_up_order = Pick_Up_Order(driver)
    pytest.driver.implicitly_wait(5)
    assert pick_up_order.get_pick_up_order()[1].is_displayed()

def test_how_to_place_an_order(driver):  # тест 27.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_how_to_place_an_order().click()
    how_to_place_an_order = How_To_Place_An_Order(driver)
    pytest.driver.implicitly_wait(5)
    assert how_to_place_an_order.get_how_to_place_an_order().is_displayed()

def test_when_returned_money(driver):  # тест 28.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_when_returned_money().click()
    when_returned_money = When_Returned_Money(driver)
    pytest.driver.implicitly_wait(5)
    assert when_returned_money.get_when_returned_money()[1].is_displayed()

def test_payment_methods(driver):  # тест 29.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_payment_methods().click()
    payment_methods = Payment_Methods(driver)
    pytest.driver.implicitly_wait(5)
    assert payment_methods.get_payment_methods()[1].is_displayed()

def test_payment_error(driver):  # тест 30.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_payment_error().click()
    payment_error = Payment_Error(driver)
    pytest.driver.implicitly_wait(5)
    assert payment_error.get_payment_error()[1].is_displayed()

def test_receipts_and_documents(driver):  # тест 31.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_receipts_and_documents().click()
    receipts_and_documents = Receipts_And_Documents(driver)
    pytest.driver.implicitly_wait(5)
    assert receipts_and_documents.get_receipts_and_documents()[1].is_displayed()

def test_points(driver):  # тест 32.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_ozon_points().click()
    ozon_points = Ozon_Points(driver)
    pytest.driver.implicitly_wait(5)
    assert ozon_points.get_ozon_points()[6].is_displayed()

def test_points(driver):  # тест 33.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_ozon_personal_account().click()
    ozon_personal_account = Ozon_Personal_Account(driver)
    pytest.driver.implicitly_wait(5)
    assert ozon_personal_account.get_ozon_personal_account()[1].is_displayed()

def test_Fraud_In_Internet(driver):  # тест 34.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_fraud_in_internet().click()
    fraud_in_internet = Fraud_In_Internet(driver)
    pytest.driver.implicitly_wait(5)
    assert fraud_in_internet.get_fraud_in_internet()[2].is_displayed()

def test_protection_against_hacking(driver):  # тест 35.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_protection_against_hacking().click()
    protection_against_hacking = Protection_Against_Hacking(driver)
    pytest.driver.implicitly_wait(5)
    assert protection_against_hacking.get_protection_against_hacking().is_displayed()

def test_how_to_return_product(driver):  # тест 36.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_how_to_return_product().click()
    how_to_return_product = How_To_Return_Product(driver)
    pytest.driver.implicitly_wait(5)
    assert how_to_return_product.get_how_to_return_product()[1].is_displayed()

def test_warranty(driver):  # тест 37.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_warranty().click()
    warranty = Warranty(driver)
    pytest.driver.implicitly_wait(5)
    assert warranty.get_warranty().is_displayed()

def test_specifications(driver):  # тест 38.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_specifications().click()
    specifications = Specifications(driver)
    pytest.driver.implicitly_wait(5)
    assert specifications.get_specifications()[1].is_displayed()

def test_shiping_cost(driver):  # тест 39.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_shiping_cost().click()
    shiping_cost = Shiping_Cost(driver)
    pytest.driver.implicitly_wait(5)
    assert shiping_cost.get_shiping_cost()[5].is_displayed()

def test_delivery_methods(driver):  # тест 40.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_delivery_methods().click()
    delivery_methods = Delivery_methods(driver)
    pytest.driver.implicitly_wait(5)
    assert delivery_methods.get_delivery_methods()[0].is_displayed()

def test_fitting(driver):  # тест 41.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_fitting().click()
    fitting = Fitting(driver)
    pytest.driver.implicitly_wait(5)
    assert fitting.get_fitting()[1].is_displayed()

def test_delivery_from_abroad(driver):  # тест 42.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_delivery_from_abroad().click()
    delivery_from_abroad = Delivery_From_Abroad(driver)
    pytest.driver.implicitly_wait(5)
    assert delivery_from_abroad.get_delivery_from_abroad()[0].is_displayed()

def test_delivery_abroad(driver):  # тест 43.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_delivery_abroad().click()
    delivery_abroad = Delivery_Abroad(driver)
    pytest.driver.implicitly_wait(5)
    assert delivery_abroad.get_delivery_abroad()[1].is_displayed()

def test_delivery_ozon_express(driver):  # тест 44.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_delivery_ozon_express().click()
    delivery_ozon_express = Delivery_Ozon_Express(driver)
    pytest.driver.implicitly_wait(5)
    assert delivery_ozon_express.get_delivery_ozon_express()[1].is_displayed()

def test_certific(driver):  # тест 45.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_certific().click()
    certific = Сertific(driver)
    pytest.driver.implicitly_wait(5)
    assert certific.get_certific()[2].is_displayed()

def test_koupons(driver):  # тест 46.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_koupons().click()
    koupons = Koupons(driver)
    pytest.driver.implicitly_wait(5)
    assert koupons.get_koupons()[1].is_displayed()

def test_installment_plan(driver):  # тест 47.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_payment_menu().click()
    ozon_page.get_installment_plan().click()
    installment_plan =Installment_Plan(driver)
    pytest.driver.implicitly_wait(5)
    assert installment_plan.get_installment_plan()[1].is_displayed()

def test_extract(driver):  # тест 48.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_payment_menu().click()
    ozon_page.get_extract().click()
    extract = Extract(driver)
    pytest.driver.implicitly_wait(5)
    assert extract.get_extract().is_displayed()

def test_regular_delivery(driver):  # тест 49.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_delivery_menu().click()
    ozon_page.get_regular_delivery().click()
    regular_delivery = Regular_Delivery(driver)
    pytest.driver.implicitly_wait(5)
    assert regular_delivery.get_regular_delivery()[1].is_displayed()

def test_purchase_as_a_gift(driver):  # тест 50.Работает
    ozon_page = OzonPage(driver)
    ozon_page.visit_help()
    ozon_page.get_delivery_menu().click()
    ozon_page.get_purchase_as_a_gift().click()
    purchase_as_a_gift = Purchase_As_A_Gift(driver)
    pytest.driver.implicitly_wait(5)
    assert purchase_as_a_gift.get_purchase_as_a_gift()[1].is_displayed()



























