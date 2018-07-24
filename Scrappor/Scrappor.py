"""
Module to store functions to scrap data.
"""
import requests
from bs4 import BeautifulSoup

PREFIX_URL = 'https://www.leboncoin.fr/{}/offres/ile_de_france/occasions/?o='
SUFFIX_URL = '&ret=4'


def get_data_from_url(prefix_url, suffix_url):
    """
    Function to get data from url on Le Bon Coin website.
    Warnings
    ----------
    Sensible code, linked to Le Bon Coin website structure.
    Parameters
    ----------
    prefix_url: str, required
        Beginning of the url to be scrapped, linked to announce type.
    suffix_url: str, required
        End of the url to be scrapped, after page number
    Returns
    -------
    announces_list: list of dictionaries
         Structured data from website
         - TBC
    """
    page_num = 1
    over = False
    announces_list = []

    while True:
        url = prefix_url + str(page_num) + suffix_url
        try:
            r = requests.get(url)
        except Exception:
            print('Error: ', Exception, ' with ', url, '.')
            return ''

        soup = BeautifulSoup(r.text, "html.parser")

        date_to_scrap = datetime.date.today() - datetime.timedelta(+1)

        # ----- getting values -----
        for content in soup.find_all('li', itemscope="", itemtype="http://schema.org/Offer"):
            announce_dict = {}
            # if not today, no scrap
            announce_date = content.find('p', class_="item_supp", itemprop="availabilityStarts").get('content')

            if datetime.datetime.strptime(announce_date, '%Y-%m-%d').date() == date_to_scrap:
                # PRICE, Mandatory
                try:
                    price = int(content.find('h3', class_="item_price", itemprop="price").get('content'))
                except:
                    continue
                # Title
                title = content.find('h2', class_="item_title", itemprop="name").text.strip()
                # Location
                location = content.find('p', class_="item_supp", itemprop="availableAtOrFrom",
                                        itemtype="http://schema.org/Place").text.strip()
                city = location.split("/")[0].strip()
                try:
                    department = location.split("/")[1].strip()
                except:
                    department = ""
                # Date
                date = content.find('p', class_="item_supp", itemprop="availabilityStarts").get('content')
                # Url for description
                url_description = 'https:' + content.find('a').get('href')

                announce_dict["price"] = price
                announce_dict["title"] = title
                announce_dict["city"] = city
                announce_dict["department"] = department
                announce_dict["date"] = date
                announce_dict["url_description"] = url_description
                announce_dict["description"] = get_description_from_url(url_description)

                announces_list.append(announce_dict)

            elif datetime.datetime.strptime(announce_date, '%Y-%m-%d').date() == date_to_scrap - datetime.timedelta(+1):
                over = True
                break
            else:
                pass

        page_num += 1

        # To quit infinite while
        if over:
            break

    return announces_list



if __name__ == "__main__":
    pass