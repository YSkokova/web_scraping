import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# make an http request
def main():
    url = "https://news.ycombinator.com/item?id=42017580"
    response = requests.get(url)
    # parse the http response with "beautifulsoup"
    soup =  BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    # extract individual comments
    comments = [e.find_next(class_="comment") for e in elements
                ]
    # scrapped content for useful data
    keywords ={"python":0,
                "java":0, 
                "javascript":0, 
                "sql":0, 
                "c++":0, 
                "c":0, 
                "ruby":0}

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(" ")
        # clean up response text, also we can use map()
        words = {w.strip(".,/:;!@|") for w in words}

        for k in keywords:
            if k in words:
                keywords[k] += 1

    print(keywords)
    # visualizing the data with "matplotlib"
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.show()
    #print(f"Comments:{len(comments)}")
    
# print(f"Scraping: {url}")
# print(response)
# print(response.content)

if __name__ == "__main__":
    main()