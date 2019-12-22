import requests
from bs4 import BeautifulSoup


def main():
    #  lets scrape the questions page of stackoverflow to check for most recent questions.
    #  first we need to send a GET request to stackoverflow
    response = requests.get("https://stackoverflow.com/questions")
    #  then we create a BeautifulSoup object capable of parsing HTML
    soup = BeautifulSoup(response.text, "html.parser")
    #  then, we use a css selector to select all DOM elements with class="question-summary"
    #  what is returned here is actually a list of Tag objects, each of these are searchable with
    #  more css selectors for easy traversal
    question_obj_list = []
    questions = soup.select(".question-summary")
    for q in questions:
        #  for each question, we want to select its title. After inspecting one of the questions on the page
        #  we notice that the question titles contain the class "question-hyperlink"
        #  using the .select method on the Tag objects in the questions list we can select all attributes
        #  of that Tag, but since we only want to get the one attribute, we use select_one.
        #  what is obtained here is actually another Tag object, we use the .getText() method to obtain the
        #  raw text within the HTML tags of this element
        title_element = q.select_one(".question-hyperlink")
        title = title_element.getText()
        print(f'title="{title}"')
        #  the vote count is contained within the element with the class "vote-count-post" in this question object
        #  we can obtain this value in a similar way
        votes = q.select_one(".vote-count-post").getText().strip()
        print(f'votes={votes}')
        #  finally, lets extract the total views
        views = q.select_one(".views").getText().strip()
        print(f'views={views}')
        #  as a bonus, lets find all the tags
        tag_elements = q.select(".post-tag")
        tags = [te.getText().strip() for te in tag_elements]
        print(f'tags={tags}')
        print()


main()

if __name__ == '__main__':
    main()


