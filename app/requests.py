import urllib.request, json
from .models import Quote

def get_quote():
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)
        quote_object = None
        if quote_details_response:
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')
            quote_object = Quote(author, quote)
    return quote_object        


#Getting the base url
# base_url = None

# def configure_request(app):
#     global base_url #,api_key
#     base_url = app.config['QUOTES_API_BASE_URL']
#     #api_key = app.config['BLOG_API_KEY']

# def get_quote():
#     with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
#         quote_details_data = url.read()
#         quote_details_response = json.loads(quote_details_data)
#         quote_object = None
#         if quote_details_response:
#             author = quote_details_response.get('author')
#             quote = quote_details_response.get('quote')
#             quote_object = Quote(author, quote)
#     return quote_object        


# def process_results(quote_list):
#     '''
#     function that processes results of the quote and returns a list of quotes
#     '''
#     quote_results = []
#     for quote_item in quote_list:
#         id = quote_item.get('id')
#         quote = quote_item.get('quote')
#         author = quote_item.get('author')

#         quote_object = Quote(id,quote,author)
#         quote_results.append(quote_object)

#     return quote_results