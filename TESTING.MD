# Testing 

## Navbar Functionality 

- **Aim** - When the **Beautify** icon on the left of navbar is clicked it redirects user to homepage.
- **Result** - This was done and user is redirected therefore passing the test.
- **Aim** - When links to other pages are clicked, the user is redirected to the mentioned page.
- **Result** - Navbar link clicked and redirected to corresponding page therefore passing the test.
- **Aim** - When screen size is reduced the **hamburger** icon displays and when clicked redirects user to corresponding page.
- **Result** - Screen size reduced activates **hamburger** icon and when clicked it reveals the page navigation which when clicked redirects user to corresponding page 
therefore passing the test.
- **Aim** - To see whether nagivation bar stays on the top of the screen on both all screen sizes.
- **Result** - Screen size was reduced and navigation bar sticks to top of page on all sizes therefore passing the test.
- **Aim** - When the user is not logged in only the recipes, log in and register links show on navbar.
- **Result** - Visited site as a new user and only mentioned links appear therefore passing the test.
- **Aim** - When the user is not logged in only the register and login are located when my account is clicked.
- **Result** - Visited site as a logged in user and only mentioned links appear therefore passing the test.
- **Aim** - When the user is logged in the my profile and logout are located when my account is clicked.
- **Result** - Visited site as a logged in user and only mentioned links appear therefore passing the test.

### Buttons 

- **Aim** - When **form fields** within both the log in and register forms are not filled correctly they do not submit.
- **Result** - When all fields are filled out the Log in and register buttons work when clicked but when even one isnt the required information prompt displays therefore passing the test.
- **Aim** - When buttons around the site are clicked they execute their intended function be it redirect or adding to basket.
- **Result** - When buttons are clicked they redirect or in the case of the add to basket or checkout buttons they perform their intended functions therefore passing the test.

### Filters

- **Aim** - When the filters above the products are selected each filter displays the products in the corresponding format with correct information displayed.
- **Result** - When all filters were individually selected they re-ordered or displayed the corresponding results therefore passing the test.

## JavaScript Validator

- **[JSHint](https://jshint.com/)** - To Validate JavaScript and Jquery(Please copy and paste selected file into JSHint to reproduce results).

- **stripe_elements.js** File = **Passed**- No errors found. One undefined variable $ (Warnings are ES6 related)
- **countryfield.js** File = **Passed**- No errors found. One undefined variable $ (Warnings are ES6 related)
- **btn-increment.js** File = **Passed**- No errors found. One undefined variable $ (Warnings are ES6 related)
- **script.js** File = **Passed**- No errors found. One undefined variable $ (Warnings are ES6 related)
- **toasts.js** File = **Passed**- No errors found. One undefined variable $ (Warnings are ES6 related)

## Python PEP8 Validator

- **[PEP8online](http://pep8online.com/)** - To Validate Python code and ensure it is PEP8 complient(Please copy and paste selected file into PEP8online to reproduce results).

## Bag App
- **contexts.py** File = **Passed**- No errors found.
- **urls.py** File = **Passed**- No errors found.
- **views.py** File = **Passed**- No errors found with the exception of the first line where importing some django resources this did not effect the live site at all.
The other errors in this app were due to files that were created by django when creating the new app.

## Beautify App
- **settings.py** File = **Passed**- No errors found with the exception of the password validators lines  being too long, this did not effect the live site at all.
- **urls.py** File = **Passed**- No errors found.
The other errors in this app were due to files that were created by django when creating the new app.

## Checkout App
- **admin.py** File = **Passed**- No errors found.
- **apps.py** File = **Passed**- No errors found.
- **forms.py** File = **Passed**- No errors found.
- **models.py** File = **Passed**- No errors found with the exception of the lines 42 and 54 being too long, this did not effect the live site at all.
- **signals.py** File = **Passed**- No errors found.
- **urls.py** File = **Passed**- No errors found.
- **views.py** File = **Passed**- No errors found with the exception of lines 1, 80, 88, 99 which were all too long, this did not effect the live site at all.
- **webhook_handler.py** File = **Passed**- No errors found with the exception of lines 38, 67, 68, 98, 135 and 141 which were all too long, this did not effect the live site at all.
- **webhooks.py** File = **Passed**- No errors found with the exception of line 41 which was too long, this did not effect the live site at all.
The other errors in this app were due to files that were created by django when creating the new app.

## Home App
- **apps.py** File = **Passed**- No errors found.
- **urls.py** File = **Passed**- No errors found.
- **views.py** File = **Passed**- No errors found.
The other errors in this app were due to files that were created by django when creating the new app.

## Products App
- **admin.py** File = **Passed**- No errors found.
- **apps.py** File = **Passed**- No errors found.
- **models.py** File = **Passed**- No errors found with the exception of line 25 being too long, this did not effect the live site at all.
- **urls.py** File = **Passed**- No errors found.
- **views.py** File = **Passed**- No errors found with the exception of lines 41 and 44 which were all too long, this did not effect the live site at all.
The other errors in this app were due to files that were created by django when creating the new app.

## Profiles App
- **apps.py** File = **Passed**- No errors found.
- **forms.py** File = **Passed**- No errors found.
- **models.py** File = **Passed**- No errors found with the exception of the lines 14, 15, 16, 17 and 20 being too long, this did not effect the live site at all.
- **urls.py** File = **Passed**- No errors found with the exception of line 6 being too long, this did not effect the live site at all.
- **views.py** File = **Passed**- No errors found.
The other errors in this app were due to files that were created by django when creating the new app.

## Other
- **custom_storages.py** File = **Passed**- No errors found.


## CSS3 Validator 

- **[jigsawW3C](https://jigsaw.w3.org/css-validator/#validate_by_input)** - To Validate CSS.

- **checkout.css** File = **Passed**- No errors found.
- **profile.css** File = **Passed**- No errors found.
- **base.css** File = **Passed**- No errors found.

    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>

## HTML5 Validator

- **[validatorW3C](https://validator.w3.org/#validate_by_input)** - To Validate HTML5.

- **shopping_bag.html** File = **Passed**- No errors found except for loops syntax.
- **checkout_success.html** File = **Passed**- No errors found except for loops syntax.
- **checkout.html** File = **Passed**- No errors found except for loops syntax and heading for spinner.
- **index.html** File = **Passed**- No errors found except for loops syntax.
- **product_single.html** File = **Passed**- No errors found except for loops syntax.
- **products.html** File = **Passed**- No errors found except for loops syntax.
- **profile.html** File = **Passed**- No errors found except for loops syntax.
- **base.html** **Allauth** File = **Passed**- No errors found except for loops syntax.
- **base.html** File = **Passed**- No errors found except for loops syntax.

 ### Includes

- **main-nav.html** File = **Passed**- No errors found except for loops syntax and the fact it is an includes file.
- **mobile-top-header.html** File = **Passed**- No errors found except for loops syntax and the fact it is an includes file.

## Compatibility

| Screen              | Google Chrome    | Safari           | Microsoft Edge   | Opera            | Mozilla Firefox  | Internet Explorer |
| --------------------|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:-----------------:|
| Mobile              |     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:| N/A               |
| Tablet              |     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:| N/A               |
| Desktop             |     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:|     Passed:heavy_check_mark:| N/A               |

- The devices used for iOS testing were Macbook Pro, iPad mini, iPhone 10 and iPhone 8.
- The devices used for android testing were Huawei P30, Samsung A40, Samsung S20 aswell as Samsung Galaxy tab A7.
- For Windows 10 testing a HP pavillion was used as well as a HP Chromebook.
- Chrome Dev Tools was used for the other testing and every phone/tablet type and screen size was checked form the smallest available (320px),
to the largest (1200px +)

## User Stories Testing

 1. As a new user I want to know the sites purpose immediately.
 - User is greeted by an image of a makeup product showing the site intent straight away.
 2. As a new user I want an intuitive search experience.
 - User can use filters and a search bar to search for any terms in the products description or use the filters to narrow down the criteria they wish to search by.
 3. As a new user I expect to be able to navigate the site easily to find a product.
 - The site has a navbar on all sizes and has clearly labelled actions for each button or product provided.
 4. As a new user I expect to be able to sign up to services.
 - Users can register on the right hand side of navbar.
 5. As a potential customer I want an easy sign up process.
 - Users can register on the right hand side of navbar.
 6. As a potential customer I want easily explained details for the products.
 - Clicking each product brings up and individual page describing the product with more information.
 7. As a potential customer I want to have a good choice of filters for searching.
 - User can use filters and a search bar to search for any terms in the products description or use the filters to narrow down the criteria they wish to search by.
 8. As a returning user I want information and other useful content to entice me to return.
  - Clicking each product brings up and individual page describing the product with more information.
 9. As a returning user I want to be able to view my order history.
 - Creating a profile and signing in shows the user their order history if any.
 10. As a user I expect to be able to login and out of my own profile.
 - This is possible from the my account link on the top right of navbar.
 11. As a site admin I expect to be able to maintain the site.
 - As the admin you can sign in and manage the site from removing or adding products to creating new emails and viewing orders made.


## Usability  

- I shared the website with friends and family and received feedback from them stating the site was easy to use,
all features implemented fuctioned as expected.
They also mentioned that its simplicity lead to easy usage and navigation and the text and color choices made everything very user friendly.

## Issues and Fixes during Development

1. Changed json data models and changed data was not reflected in the live site.
- Fix = Had to use the "loaddata" command to ensure the live site was using the most recent data.
2. Issues with styling caused by default bootstrap classes for cards.
- Fix = Created my own classes to style each elemnt myself so if changes occur on bootstraps default classes mine will remain unaffected.
3. Using VH in css caused my cards to overlap and be strangely positioned.
- Fix = Used pixels for height and width to give a solid size.
4. Issues using API from makeup site.
- Fix = Solution was to use the data in json format in a fixture setup and edit the files to only contain information that was needed.

## Known Bugs

There are no known bugs to the best of my knowledge.