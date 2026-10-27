import requests
from bs4 import BeautifulSoup

def ingest_google_doc(url):
   # ingests the google doc and parses it.
    response = requests.get(url, timeout=60)
    
    character_coordinates = []
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        # tableDef = r"<table.*</table>"
        # tableStr = re.search(tableDef, soup.prettify(), re.DOTALL).group()
        table = soup.find("table")
        rows = table.find_all("tr")
        # note: first row is going to be the 'header' so just get rid of that
        if(len(rows) > 1): # If we have more than one row (i.e. empty header or just blank table).
            for x in range(1, len(rows)): # Start with the 2nd row (index 1)
                cols = rows[x].find_all('td')
                # Our structure is X, [ITEM], Y
                x_text = cols[0].find("p").text
                x_coord = -1
                if(x_text.isdigit()):
                    x_coord = int(x_text)
                y_text = cols[2].find("p").text
                y_coord = -1
                if(y_text.isdigit()):
                    y_coord = int(y_text)
                character = cols[1].find("p").text
                if(x_coord != -1 and y_coord != -1): # We can define -1 as 'no coordinate' because coordinates were specified as being minimum 1.
                    character_coordinates.append((x_coord, y_coord, character)) # tuple of elements.
    return character_coordinates # Empty if bad response.
def print_google_doc_shape(grid):
   # outputs the grid data returned by ingest_google_doc
   if(grid == []):
       return
   grid_sorted = sorted(grid, key = lambda x : x[0]) # sort by x
   maximum_x = grid_sorted[-1][0] # get the last X; this will be the biggest
   grid_sorted = sorted(grid_sorted, key = lambda x : x[1], reverse=True) # sort by y backwards
   maximum_y = grid_sorted[0][1] # get the first Y; this will be the biggest.

   for y in reversed(range(0, maximum_y+1)):
        for x in range(0, maximum_x + 1):
            if(grid_sorted == []):
                break
            if(grid_sorted[0][0] == x and grid_sorted[0][1] == y):
                point = grid_sorted.pop(0)
                print(point[2], end="")
            else:
                print(" ", end="")

        print("") # new line
        
       
example_url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
example_url_2 = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
grid_output = ingest_google_doc(example_url_2)
print_google_doc_shape(grid_output)