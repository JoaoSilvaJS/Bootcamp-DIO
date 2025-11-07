import time
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

caminhoArquivo = 'Pasta1.xlsx'
planilha = load_workbook(filename=caminhoArquivo)
sheet = planilha['Planilha1']

nav = webdriver.Chrome()
nav.maximize_window()

time.sleep(2)

nav.get('https://gfl.sinclog.com.br/')
nav.find_element(By.NAME,'login').send_keys('xx')

nav.find_element(By.NAME,'senha').send_keys('xxxxxxx')
nav.find_element(By.NAME,'senha').send_keys(Keys.RETURN)

sleep(4)

nav.get('https://gfl.sinclog.com.br/usuariosistema/listar')

sleep(3)

for coluna in range(2, len(sheet['A']) + 1):
    
    nome = sheet[f'A{coluna}'].value
    
    #Pesquisar
    nav.find_element(By.XPATH, '/html/body/div[2]/div/section[1]/div/a[1]').click()
    sleep(2)
    #Encontra o campo buscar e enviar nome do usuário do excel
    nav.find_element(By.XPATH, '//*[@id="valorBusca"]').send_keys(nome)
    nav.find_element(By.XPATH, '//*[@id="valorBusca"]').send_keys(Keys.RETURN)

    sleep(2)

    #Clica na engrenagem e em editar
    nav.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/div[3]/div/div/div[1]/div/div[1]/div/a/i').click()
    nav.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/div[3]/div/div/div[1]/div/div[1]/div/ul/li[1]/a').click()
    
    sleep(2)

    #Clica no perfil de acesso e altera o perfil para operacional
    nav.find_element(By.ID, 'select2-UsuarioSistema_idPerfilAcesso-container').click()

    sleep(1)


    nav.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys('Operacional', Keys.RETURN)
    sleep(2)
    #nav.find_element(By.XPATH, '//*[@id="tab-1"]/form/div[3]/div/p/button').click()

    print(nome, 'Perfil alterado..')
    
    sleep(3)

    nav.get('https://gfl.sinclog.com.br/usuariosistema/listar')

    sleep(3)

    print()

nav.quit()
print('Fim!:)')