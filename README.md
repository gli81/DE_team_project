[![install](https://github.com/gli81/DE_team_project/actions/workflows/install.yml/badge.svg)](https://github.com/gli81/DE_team_project/actions/workflows/install.yml)

[![lint](https://github.com/gli81/DE_team_project/actions/workflows/lint.yml/badge.svg)](https://github.com/gli81/DE_team_project/actions/workflows/lint.yml)

[![format](https://github.com/gli81/DE_team_project/actions/workflows/format.yml/badge.svg)](https://github.com/gli81/DE_team_project/actions/workflows/format.yml)

[![test](https://github.com/gli81/DE_team_project/actions/workflows/test.yml/badge.svg)](https://github.com/gli81/DE_team_project/actions/workflows/test.yml)

(Insert GitHub Codespaces .devcontainer configuration)

## Auto Scaling Flask App Using Azure Container Platform

[Nutrition Guide Web Application](https://nutfood.azurewebsites.net)

### Architecture Diagram (Annie)

### Overview 

The team project, "Nutrition Guide," is a dynamic, auto-scaling web application microservice that interfaces with the Databricks data pipeline, utilizing Docker for effective containerization and Azure App Services and Flask for deployment and management. 

Explore the user journey within the Nutrition Guide application:

- Nutrient Selection: Users select their desired nutrient from a drop-down menu within the web application.

- Nutrition Query: Upon selection, the application processes this input and searches its database to identify the top 10 foods that are highest in the chosen nutrient.

- Results Display: The web application then displays a detailed list of these top 10 foods, providing users with valuable information about their nutrient content.

<img width="1440" alt="Screen Shot 2023-12-09 at 11 35 20 AM" src="https://github.com/gli81/DE_team_project/assets/143360909/bf7bff5a-e5d3-4e26-ad62-e1eee3bf8984">

### Database

The dataset utilized in our web application is sourced from the United States Department of Agriculture's Food Composition Database, available [here](https://think.cs.vt.edu/corgis/csv/food/). It encompasses a wide range of foods, from everyday items like butter to branded products such as Campbell’s soup. It provides detailed information on various nutrients, including vitamins, minerals, and the macronutrient composition of each food item. Supplementary documenation for each field can be found [here](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fndds-download-databases/). 

Our team downloaded the original dataset and performed data cleaning and aggregation, transforming raw nutritional data into a more organized and analysis-ready format. The final dataset `food_new.csv` categorizes 35 different nutrient types and includes a diverse selection of 2429 food items, making it a valuable resource for nutritional analysis.

### Dependencies Installation and Setup: 

    - Create a Databricks workspace on Azure

    - Connect GitHub account to Databricks Workspace

    - Create global init script for cluster start to store environment variables

    - Establishes a connection to the Databricks environment using environment variables for authentication (SERVER_HOSTNAME, ACCESS_TOKEN and HTTP_PATH).

    - Create a Databricks cluster that supports Pyspark

    - Clone Github repo into Databricks workspace

    - Create a job on Databricks to build an ETL pipeline

    - Estbalishes a connection between Databricks and Github (SERVER_HOSTNAME, ACCESS_TOKEN and HTTP_PATH)

    - Specify installation requirements `requirements.txt`

    ```
    #devops
    black==22.3.0
    click==8.1.3 
    pytest==7.1.3
    pytest-cov==4.0.0
    requests
    #rust based linter
    ruff==0.0.284
    ## databricks
    pandas
    # python-dotenv
    # databricks-sql-connector
    ## for server to receive requests
    flask
    # sqlite3 ## include in base
    gunicorn
    python-dotenv
    databricks-sql-connector
    ```

    - install: `make install`

    - run: `python3 server/server.py` and navigate to the locally hosted website

    - Build docker image: docker build --tag <insert image name> .

    - Login to azure cli: `az login`

    - Deploy Azure web app: `az containerapp up --resource-group <insert resource group> --name <insert app name> --ingress external --target-port 50505 --source .`

    - View app via `container apps` and docker image via `container registry` in azure web portal 

### AI Pair Programming Tools

In our development process, we integrated advanced AI Pair Programming tools, specifically GitHub Copilot and AWS CodeWhisper, to enhance our coding efficiency and accuracy. GitHub Copilot's real-time code suggestions were particularly helpful in refining our algorithms and debugging. Similarly, AWS CodeWhisper played a crucial role, especially when we needed to adapt our existing ETL (Extract, Transform, Load) queries for compatibility with different platforms. It assisted us in seamlessly converting ETL queries, originally tailored for SQLite, into a format suitable for use with Databricks, ensuring smooth data processing and integration. 

### Microservice

#### Databricks ETL(Extract,Transform,Load)-Query Pipeline 

- Extract task (Data Source): `server/mylib/extract_databricks.py`

    - automate the process of downloading the file `food_new.csv` from a specified URL and uploading it to a Databricks Filestore.   

- Transform and Load Task (Data Sink): `server/mylib/transform_load_databricks.py`

    - takes the file `food_new.csv`, transforms it by adding unique IDs, and loads it into a Delta Lake table `Food` for further use in data analytics and other Spark-based data processing tasks.

- Query Task: `server/mylib/query_food.py`, `server/mylib/query_nutrition.py`

    - querying the structure of the food table in a Databricks database, processing the column names, and logging both the query and its results for documentation.

    - querying nutritional data from a Databricks database (constructing a SQL query to select the top 10 food categories, ordered by a specified nutrition column. This column is dynamically determined based on the input argument 'nutrition'). Systematically logging the queries and their outcomes for documentation.

(Insert DBFS, delta lake, pipeline screenshot)

#### Logging Result

[query_log_food.md](./server/mylib/query_log_food.md)

[query_log_nutrition.md](./server/mylib/query_log_nutrition.md)

(Insert screenshot of query result in datarbricks sql editor)

#### Flask Web Application:

- **Functionality:** The web application enables users to choose a nutrient from a drop-down menu, processes this input to query its database for the top 10 foods highest in the selected nutrient, and then displays a detailed list of these foods on a results page.

    - `server/server.py`: creates a web application that allows users to interact with a nutritional database, querying for different nutrients and displaying relevant foods and their nutritional content. 

- **HTML Templates:** The project contains HTML templates (`index.html`, `result.html`) providing a user-friendly interface.

    - `index.html`: creates a user interface for a web application that allows users to select a nutritional category from a dropdown menu and view information about it. 

    - `result.html`: displays specific nutrition and food information in a table format.

- **Static Image:** The project contains a `nuts.ipg` image in the `static` folder providing a user-friendly website design. 

#### Github Actions:
- **Makefile & CICD:** The workflow includes running a `Makefile` to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

#### Web App Optimization:
- **Gunicorn configuration file:** The `gunicorn.conf.py` optimize the performance and reliability of a Python web application in a production environment. It balances resource use with the ability to handle a significant number of concurrent requests.

#### Docker Containerization:
- **Dockerfile:** This Dockerfile containerizes a Flask app, setting up a Docker container with Python and Gunicorn to run the web application. It encapsulates the app's code and dependencies, simplifying deployment across different environments.

### Azure Container Apps Deployment:

- **Azure Container Registry :** The Docker image is hosted on Azure Container Registry

(insert screenshot of docker image on azure)

- **Azure Container Apps Deployment:** The Flask app is successfully deployed on Azure Container Apps, providing a public endpoint for users to interact with the application.

(insert screenshot of azure container app deployment web page)

### Data Engineering 

We effectively leveraged key data engineering libraries, namely PySpark and databricks-sql, to streamline our Databricks ETL (Extract, Transform, Load) and query processes. PySpark, the Python API for Apache Spark, was pivotal in transforming and loading operations on our datasets. Additionally, for querying purposes, we utilized the databricks-sql Python package. This allowed us to efficiently connect to and execute queries on a Databricks SQL endpoint.

### IAC (Infrastructure of Code) (Wait for Gavin to upload)

### Check Format and Test Errors: 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`

### Load Test 

Our microservice is capable of handling 10,000 requests per second.

<img width="1422" alt="8982a2b29943c9a2893ed2ed35769bbf 2" src="https://github.com/gli81/DE_team_project/assets/143360909/1af6b5e5-032f-4ecd-9b54-12bf871679c3">

<img width="1423" alt="ba53fea524cef1c1463f9c06d649ddfd 2" src="https://github.com/gli81/DE_team_project/assets/143360909/25e1bbff-600c-48ce-9874-0453e0aed244">

<img width="1419" alt="e4841b64b307f8abc4ee0bc24e161fa9" src="https://github.com/gli81/DE_team_project/assets/143360909/6a0f2992-1315-4142-a2be-e86e64ed083c">

### Quantitative Assessment (Annie)

The project must include a quantitative assessment of its reliability and stability. You must use data science fundamentals to describe system performance, e.g., average latency per request at different levels of requests per second (100, 1000, etc.). Think of the software system as a data science problem that needs to be described using data science principles.

### Limitations and Potential Improvement

- Limitations: The current iteration of the "Nutrition Guide" application, while robust in its fundamental capabilities, is limited in terms of personalized user engagement and versatility. The absence of features such as diet planning, nutritional advice, and integration with health tracking apps restricts the application's appeal to users seeking a more comprehensive health and nutrition management tool. Additionally, the inability for users to input custom foods or recipes for nutritional analysis limits the app's practicality for those with specific dietary preferences or needs.

- Potential Improvements: To overcome these limitations, the application could greatly benefit from integrating AI-driven features that offer personalized nutrition recommendations tailored to individual user health data. This enhancement would not only make the app more engaging but also more useful in supporting users' unique health goals. Further, incorporating advanced AI Pair Programming tools could enable predictive analytics and user behavior analysis, paving the way for more intuitive and responsive user interactions. Expanding the app's features to include diet planning, integration with health trackers, and the ability to analyze custom food inputs would significantly broaden its utility and appeal. Such improvements would transform the app into a more holistic nutritional guide, catering to a diverse range of user needs and preferences in the realm of health and wellness.
