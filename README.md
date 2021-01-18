## Project Submission
Hello!

This was a pretty fun project to undertake! A lot of my past experience has been Java/Spring/Angular, so it was nice to 
break out of that box. 

I tracked features and progress using trello: https://trello.com/b/rYD174wl/untitled

I created an app for home page and article. My starting goal was to separate the UI to several apps, and then compose 
them together as needed. For example you could have a comment app, which could then reused. 


### Home Page
#### Views
* homepage_view - I added a feature to view all articles for a specific company. I think this feature would become more useful
  when there are more articles :) 
#### Service
* contentService - Mock api call, when you load the page it loads the data from content JSON, and determines the slug-10
  article. This also saves the articles to the database, and picks 3 random articles.
  
### Articles 
#### Models
* Article 
* Tag 
* Instrument
* Comment

I decided to make models for instruments, comments, and tags, because I thought it would make it easier to filter and decouple if needed
in the future. The article page uses the related instruments to populate the ticker box on the right. The randomize button will
reorder the stocks listed there in a random order. The comment section allows anyone to post a comment. 

#### Views
* article_full_view - Shows you an article with related instruments. I make a "Service call" to get quotes data
* article_list_View - Shows you a list of articles with an Instrument ID. This view can be repeated for other attributes like tag

#### Service
* quoteService - Mock api call. It loads all data from the JSON into a dict and then allows for look ups by 
instrument id

### Files
* static: css, fonts, js files
* staticfiles: content_api, quotes_api
* templates: article, article_list, base, comment_form, home

