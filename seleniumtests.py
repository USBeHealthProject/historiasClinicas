# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Seleniumtests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_seleniumtests(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("rr")
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("rr")
        time.sleep(1)
        driver.find_element_by_css_selector("input.btn.btn-default").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"Historias Clínicas").click()
        time.sleep(1)
        driver.find_element_by_link_text("Nueva Historia").click()
        time.sleep(1)
        Select(driver.find_element_by_id("id_paciente")).select_by_visible_text("11122 p p")
        driver.find_element_by_id("id_antecedentes_personales").clear()
        driver.find_element_by_id("id_antecedentes_personales").send_keys("antecedentes")
        time.sleep(1)
        driver.find_element_by_id("id_antecedentes_familiares").clear()
        driver.find_element_by_id("id_antecedentes_familiares").send_keys("familiares")
        time.sleep(1)
        driver.find_element_by_id("id_motivo_consulta").clear()
        driver.find_element_by_id("id_motivo_consulta").send_keys("motivo")
        time.sleep(1)
        driver.find_element_by_id("id_enfermedad_actual").clear()
        driver.find_element_by_id("id_enfermedad_actual").send_keys("enfermedad")
        time.sleep(1)
        driver.find_element_by_id("id_peso").clear()
        driver.find_element_by_id("id_peso").send_keys("15")
        time.sleep(1)
        driver.find_element_by_id("id_talla").clear()
        driver.find_element_by_id("id_talla").send_keys("10")
        time.sleep(1)
        driver.find_element_by_id("id_signos_vitales").clear()
        driver.find_element_by_id("id_signos_vitales").send_keys("si")
        time.sleep(1)
        driver.find_element_by_id("id_piel").clear()
        driver.find_element_by_id("id_piel").send_keys("blanca")
        time.sleep(1)
        driver.find_element_by_id("id_ojos").clear()
        driver.find_element_by_id("id_ojos").send_keys("x")
        time.sleep(1)
        driver.find_element_by_id("id_fosas_nasales").clear()
        driver.find_element_by_id("id_fosas_nasales").send_keys("bien")
        time.sleep(1)
        driver.find_element_by_id("id_conductos_auditivos").clear()
        driver.find_element_by_id("id_conductos_auditivos").send_keys("bien")
        time.sleep(1)
        driver.find_element_by_id("id_cavidad_oral").clear()
        driver.find_element_by_id("id_cavidad_oral").send_keys("cavidad")
        time.sleep(1)
        driver.find_element_by_id("id_cuello").clear()
        driver.find_element_by_id("id_cuello").send_keys("cuello")
        time.sleep(1)
        driver.find_element_by_id("id_columna").clear()
        driver.find_element_by_id("id_columna").send_keys("columna")
        time.sleep(1)
        driver.find_element_by_id("id_torax").clear()
        driver.find_element_by_id("id_torax").send_keys("torax")
        time.sleep(1)
        driver.find_element_by_id("id_abdomen").clear()
        driver.find_element_by_id("id_abdomen").send_keys("abdomen")
        time.sleep(1)
        driver.find_element_by_id("id_extremidades").clear()
        driver.find_element_by_id("id_extremidades").send_keys("bien")
        time.sleep(1)
        driver.find_element_by_id("id_genitales").clear()
        driver.find_element_by_id("id_genitales").send_keys("bien")
        time.sleep(1)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        time.sleep(1)
        driver.find_element_by_link_text("x").click()
        time.sleep(1)
        driver.find_element_by_link_text("Ver Perfil").click()
        time.sleep(1)
        Select(driver.find_element_by_name("sex")).select_by_visible_text("Masculino")
        time.sleep(1)
        Select(driver.find_element_by_name("marital_status")).select_by_visible_text("Soltero")
        time.sleep(1)
        driver.find_element_by_id("id_phone").clear()
        driver.find_element_by_id("id_phone").send_keys("0212")
        time.sleep(1)
        driver.find_element_by_id("id_address").clear()
        driver.find_element_by_id("id_address").send_keys("direccion")
        time.sleep(1)
        driver.find_element_by_id("id_submit").click()
        time.sleep(7)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
