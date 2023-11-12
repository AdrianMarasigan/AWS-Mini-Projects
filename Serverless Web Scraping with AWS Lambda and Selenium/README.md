# Web Scraping with Selenium in AWS Lambda

## Overview

This project demonstrates how to perform web scraping using Selenium in an AWS Lambda function. The Lambda function is designed to navigate to a specified URL, retrieve information, and return the results. In this example, it navigates to the World Bank Data Catalog homepage and retrieves the title of the page.

## Prerequisites

Before getting started, ensure you have the following:

- AWS account with the necessary permissions to create Lambda functions.
- AWS CLI installed and configured with the appropriate credentials.

## Setup

### 1. Set up the Lambda Function

- Navigate to the AWS Lambda service.
- Create a new Lambda function.
- Choose the runtime (e.g., Python) based on your preference.
- Configure the function with an IAM role that has the necessary permissions.

### 2. Add Dependencies

- Include the necessary dependencies, such as the Selenium library and the ChromeDriver executable.
- Ensure the ChromeDriver version matches the version compatible with the installed Chrome browser on the Lambda execution environment.

### 3. Define the Lambda Function Code

- Write code that utilizes Selenium to perform web scraping.
- Refer to the provided sample code in the README or create your own based on your web scraping requirements.

### 4. Configure Lambda Execution Role

- Ensure the Lambda execution role has the necessary permissions to write logs to CloudWatch.

## Usage

1. Trigger the Lambda function manually or set up an event trigger.
2. Check the CloudWatch Logs for the Lambda function's output, including the retrieved webpage title.

## Additional Notes

- Customize the web scraping logic in the Lambda function based on your specific use case.
- Be mindful of the execution environment's limitations on AWS Lambda, such as memory and timeout constraints.

## Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
