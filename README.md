<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->

<h3 align="center">Web Scrapping Builders Data</h3>

  <p align="center">
    This repository contains a Python script that can be used to scrape data of real-estate builders and their projects from the websites '99acres.com' and 'magicbricks.com' respectively. The script uses the beautifulsoup library and selenium to parse the HTML code of the websites and extract the desired data.
    <br />
    <a href="https://github.com/sagarparmar881/web-scrapping-builders-data"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/sagarparmar881/web-scrapping-builders-data">View Demo</a>
    ·
    <a href="https://github.com/sagarparmar881/web-scrapping-builders-data/issues">Report Bug</a>
    ·
    <a href="https://github.com/sagarparmar881/web-scrapping-builders-data/issues">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
        <ul>
        <li><a href="#disclaimer">Disclaimer</a></li>
        <li><a href="#results">Results</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This repository contains a Python script that can be used to scrape data of real-estate builders and their projects from the websites '99acres.com' and 'magicbricks.com' respectively. The script uses the beautifulsoup library and selenium to parse the HTML code of the websites and extract the desired data.

###### **Disclaimer**

This project is for educational purposes only. The data that is scraped from the websites `99acres.com` and `magicbricks.com` is not intended to be used for commercial purposes. The websites `99acres.com` and `magicbricks.com` are not affiliated with this project in any way.

The developer(s) of this project make no guarantees about the accuracy or completeness of the data that is scraped. The data may be changed or removed at any time by the websites `99acres.com` and `magicbricks.com`.

###### **Results**

The results of the data scrapped from the websites `99acres.com` and `magicbricks.com` are saved in the CSV file format. The sample screenshots are attached below.

- ##### CSV Output - [99acers.com]

| FIELD1 | builder_name        | projects_total | projects_completed |
| ------ | ------------------- | -------------- | ------------------ |
| 0      | Darshanam Group     | 50             | 34                 |
| 1      | Nyalkaran Group     | 30             | 13                 |
| 2      | Kanha Group         | 23             | 14                 |
| 3      | Nilamber Group      | 21             | 15                 |
| 4      | Narayan Realty      | 20             | 16                 |
| 5      | Ananta Group        | 18             | 14                 |
| 6      | Earth Group Gujarat | 18             | 17                 |
| 7      | Pawan Group         | 19             | 16                 |
| 8      | Raama Group         | 18             | 12                 |
| 9      | Samanvay Realty     | 20             | 14                 |
| 10     | Taksh Group         | 15             | 13                 |

[![99acers][99acers-screenshot]]()

- ##### CSV Output - [magicbricks.com]

| FIELD1 | name                                   | projects_total          | projects_completed |
| ------ | -------------------------------------- | ----------------------- | ------------------ |
| 0      | Pacifica Companies                     | 8 Projects in Vadodara  | 6 Completed        |
| 1      | Akshar Group                           | 14 Projects in Vadodara | 9 Completed        |
| 2      | Sangani Infrastructure India Pvt. Ltd. | 3 Projects in Vadodara  | 1 Completed        |
| 3      | Shreenath Group                        | 12 Projects in Vadodara | 10 Completed       |
| 4      | Nilamber Group                         | 23 Projects in Vadodara | 18 Completed       |
| 5      | Pratham Enterprises                    | 14 Projects in Vadodara | 12 Completed       |
| 6      | J P Iscon                              | 2 Projects in Vadodara  | 2 Completed        |
| 7      | Narayan Realty Ltd.                    | 11 Projects in Vadodara | 8 Completed        |
| 8      | Alembic Group Alchemy Real Estate      | 2 Projects in Vadodara  | 2 Completed        |
| 9      | Shreeji Infrastucture                  | 2 Projects in Vadodara  | 1 Completed        |
| 10     | Kanha Group                            | 22 Projects in Vadodara | 11 Completed       |

    [![magicbricks][magicbricks-screenshot]]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

These are list things you need to use the software and how to install them.

- Python3

The libraries used for the this project are:

- BeautifulSoup
- Selenium
- Requests
- Pandas

### Installation

1. Clone the repository.

   ```
   git clone https://github.com/sagarparmar881/web-scrapping-builders-data.git
   ```

2. Install requirements.

   ```
   pip install -r requirements.txt
   ```

3. Set URLs in **'.env'** file.

   - ##### For `magicbricks.com`

   - Search on google and find the URL of the particular city to scrap the data of builders. Check out the below URL for reference. Make sure to get the exact similar URL or else program might produce unexpected results.

   ```
   BASE_URL_MAGICBRICKS="https://www.magicbricks.com/mbutility/builders-in-Vadodara"
   ```

   - More examples of URLs for `magicbricks.com` can be:
     ```
     https://www.magicbricks.com/mbutility/builders-in--ahmedabad
     ```
     ```
     https://www.magicbricks.com/mbutility/builders-in--Surat
     ```
   - ##### For `www.99acres.com`

   - Search on google and find the URL of the particular city to scrap the data of builders. Check out the below URL for reference. Make sure to get the exact similar URL or else program might produce unexpected results.

   ```
   BASE_URL_99_ACERS="https://www.99acres.com/builders-in-vadodara-bffid"
   ```

   - More examples of URLs for `99acres.com` can be:
     ```
     https://www.99acres.com/builders-in-ahmedabad-bffid
     ```
     ```
     https://www.99acres.com/builders-in-surat-bffid
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

##### For `magicbricks.com`

1. Run the file named `data_scrap_magicbricks.py`

   ```python
   python3 data_scrap_magicbricks.py
   ```

##### For `www.99acres.com`

1. Run the file named `data_scrap_99acers.py`

   ```python
   python3 data_scrap_99acers.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- RESULTS -->

## Results

##### For `magicbricks.com` &`www.99acres.com`

- The final CSV file will be saved in the `data` folder of the root directory of the project.
- The respective file names will be:
  - `99acers_builders_in_vadodara_26082023_154912.csv`
  - `magicbricks_builders_in_vadodara_26082023_152856.csv`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/sagarparmar881/web-scrapping-builders-data.svg?style=for-the-badge
[contributors-url]: https://github.com/sagarparmar881/web-scrapping-builders-data/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sagarparmar881/web-scrapping-builders-data.svg?style=for-the-badge
[forks-url]: https://github.com/sagarparmar881/web-scrapping-builders-data/network/members
[stars-shield]: https://img.shields.io/github/stars/sagarparmar881/web-scrapping-builders-data.svg?style=for-the-badge
[stars-url]: https://github.com/sagarparmar881/web-scrapping-builders-data/stargazers
[issues-shield]: https://img.shields.io/github/issues/sagarparmar881/web-scrapping-builders-data.svg?style=for-the-badge
[issues-url]: https://github.com/sagarparmar881/web-scrapping-builders-data/issues
[license-shield]: https://img.shields.io/github/license/sagarparmar881/web-scrapping-builders-data.svg?style=for-the-badge
[license-url]: https://github.com/sagarparmar881/web-scrapping-builders-data/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sagarparmar881
[99acers-screenshot]: screenshots/data_scrap_99acers.png
[magicbricks-screenshot]: screenshots/data_scrap_magicbricks.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python.org]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/