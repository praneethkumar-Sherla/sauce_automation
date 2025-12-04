import allure


@allure.title("Sauce Demo Checkout Flow")
def test_checkout_success(page, reporter, login_page, inventory_page, cart_page, checkout_page):
    try:
        with allure.step("Step 1: Login"):            
            login_page.login()
            locator = page.locator("text=Products").first
            locator.wait_for(state="visible", timeout=5000)
            assert locator.is_visible(), "Login failed: Inventory list not visible."
            reporter.attach_screenshot("Step_1_Login")

        with allure.step("Step 2: Select Random Items"):
            items = inventory_page.get_random_items()
            selected = inventory_page.add_items_to_cart(items)
            inventory_page.go_to_cart()
            locator = page.locator("text=Your Cart").first
            locator.wait_for(state="visible", timeout=5000)
            assert locator.is_visible(), "Items not added to cart."
            reporter.attach_screenshot("Step_2_Items_Added")

        with allure.step("Step 3: Cart Verification"):            
            cart_page.verify_items_present(selected)
            cart_page.checkout()
            locator = page.locator("text=Checkout: Your Information").first
            locator.wait_for(state="visible", timeout=5000)
            assert locator.is_visible(), "Checkout info page not visible."
            reporter.attach_screenshot("Step_3_Cart_Validated")

        with allure.step("Step 4: Checkout"):            
            checkout_page.fill_information()
            locator = page.locator("text=Checkout: Overview").first
            locator.wait_for(state="visible", timeout=5000)
            assert locator.is_visible(), "Checkout overview page not visible."
            reporter.attach_screenshot("Step_4_Info_Filled")

        with allure.step("Step 5: Complete Order"):
            checkout_page.finish_checkout()
            checkout_page.assert_checkout_complete()            
            reporter.attach_screenshot("Step_5_Order_Completed")

    except Exception as e:
        reporter.attach_screenshot("Failure")
        raise e
