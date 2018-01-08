<!--A "design document" for your project in the form of a file called DESIGN.md that discusses, technically, -->
<!--how you implemented your project and why you made the design decisions you did. Your design document should be at least -->
<!--several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your -->
<!--opportunity to give the staff a technical tour of your project underneath its hood.-->

In my directory project/ there are two folders, static and templates, and five other inclusions. Inside the Static folder is an images
folder which holds all the images my website uses. Also included in the Static folder are my CSS files. There is a CSS file named
circles.css which contains the styling for turning the images on the founders.html and info.html into circles to make those pages
look more pleasing. Then is featurette.css which is referenced in donate.html and mission.html. This css file was found on stack overflow:
https://stackoverflow.com/questions/22670731/are-the-featurette-classes-in-bootstrap-3-in-css-by-default-or-do-i-have-to-add
Style.css is the style page for index.html. It controls the style of the homepage's grid of images, the header, and the footer. It also
has the shades of brown colors needed for the large CACAO on the homepage. I found the css for the grid on W3Schools:
https://www.w3schools.com/css/css_grid_container.asp. I played around with their examples to find the exact way I wanted my homepage grid
of images to look (the size of the images, the placement, the padding). There is a href to styles.css in every html page except index.
Style.css is responsible for the navigation bar that is shown on every clickable page and for carousel in events.html.
I used styles.css from problem set 7, and added on additional styling needed for my pages.

In the templates folder are the my html files. I used some of layout.html from problem set 7 and had my files recipe.html,
emailregister.html, and apology.html extend layout.html. Recipe.html has a form to type in an ingredient and a button to submit. This
design is simple and crisp. I used jinja to go through each item in values (from application.py) to be displayed on my website: the
recipe title, url, and image. I felt that those are the only 3 keys that needed to be displayed on the page. Emailregister.html also uses
jinja and has a form to enter name, email, and confirmation email and a button to register. Apology.html uses jinja to print out the
appropriate apology message as well as gifs from the film Legally Blonde where Elle Woods is throwing chocolate at her TV screen. Her
frustration is channeled to the user in the apology message that comes from application.py. Confirmed.html has the navigation bar code in
the body and a success confirmation message to the user that they signed up for the club's email list paired with a chocolate gif.
Donate.html and mission.html both use featurettes. In both of their bodies, there is the code for the navigation bar, followed by a
div class main container (which holds the featurette in its proper place). The featurette in both pages has a heading, followed by
paragraphs and an image on the right. In donate.html I included Pencils of Promise's verbiage to capture the spirit of the charity.
I wanted both donate.html and mission.html to have a similar format to have a string of consistency in the website.
However, for the most part on rest of the pages, they look different to show off different features. Info.html, along
with the nav bar, has a container of three columns of circle images with text under them and links to resources with more information
on chocolate making and the history behind it. I have one row of three columns with paragraph tags in each column class.
Events.html links some bootstrap style for the nav bar and carousel. I chose to have paragraph text in the center at the top to
display upcoming events easily for user convenience. The carousel came from bootstrap 4:
https://v4-alpha.getbootstrap.com/components/carousel/. I decided to include slides with controls, indicators, and captions on my carousel.
Founders.html has a layout of three rows of two columns to show the members of the board. I used cards to have the person's name,
title, image, bio, and social media link all in one grid. I changed the outline color to white so the border is not clearly visible
for a neater appearance. I made the images circles to look more interesting and not clutter the page with overwhelming rectangles.
Index.html is the homepage. I chose not to include the nav bar and instead have a more graphic approach with clickable images.
Every additional page I made can be accessed from the homepage. The top left email sign up links to emailregister.html.
The bottom left footer allows the user to easily email directly to the board. I chose icons for the bottom right because they
are more user friendly as people would rather see images rather than bulky text. I set the images in the center in a class
called grid-container. I manipulated the grid to have the images be the size I wanted and the space between the images to
be uniform.

Along with DESIGN.md and README.md is application.py, helpers.py, and signup.db.

signup.db is a SQLite database with one table called "email". This table keeps track of the users that signed up for CACAO's email list.
The table stores a unique id, the user's name and yale email address. I used my knowledge of SQLite databases from problem set 7: finance.

helpers.py has two functions defined: lookup(ing) and apology(message, code=400). Lookup(ing) takes ing (which is an ingredient) as an
argument. Inside this definition is the API key for food2fork, which offers an API which exposes its ingredient search functionality
across its database of publishers.Food2Fork API: https://market.mashape.com/community/food2fork
I restricted the results to only results with the ingredient chocolate by setting the "q" in the url to chocolate.
The function sets the url to include the second ingredient as well as chocolate to narrow the results. The function returns
a dictionary of recipes with 8 keys: publisher, f2f_url (food2fork url), title, source_url, recipe_id, image_url, social_rank, and
publisher_url. The function Apology(message, code=400) renders the message as an apology to the user. I used the template of helpers.py
from problem set 7, but changed both functions for my website.

I used the template of application.py from problem set 7, but added more routes and adjusted the previous def register() to
emailregister() to fit the needs of my website. application.py begins with many imports, CS50’s SQL module and a few helper functions.
Then application.py configures flask, disables caching of responses, configures jinja, configures CS50’s SQL module to use signup.db.
Then there are numerous routes including index (to the homepage), events (Upcoming Events page), founders (the Team members page),
mission (the About page with the mission statement), donate, info, and confirmed. These routes support only GET as there is no user
input, however the routes for recipe and emailregister support both GET and POST. The routes that only support the request method
GET go directly to that page's html. def recipe(), if POST, sets ing to the second ingredient entered by the user and
checks to make sure a second ingredient was entered. If it is not entered, it returns the apology("Missing Ingredient!")
and a gif. Once it is entered, ing is set to values, and the function returns render_template to "recipe.html" with values
equaling values. If def recipe() is with the method GET, it returns the render_template recipe.html.
def emailregister() registers a users email for the email list. If it is GET, it returns render_template to emailregister.html.
If the request method is POST, the function gets the name, email, and confirmation email from the user. There are checks to make
sure the user entered a name, email, and confirmation email. Also a check that the email entered is a yale email and that the email
matches the confirmation email. This function uses db.execute (from CS50’s library) to query signup.db. Upon completion,
the user is redirected to /confirmed to tell the user that they successfully signed up.
