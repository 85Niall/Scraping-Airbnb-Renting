from requests_op import Scraping
from selenium_op import SeleniumOP

AIRBNB_OPERATIONS = {
	"region": "台中市",
	"checkin": "2023-06-20",
	"checkout": "2023-06-21",
	"adults": "1",
	"children": "0",
	"infants": "0",
	"pets": "0"
}
GOOGLEFROMS = "https://docs.google.com/forms/d/e/1FAIpQLSce2S_nIOthzZFfpQAUX7oyIE1yLxUcsLiSsVNWbSqs9kMdOw/viewform?usp=sf_link"

# Use Requests to scrape all the listings from the Airbnb web address
# Use Selenium to operate Airbnb next page.
page = f"https://www.airbnb.com.tw/s/{AIRBNB_OPERATIONS['region']}/homes?place_id=ChIJ7yJ5-d8XaTQRf0SmfuQ-Uoc&refinement_paths%5B%5D=%2Fhomes&checkin={AIRBNB_OPERATIONS['checkin']}&checkout={AIRBNB_OPERATIONS['checkout']}&date_picker_type=calendar&adults={AIRBNB_OPERATIONS['adults']}&children={AIRBNB_OPERATIONS['children']}&infants={AIRBNB_OPERATIONS['infants']}&pets={AIRBNB_OPERATIONS['pets']}&search_type=AUTOSUGGEST"
rq = Scraping(page)
print(rq.soup)
sl = SeleniumOP()
while sl.click_next_page(page):
	rq.add_scarp_link(page)
	rq.add_scarp_address(page)
	rq.add_scarp_price(page)
	sl.click_next_page(page)
	page = str(sl.driver.current_url)

# rq.address_name = ['1', '2', '3']
# rq.address_title = ['1', '2', '3']
# rq.prices = [1, 2, 3]
# rq.links = ['12345', '67890', '12345']
print(rq.address_name)
print(rq.address_title)
print(rq.prices)
print(rq.links)
print(len(rq.address_name), len(rq.address_title), len(rq.prices), len(rq.links))
for n in range(len(rq.prices)):
	sl.add_from(
		google_forms=GOOGLEFROMS,
		ad_name=rq.address_name[n],
		ad_title=rq.address_title[n],
		price=rq.prices[n],
		link=rq.links[n]
	)
sl.driver.quit()
