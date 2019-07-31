from bs4 import BeautifulSoup



def read_file():
    file = open('24.three-sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')



# tag.contents         -- returns a list of children

body = soup.body


for child in body.contents:
    #print(child if child is not None else '',end='\n\n\n\n')
    pass





# .children         -- returns an iterator


for child in body.children:
    print(child if child is not None else '', end='\n\n\n\n')
