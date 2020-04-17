
from requests_html import HTML,HTMLSession

def ScrapyStages(Country ='morocco'):

    session = HTMLSession()
    dataStatistics = []
    linkScrap = 'https://www.worldometers.info/coronavirus/country/'+ Country 
    r = session.get(linkScrap)
    CountryStatistics = r.html.find('.col-md-8 .content-inner .maincounter-number span')
    LastUpdateTime = r.html.find('.col-md-8 .content-inner > div:nth-child(4)')
    print(LastUpdateTime[0].text)
    print('Country : '+Country)
    
    
    CoronavirusCases  =  CountryStatistics[0].text
    print('Coronavirus Cases: '+CoronavirusCases)
    Deaths = CountryStatistics[1].text
    print('Deaths: '+Deaths)
   
    Recovered = CountryStatistics[2].text
    print('Recovered: '+Recovered)


ScrapyStages('morocco')