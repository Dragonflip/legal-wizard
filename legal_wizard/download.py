from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def download_documento(numero_documento):
    URL = f"https://www.tjrs.jus.br/proc/alvara/alvara.php?identificador={numero_documento}&t=3"

    #necessario adicionar preferencias do firefox para permitir o download pelo selenium
    options = Options()
    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf"
    )
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.manager.useWindow", False)
    options.set_preference(
        "browser.download.dir", BASE_DIR
    )
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("pdfjs.disabled", True)
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    navegador = Firefox(options=options)
    navegador.get(URL)
    navegador.back()
