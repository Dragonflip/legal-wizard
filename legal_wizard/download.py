from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def download_documento(numero_documento):
    URL = f"https://www.tjrs.jus.br/proc/alvara/alvara.php?identificador={numero_documento}&t=3"

    options = Options()
    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf"
    )
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.manager.useWindow", False)
    options.set_preference(
        "browser.download.dir", "/home/joao/Development/legal-wizard"
    )
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("pdfjs.disabled", True)
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    navegador = Firefox(options=options)
    navegador.get(URL)
    navegador.back()
