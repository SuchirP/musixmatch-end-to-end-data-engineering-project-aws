# Musixmatch End-to-End ETL Data Engineering Project AWS
Explore the Musixmatch Data ETL Pipeline! 🎵 This repository houses Python scripts for data extraction, transformation, and loading from the Musixmatch API. Leveraging AWS serverless architecture, get daily updates on music trends. Join us in shaping the future of music data analysis! 🚀 #DataEngineering #AWS #ETLPipeline #MusicData

### Architecture:
![Architecture Diagram](https://github.com/SuchirP/musixmatch-etl-aws-pipeline/blob/main/musixmatch_etl_aws_architecture.jpg)

### About Musixmatch API:
The Musixmatch API offers access to a vast database of music-related data. You can search for lyrics, get track details, retrieve chart data, identify tracks from recordings, and more. It's easy to integrate with your projects and offers various possibilities, like adding lyrics to your player or creating a music trivia game. To start, create a free account, obtain your API key, and begin making requests.

Documentation for the Musixmatch API is available here - [Musixmatch API](https://developer.musixmatch.com/documentation).

### Services Used:
1. **AWS Lambda:** AWS Lambda executes Python functions for data extraction and transformation without managing servers.
   
2. **Amazon S3 (Simple Storage Service):** Amazon S3 stores raw and transformed data extracted from the Musixmatch API.

3. **AWS CloudWatch:** AWS CloudWatch triggers AWS Lambda functions at scheduled intervals for data extraction and transformation.

4. **AWS Glue:** AWS Glue catalogs data stored in S3 buckets, facilitating easy querying and analysis using services like AWS Athena.

5. **AWS Athena:** AWS Athena enables querying and analysis of transformed data stored in S3 buckets using standard SQL.

### Project Execution Flow

1. **Data Extraction and Cleaning (Jupyter Notebook):**
   - Begin by using the Musixmatch API to extract data in Python (Jupyter Notebook).
   - Clean and process the extracted data to create a dataframe containing the required information.

2. **EXTRACT: AWS Lambda Function 1 for Raw Data Extraction:**
   - Set up a trigger in AWS CloudWatch to execute a daily update request.
   - This trigger invokes AWS Lambda function 1, responsible for data extraction.
   - The Lambda function retrieves data from the Musixmatch API using the `requests` library (provided as a layer) and saves the raw data in an AWS S3 bucket.

3. **TRANSFORM: AWS Lambda Function 2 for Data Transformation:**
   - Upon the arrival of raw data in the S3 bucket, another trigger (object put) from CloudWatch activates Lambda function 2.
   - Lambda function 2 performs data transformation tasks on the raw data.
   - Transformed data is then stored in a designated "Transformed" folder within the same AWS S3 bucket.

4. **LOAD: AWS Glue and AWS Athena for Analysis:**
   - AWS Glue, acting as a Data Catalog, identifies all data types and schema.
   - Transformed data stored in the AWS S3 bucket is cataloged by AWS Glue.
   - AWS Athena can then be used for analysis, employing standard SQL queries to gain insights from the transformed data.

### Instructions for Installation and Usage

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Set Up AWS Credentials:**
   - Ensure you have an AWS account and credentials set up with appropriate permissions.
   - Install and configure the AWS CLI if not already installed.

3. **Install Dependencies:**
   - Make sure you have the following Python packages installed:
     - `pymusixmatch`
     - `requests`
     - `pandas`
     - `boto3`

4. **Upload requests Layer:**
   - Upload the `requests_layer.zip` file to AWS Lambda as an external function layer.

5. **Configure Musixmatch API Key:**
   - Replace `<YOUR_API_KEY>` in the code with your Musixmatch API key.

6. **Deploy AWS Lambda Functions:**
   - Deploy `musixmatch_api_data_extract.py` and `musixmatch_transformation_load_function.py` to AWS Lambda.
   - Set up triggers in AWS CloudWatch for the Lambda functions.

7. **Run the Jupyter Notebook:**
   - Open and run `data_analysis.ipynb` for data extraction and analysis.

8. **Monitor AWS Services:**
   - Check CloudWatch logs for Lambda functions.
   - Verify data in the AWS S3 bucket.

9. **Explore Transformed Data:**
   - Analyze transformed data in the AWS S3 bucket.
   - Query data using AWS Athena.

10. **Contributing:**
    - Open issues or submit pull requests on GitHub.

11. **License:**
    - This project is licensed under the [MIT License](LICENSE).

These instructions guide users through setting up and executing the project, from data extraction to analysis, using AWS services, Python scripts, and the provided requests layer for Lambda.

### Install Packages:
```
pip install pymusixmatch
pip install requests
pip install pandas
pip install boto3
```
