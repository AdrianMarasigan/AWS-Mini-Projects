# Serverless Data Analysis with AWS Lambda and Amazon Athena

## Overview

The "Serverless Data Analysis with AWS Lambda and Amazon Athena" project aims to create a streamlined data analysis pipeline using serverless components within the AWS ecosystem. This project leverages AWS Lambda for event-driven data processing and Amazon Athena for query-based analysis on data stored in an S3 bucket.

## Prerequisites

Before getting started, ensure you have the following:

- AWS account with the necessary permissions to create Lambda functions, Athena Database, S3 buckets and IAM roles.

## Setup

1. Generate Sample Data:
- Create a simple CSV file with sample data (e.g., user transactions, sensor readings).
- Upload this CSV file to an S3 bucket.

2. Create an Athena Database and Table:
- In the Athena service, create a new database.
- Define a table schema that corresponds to your sample data.
- Use the S3 bucket and path where you uploaded the CSV as the table source.

3. Write Lambda Function for Data Processing:
- Create a new Lambda function.
- Configure the function to have permissions to read from the S3 bucket and execute Athena queries.
- Write code to trigger data processing logic (e.g., data transformation) when new data is uploaded to the S3 bucket.

4. Configure S3 Trigger for Lambda:
- In the Lambda function settings, add an S3 trigger.
- Choose the S3 bucket where you're uploading the data.
- Set the event type to trigger the Lambda function (e.g., Object Created).

5. Run the Data Analysis:
- Upload new sample data to the S3 bucket.
- Monitor the Lambda function's execution in the CloudWatch Logs.
- Check the Athena query results in the Athena console.

## Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS Athena](https://aws.amazon.com/athena/)
- [AWS S3](https://aws.amazon.com/s3/)

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.