from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re

app = Flask(__name__)
CORS(app)

@app.route('/desbloquear', methods=['POST'])
def desbloquear():
    data = request.json
    rsocial = data.get('rsocial')
    cnpj_const = data.get('cnpj')
    telefone_const = "31988112233"
    serial_const = data.get('serial')
    senha_const = data.get('senha')

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-extensions')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-blink-features=AutomationControlled') 
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("user-agent=Mozilla/5.0 ...")

        driver = webdriver.Chrome(options=options)
        driver.get('https://www.controlid.com.br/desbloqueio/index.php')

        sleep(3)

        driver.find_element(By.ID, 'rsocial').send_keys(rsocial)
        driver.find_element(By.ID, 'cnpj').send_keys(cnpj_const)
        driver.find_element(By.ID, 'telefone').send_keys(telefone_const)
        driver.find_element(By.ID, 'serial').send_keys(serial_const)
        driver.find_element(By.ID, 'senha').send_keys(senha_const)
        driver.find_element(By.ID, 'termos').click()
        driver.find_element(By.ID, 'btnSubmit').click()
        sleep(3)

        texto_desbloqueio = driver.find_element(By.XPATH, '//*[@id="endModal"]/div/div/div[2]/span').text
        driver.quit()

        match = re.search(r'código de desbloqueio é:\s*\n*(\d+)', texto_desbloqueio, re.IGNORECASE)
        if match:
            codigo = match.group(1)
            return jsonify({'codigo': codigo})
        else:
            return jsonify({'erro': 'Código não encontrado.'}), 404

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
