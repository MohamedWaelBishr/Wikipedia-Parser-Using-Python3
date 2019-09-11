import wikipedia

topic = input('Please Enter The Topic :  ')

TopicPage = wikipedia.page(topic)
print(TopicPage.content)
""" for cont in TopicPage.content :
    print(cont)
 """ 
 