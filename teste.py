from selenium import webdriver

# Caso de teste informando os valores corretos para login e cadastro

navegador = webdriver.Chrome()
# Passo 1: Entrar em http://127.0.0.1:8000/:
navegador.get("http://127.0.0.1:8000/")
# Passo 2: Clicar em criar conta:
navegador.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]').click()
# Passo 3: Preencher as informações do usuário:
navegador.find_element_by_xpath('//*[@id="id_username"]').send_keys("Marcos")
navegador.find_element_by_xpath('//*[@id="id_email"]').send_keys("marcosilva@gmail.com")
navegador.find_element_by_xpath('//*[@id="id_password"]').send_keys("#Projeto2021")
#Passo 4: Clicar em cadastrar:
navegador.find_element_by_id('cadastrar-usuario').click()
#Passo 5: Clicar em Login:
navegador.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[2]').click()
# Passo 6: Preencher as informações de login:
navegador.find_element_by_id("email").send_keys("marcosilva@gmail.com")
navegador.find_element_by_id("senha").send_keys("#Projeto2021")
# Passo 7: Clicar em entrar:
navegador.find_element_by_id('Entrar').click()

