![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome phillrutherford,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!

# Fitness First

Fitness First is a website/application designed to help users reach their fitness goals without the hassle or costs of gym memberships. 
The site focus on using minimal equipment whilst keeping the workouts quick and effective. We also offer meal plans to further help users reach their goal.

## UX

Please head over to the UX folder to find my marvelapp mock ups and my User stories that I used in the planning process.

## Features

#### Feature 1 - Subscription
The Subscription feature is one set cost of $6.99 per week, this allows users full access to the site. This opens up more workouts and more meals to the customer.

#### Feature 2 - Free trial 
Without subscribing any user can log on and access 1 days worth of any programme for free. For E.G. 3 meals, a snack and a workout is accessible to anyone who opens the site. 
The reason for this is I wanted to give any user a taste of what might be coming should they choose to subscribe so they know if its for them or not.

#### Feature 3 - Variety
Offering a variety of programmes opens up the target audience to everyone. No matter the goal of the user this site offers something for them. I didnt want to make a site that
was specificallty for bodybuilding or any one thing particularly. As a business plan I think it is a positive move to target a wider audience.

### Features to implement

#### More detail
If i had more time to work on this project I would deepen the product detail. More workouts, more meals. For E.G. Offering a 6 week programme, 12 week programme all at different costs.
I would also offer a yearly subscription which the customer could pay weekly/monthly/yearly depending on their choice. 

#### Videos on the page 
The workout videos that are currently external links to youtube. I would like to have those embedded into the code so a user can view them without being redirect to another tab.

#### Store 
I would also like to add a store to the site. This would allow users to purchase all the equipment necessary for the workouts (pull-up bars, kettleballs, skipping ropes etc..).
In addition to that there would be some workout apparel available - tanktops, t-shirts, shorts, joggers, yoga pants, water bottles etc..


#### Images
I would also have preferred to have used some images for the meals. Maybe even video instructions on prepping and cooking. But an image of the final product would add a nice effect to 
the page. 

# Technologies Used

- The project uses Stripe to initalise payment methods.
- The project uses bootstrap for navbar and layout designs.
- The project uses google fonts to specify the font chosen.
- The project uses the django framework to simplify the building process.
- The project uses python to
- The project uses Javascript

# Testing

Throughout this project I encountered several bugs and issues. Firstly I struggled linking my templates to eachother through the navbar. This was a difficult problem as I couldnt understand why it wasn't 
working despite going through the course material, slack and tutor support all unsucessfully! Eventually I realised I was missing a folder. For example I had programmes/templates/build_muscle.html and that
wasnt working, what I had to do was make the path programmes/templates/programmes/build_muscle.html and then everything ran smoothly. 

Furthermore I am struggling to get the card element from stripe to show on my project. I have revisited the course material and checked over my views/urls/html/js code for it and still cannot see the issue. 
I found out the issue was the same as the one above, I had to create another folder called subscriptions within the static folder and then everything worked perfectly.