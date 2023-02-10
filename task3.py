import time
from selenium import webdriver
import re


def html_pars(url: str = 'https://greenatom.ru/') -> str:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)
    generated_html = driver.page_source
    driver.quit()
    return generated_html


def print_result(string_for_re: str) -> None:
    save_pars = string_for_re
    pattern_all = re.compile(r'<[^<>]+>')
    pattern_not_atr = re.compile(r'<[^<>=]+>')
    p_a = pattern_all.findall(save_pars)
    print("All html tags:", len(p_a))
    print("Tags with an attribute:", len(p_a) - len(pattern_not_atr.findall(save_pars)))


if __name__ == "__main__":
    print_result(html_pars())
