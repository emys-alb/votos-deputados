import scrapy

anos = [i for i in range(2019, 2023)]
urls = [f"https://www.camara.leg.br/deputados/204554/votacoes-nominais-plenario/{ano}" for ano in anos]

class AbilioSantanaScraper(scrapy.Spider):
    name = "abilio-santana-scraper"
    start_urls = urls
    custom_settings = {
        "FEEDS": {
            'abilio-santana.csv': {
                'format': 'csv'
            }
        }
    }


    def parse(self, response):
        SEL_TABLE = "table"

        for table in response.css(SEL_TABLE):
            SEL_LINHA = "tbody > tr"
            for linha in table.css(SEL_LINHA):
                SEL_PAUTA = "a::text"
                SEL_URL = "a::attr(href)"
                SEL_VOTO = "td:nth-child(2)::text"

                yield {
                    'pauta': linha.css(SEL_PAUTA).extract_first(),
                    'url': linha.css(SEL_URL).extract_first(),
                    'voto': linha.css(SEL_VOTO).extract_first()
                }