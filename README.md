![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# StarTrax Django Project

## Introduction

## Agile Development
To manage this project efficiently, I utilized GitHub's Project Board to implement agile development practices, allowing me to organize user stories into acceptence criteria and track progress.

### Must Haves
My must have criteria are outlined below. A user must be able to login, register and logout. They must be able to create, update, delete and read the reviews on their account. They must also be able to add and delete the albums that the reviews are associated with.

![screenshot of all must have criteria](images/user-stories.jpg)
#### Star Rating
![sceenshot of star rating stories](images/user-story-1.jpg)

#### Add Notes
![screenshot of adding notes user story](images/user-story-2.jpg)

#### User Account
![sceenshot of account functionality](images/user-story-3.jpg)

#### Add Library
![screenshot of library user story](images/user-story-4.jpg)

### Should Haves
![screenshot of should have stories](images/user-stories-shouldhave.jpg)

#### Album Covers
AS A music collector

I WANT to be able to see the album artwork of my library

SO THAT I can have a sense of a music library

-- ACCEPTANCE CRITERIA --

User can upload album artwork and tie it to albums

User can see album artwork in libraray

#### Clean Design
AS A Music Enthusiast

I WANT the website design to be calming and minimal

SO THAT it creates a calming atmosphere and I can thoughtfully enter my notes and ratings

-- ACCEPTENCE CRITERIA --

Calming choice of fonts

Elements on page kept to minimum

Modal to create album reviews is minimally styled (like calmly writer)

#### Add Album Review
AS A music lover

I WANT a space to insert a written comment on an album

SO THAT I can record my thoughts on an album

-- ACCEPTENCE CRITERIA --

User can create written comments for albums in their library

User can delete existing comments

User can edit existing comments

### Could Haves
![screenshot of could have user stories](images/user-stories-couldhave.jpg)

#### See Friends Reviews
AS A Music Lover

I WANT TO be able to see my friend's ratings

SO THAT I can compare my thoughts with theirs

-- ACCEPTENCE CRITERIA --

Ability to see ratings of friends on Spotify

#### Connect to Spotify
AS A Spotify User

I WANT TO be able to connect my Spotify account

SO THAT I can add ratings and reviews to my existing music library

-- ACCEPTENCE CRITERIA --

Connect to Spotify API

Import user library

Add data to user library from Spotify user library

## Wireframes

### Homepage
![wireframe of homepage](images/homepage_copy.png)

### Create an account
![wireframe of registration page](images/create_an_account.png)

### New Album Input
![wireframe of new album page](images/new_album.png)

### New Review Input
![wireframe of new review page](images/new_review.png)

## Entity Relationship Diagram
See below for ERD. Albums are tied to reviews, which are tied to users. I chose to use Django's inbuilt user system for this project
![entity relationship diagram](images/erd.png)

## Testing
Using GitHub Copilot I generate automated tests for the website's main features. These tests were implemented using the pytest framework.

The tests were as follows:
- a user can create a review
- a review can be updated
- a review can be deleted
- an album can be created
- an album can be deleted
- homepage welcomes client
- navigation links work correctly

![screenshot of test results](images/pytest.jpg)

## Deployment
Using manual deployment from a GitHub branch, I deployed using Heroku.

See deployed URL below;
https://startrax-draft-5e0a1c66b441.herokuapp.com/

![heroku screenshot](images/heroku.jpg)

# Reflection on use of AI in the project
Throughout the development of this project, AI played a crucial role in debugging and adding new features, especially in areas where I was unfamiliar with the necessary code. The AI significantly reduced the time I spent debugging by providing immediate solutions, which allowed me to focus more on the overall development process.

## Where the AI was useful
The AI was most useful in the debugging part of development. Django offered detailed traceback solutions - and copy and pasting them into Copilot was able to resolve these issues quickly and painlessly. 

It was also useful when dealing with features I hadn't encountered before in the LMS. For example the notification that comes with changes to data. I did not know how to implement messages this, but by using a multi-step reverse prompt I was able to specificy my requirements and the feature worked in the first instance. Being able to include these messages improved the User Experience.

## AI in testing
This was an example of where AI helped me to implement something I would not have otherwise been able to accomplish. Using a multi-step prompt, I asked Copilot to create me automated tests for all of the features existing in my project. The tests ran without issue. To learn, implement and debug the testing process myself would have taken days, but with Copilot assistance it was completed in about 25 minutes.

## Issues
While the AI's code suggestions were often helpful, there were instances where its solutions were overly complex. This highlighted the importance of understanding the code myself. Not blindly following code I didn't understand and then being stuck when it breaks.

One example of this was when I was creating the User Accounts section. Initially, the AI suggested using a 3rd party dependency, which I didn't fully understand. I was then able to specify that Django's built in account system to be used, creating a much simpler solution.



I saw the AI as a co-developer, contributing valuable insights and code snippets, but I maintained control over the decision-making process. Overall, the collaboration with AI resulted in a much faster development cycle, helping me achieve milestones more efficiently.

