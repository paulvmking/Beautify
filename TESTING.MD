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

