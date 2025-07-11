# Waads Space Website.
#### Video Demo:  <[URL HERE](https://youtu.be/LYk_cLZn6Sg?si=JWjAKPWgaWUvaj8_)>
#### Description:
Waads Space project is a web application that provides information about space. The project includes several HYML pages that cover different topics related to space.

## Project Structurs

-
**templates/index.html**: The main page of the project. Here are some kry sections:
-**Head section**:
  - Sets the character encoding and viewport settings.
  - Includes external CSS and JavaScript libraries.
  - Links to the project's favicon and custom stylesheet.
-**Body Section**:
  - Contains a form for searching content.
  - Uses various loops to display data from different sources (e.g., Nasa data, mission data, books data, space data).
  - Includes conditional statements to handle specific cases (e.g., displaying different links based on `id`).
  - Displays additional content if available.
  -**Introduction Section**:
    - Contains a header and a main welcome message.
    - Introduces the website and its focus on space-related information.
  -**Space Section**:
    - Describes what space is with a definition and explanation.
  -**Planets Section**:
    - Provides information about the planets in our solar system.
    - Includes details about what defines a planet and the different types of planets (inner, outer, and dwarf planets).
    - Uses various CSS classes to style the content and images.
    - Contains links to more detailed pages about each planet.
  -**Inner Planets**:
    - Lists facts about Mercury, Venus, Earth, and Mars.
  -**Outer Planets**:
    - Lists facts about Jupiter, Saturn, Uranus, and Neptune.
  -**Dwarf Planets**:
    - Lists facts about Ceres, Pluto, Haumea, Makemake, and Eris.
  -**The Sun Section**:
    - Provides an overview of the Sun, its importance, and its influence on the solar system.
    - Includes information about the Heliophysics Big Year.
  -**Stars Section**:
    - Describes stars, their composition, and their life cycles.
    - Conatins a link to a detailed page about stars.
  -**Galaxies Section**:
    - EXplains what galaxies are, their composition, and their various types.
    - Provides information about the age and structure of galaxies.
    - Contains a link to a detailed page about galaxies.
  -**Black Holes Section**:
    - Discusses black holes, their properties, and what is known about them.
    - Contains a link to a detailed page about black holes.
  -**JavaScript Section**:
    - Contains a script to toggle the display of the "explore-content" section when the "explore-toggle" icon is clicked.
    - Includes a script that scrolls the page to specific sections based on the search query.
  -**Footer Section**:
    - Provides a note indicating that all information and images are sourced from NASA.
    - Includes a horizontal rule for separation and a footer message.

-
**templates/blackhole.html**: Provides detailed information about black holes, including:
- Different methods of detecting black holes.
- Misconceptions about black holes.
- Types of black holes:
Steller, Supermassive, Intermediate, and Primordial.
- Uses various CSS classes from`style.css` to style the content and images.

-
**templates/earth.html**: Provides detailed information about earth, including:
- The definition of the earth.
- Namesake, Potential for Life, Size and Distance, Orbit and Rotation.
- Moons, Formation, Structure, Atmosphere, Magnetosphere.
- 8 Different things that you  Need-to-Know About Our Home Planet:
Measuring Up, We're On It, Breathe Easy, Our Cosmic Companion, Ringless, Orbital Science, Home, Sweet Home, Protective Shield.
- Uses various CSS classes from`style.css` to style the content.

-
**templates/galaxies.html**: Provides detailed information about galaxies, including:
- It covers two things.
- The first one talks about Our Milky Way.
- The second one talks about the Types of Galaxies and information with photos about each one of them::
Spiral, Elliptical, Lenticular, Irregular, Seyfert, Quasars, Blazars, Active Galaxies.
- Uses various CSS classes from`style.css` to style the content and images.

-
**templates/planets.html**: Provides detailed information about planets, including:
- We have in our body the table, table row, table head, table data and takes all the information from sql space.db.
- Within the table:
- First table row there is indside it three table heads.
- Second table row within it one table data for the Inner Planets.
- Then there's i used Jinja for loop and i specified in it to get me the first 3 planets for inner planets.
- Third table row there's inside it three table heads with images.
- Endfor loop.
- Fourth table row within it one table data for the Outer Planets.
- Then there's i used Jinja for loop and i specified in it to get me the planets from the third to the seventh for Outer planets.
- Fifth table row there's inside it three table heads with images.
- Endfor loop.
- Sixth table row within it one table data for the Dwarf Planets.
- Then there's i used Jinja for loop and i specified in it to get me the planets from the seventh to the end for Outer planets.
- Seventh table row there's inside it three table heads with images.
- Endfor loop.
- Uses various CSS classes from`style.css` to style the content and images and additional style in the head:
-`imag`: Sets the width, height, object-fit for the images.
-`.inner-outer-planets`: Sets the background-color, font-family, size, weight text algin for the tr.
-`border`: For the table.

-
**templates/stars.html**: Provides detailed information about stars, including:
- First it give us an overview of stars:
The birth, life, death.
- Then Star Types and information with photos about each one of them:
Main Sequence, Red Giants, White Dwarfs, Neutron, Red Dwarfs, Brown Dwarfs.
- Uses various CSS classes from`style.css` to style the content and images and sets the background color to white.

-
-**static/style.css**: Contains the CSS styles for the web pages. Here are some key styles:
-`body`: Sets the background and text color.
-`.starbody`: Styles the background image for star-related pages.
-`.center`: Centers content using flexbox.
-`.small-image` and `.samll1-image`: Adjust the size of images.
-`.txtal` and `txtal1`: Apply text decoration and styling.
-`.header`: Styles the header with a background color and italic font.
-`.main`: Adds padding and text decoration to the main content.
-`.space`: Adds a text shadow effect.
-`.planet`,`.earth`: Set background images and text color for specific pages.
-Various classes like
-`.fontsize`, `.planettype`, `.sun`, etc, apply specific font sizes, padding, and styles to different elements.
-`h2`: Adds padding of 2rem for any title uses header 2.
-`.ls`: Sets the font size using large type.
-`.sp`, `.sp4`: sp Add padding to left of 2rem, sp4 Add padding to left of 4rem.
-`.sunov`, `.sunov1`, `.sunover`: Set the font size of 20px, italic font style, padding to left sunov 8rem, sunov1 12rem, sunover 4rem.
-`.section`: Add padding top, bottom, left, right.
-`.large`: Sets text decoration line, color, font size, text align.
-`.dodgerblue`: Sets font size, style, color,padding left.
-`.sp2`: Add padding left, font size to the text.
-`.s`: add padding, padding top.
-`header1`: Sets the font size, padding top, text align, text decoriation line, color, style.
-`.footer`: Sets the texts padding left, font size, text decoriation line, color.
-`.line`: Adds to the text decoriation line, color.
-`.note`: Sets the font color.
-`.planets`: Sets the background, padding, margin.
-`table`: Sets the width, height, border-collapse for the table.
-`th, td`: Sets border, padding, text align for them.
-`th`: Sets the background color, font color, size for the th.
-`td`: Sets the font size, color, style for td.
-`table, th, td`: Sets the border for the table, th and the td.

-
## Application Structure

-**app.py**: The main application file for the Flask web app. Here are some key sections:
  - **Imports**: Imports necessary libraries and modules, including Flask, SQLite, and CS50's SQL library.
  - **Database Setup**: Initializes the database connection using `SQL("sqlite:///space.db").
  - **Routes**:
  - `/search`: Handles search queries and redirects to specific pages based on the query.
  - `/`: The main route that fetches data from the database and renders the `index.html` template.
  - `/earth.html`, `/stars.html`, `galaxies.html`, `blackhole.html`: Routes that render specific templates for different topics.
  - `/planets.html`: Fetches planet data from the database and renders the `planets.html` template.
- `get_db_connection()`: Establishes and returns a connection to the SQLite database.

-
## Database Structure

- **solar_system**: This tabl contains information about various aspects of the solar system. Here are the columns:
  - **id**: An integer that uniquely identifies each entry.
  - **title**: A string that provides the title of the entry.
  - **description**: A string that describes the entry.
  - **url**: A string that contains a URL related to the entry.

### Example Entries
| id |          title          |                           description                           |                                                                        url                                                                        |
|----|-------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Our Solar System        | If you wanna see our solar system you can go to NASA from here. | {{URL}}                                                                                         |
| 2  | Our Solar System Photos | And here Our Solar System Photos.                               | {{URL}}                                                                                         |
| 3  | Solar System Book       | Book name (50 Years of Solar System Exploration).               | {{URL}} |

- **photos**: This table contains information about various photos related to space. Here are the columns:
  - **id**: An integer that uniquely identifies each entry.
  - **photo_name**: A string that provides the name of the photo.
  - **photo_link**: A string that contains a URL to the photo.

### Example Entries
| id |     photo_name     |                      photo_link                      |
|----|--------------------|------------------------------------------------------|
| 1  | Stars Photos       | {{URL}}                                              |
| 2  | Black Holes Photos | {{URL}}                                              |
| 3  | Galaxies Photos    | {{URL}}                                              |

- **books**: This table contains information about various books related to NASA. Here are the columns:
  - **id**: An integer that uniquely identifies each entry.
  - **title**: A string that provides the title of the books.
  - **description**: A string that describes the books.
  - **url**: A string that contains a URL to the books.

### Example Entries
| id |      title      |                    description                     |             url              |
|----|-----------------|----------------------------------------------------|------------------------------|
| 1  | e-Books of NASA | You can find different books of NASA in this link. | {{URL}}                      |

- **planets**: This table contains information about various planets and dwarf planets. Here are the columns:
  - **id**: An integer that uniquely identifies each entry.
  - **name**: A string that provides the name of the planets.
  - **info_url**: A string that contains a URL with more information about the planets.
  - **url**: A string that contains a URL to a photo of the planets.

### Example Entries
| id  |   name   |                      info_url                       |                      photo_url                      |
|-----|----------|-----------------------------------------------------|-----------------------------------------------------|
| 1   | Mercury  | {{URL}}                                             | {{URL}}                                             |
| 2   | Venus    | {{URL}}                                             | {{URL}}                                             |
| NULL| Mars     | {{URL}}                                             | {{URL}}                                             |
| NULL| Jupiter  | {{URL}}                                             | {{URL}}                                             |
| NULL| Saturn   | {{URL}}                                             | {{URL}}                                             |
| NULL| Uranus   | {{URL}}                                             | {{URL}}                                             |
| NULL| Neptune  | {{URL}}                                             | {{URL}}                                             |
| NULL| Ceres    | {{URL}}                                             | {{URL}}                                             |
| NULL| Pluto    | {{URL}}                                             | {{URL}}                                             |
| NULL| Haumea   | {{URL}}                                             | {{URL}}                                             |
| NULL| Makemake | {{URL}}                                             | {{URL}}                                             |
| NULL| Eris     | {{URL}}                                             | {{URL}}                                             |

- **missions**: This table contains information about various NASA missions. Here are the columns:
  - **id**: An integer that uniquely identifies each entry.
  - **mission_description**: A string that describes the mission.
  - **mission_link**: A string that contains a URL with more information about the mission.
  - **mission_name**: A string that provides the name of the mission.

### Example Entries
| id |               mission_description               |            mission_link             |   mission_name   |
|----|-------------------------------------------------|-------------------------------------|------------------|
| 1  | You can find all the missions of NASA here.     | {{URL}}                             | Missions of NASA |

- **nasa**: This table contains general information about NASA. Here are the columns:
  - **id**: An integer that uniquely identifies each entry.
  - **nasa_name**: A string that provides the name.
  - **nasa_description**: A string that describes the entry.
  - **nasa_link**: A string that contains a URL with more information.

### Example Entries
| id | nasa_name |                 nasa_description                 |       nasa_link       |
|----|-----------|--------------------------------------------------|-----------------------|
| 1  | NASA      | You can go here to see different things in NASA. | {{URL}}               |


