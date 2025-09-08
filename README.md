# Project: Agentic AI Weather Detection System

##Description

This project is an **Agentic AI Weather Detection System** built on AWS.
It works as an **intelligent weather agent** that perceives live weather data from the **OpenWeather API**, processes it with reasoning, stores results, and takes appropriate actions.

The system follows the **Agentic AI cycle**:

* **Perception** – Collect weather data using API
* **Processing/Reasoning** – Classify temperature (Hot, Mild, Cold) & detect rain alerts
* **Memory** – Store raw and processed data in **S3 & DynamoDB**
* **Action** – Provide structured weather predictions via API Gateway


## Steps Performed for Implementation

1. **OpenWeather API Setup**

   * Generated API key from [OpenWeather](https://openweathermap.org/api)
   * Tested endpoint using Python script

2. **AWS S3 Bucket Creation**

   * Created bucket: `weather-agent-bucket-<unique-id>`
   * Used it to store **raw weather JSON data**

3. **AWS DynamoDB Table Setup**

   * Table: `WeatherPredictions`
   * Partition key: `timestamp`
   * Stores processed results: temperature, condition, rain alert

4. **IAM Role Creation**

   * Role: `WeatherAgentLambdaRole`
   * Permissions: `AmazonS3FullAccess`, `AmazonDynamoDBFullAccess`, `CloudWatchLogs`

5. **Lambda Function Development**

   * Wrote Python script (`lambda_function.py`)
   * Fetches data → categorizes → saves to S3 & DynamoDB
   * Configured Environment Variables:

     * `OPENWEATHER_API_KEY`
     * `CITY` (Pune)
     * `S3_BUCKET`
     * `DDB_TABLE`
     * `UNITS` (metric)
     * `LANG` (en)

6. **API Gateway Setup**

   * Created REST API endpoint `/weather`
   * Integrated with Lambda function
   * Exposed publicly accessible URL

7. **Testing & Logging**

   * Invoked Lambda manually
   * Verified raw JSON in **S3**
   * Verified predictions in **DynamoDB**
   * Monitored logs in **CloudWatch**

---

## 🏗 Architecture Diagram
![1755954904470](https://github.com/user-attachments/assets/f49ba577-f2f5-44fe-a205-5212cb930b23)

## 📊 Output Example
![1755954904148](https://github.com/user-attachments/assets/902758cd-b3a2-4ea1-96d1-98cc84fa2f1a)



## 🚀 Tech Stack

* **AWS Lambda** (Python 3.9)
* **Amazon API Gateway**
* **Amazon S3** (raw weather storage)
* **Amazon DynamoDB** (processed predictions)
* **Amazon CloudWatch** (logs & monitoring)
* **AWS IAM** (secure access)
* **OpenWeather API**

👨‍💻 Author

Shubham Ghalsasi

🌐 LinkedIn
