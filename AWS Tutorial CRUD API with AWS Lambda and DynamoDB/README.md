# AWS Tutorial: CRUD API with AWS Lambda and DynamoDB

## Overview

This project is a CRUD (Create, Read, Update, Delete) API built with AWS Lambda and DynamoDB, following an AWS tutorial. The API allows you to perform basic operations on items stored in a DynamoDB table.

**Note: This project is based on a tutorial from AWS.**

## Prerequisites

Before getting started, ensure you have the following:

- AWS account with the necessary permissions to create Lambda functions and DynamoDB tables.
- AWS CLI installed and configured with the appropriate credentials.

## Tutorial Source

This project is based on the official AWS tutorial. You can find the tutorial [here](<https://catalog.us-east-1.prod.workshops.aws/workshops/2c8321cb-812c-45a9-927d-206eea3a500f/en-US/010-createadynamodbtable>).

You can also find the summarize steps below.

## Setup

### 1. Create a DynamoDB Table

- Log in to the AWS Management Console.
- Navigate to the DynamoDB service.
- Create a new table named `http-crud-tutorial-items` with the necessary attributes.

### 2. Set up the Lambda Function

- Navigate to the AWS Lambda service.
- Create a new Lambda function (you can use the code).
- Choose the runtime (e.g., Node.js) based on your preference.
- Configure the function with an IAM role that has the necessary permissions.

### 3. Define the Lambda Function Code

- Write code that implements CRUD operations on the DynamoDB table. You can use the tutorial, which is in Node JS or mine, which is in Python.

## Usage
1. Trigger the Lambda function manually or set up an event trigger.
2. Use API Gateway or another method to interact with the API endpoints.

## Additional Notes
-  Customize the Lambda function code based on your specific use case.
- Ensure that your Lambda execution role and DynamoDB table have the necessary permissions.

## Resources
- AWS Lambda Documentation
- AWS DynamoDB Documentation
- AWS Tutorial: Building a RESTful Web API with AWS Lambda, DynamoDB, and API Gateway

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.