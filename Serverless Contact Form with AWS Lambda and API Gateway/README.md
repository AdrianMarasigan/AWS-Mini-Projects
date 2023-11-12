# Image Processing with AWS Lambda and S3

## Overview

This project demonstrates how to create a serverless contact form for a website using AWS Lambda and API Gateway. Messages submitted through the form will be processed and sent via Simple Email Service (SES).

## Prerequisites

Before getting started, ensure you have the following:

- AWS account with the necessary permissions to create Lambda functions, APIs, and IAM roles.

## Setup

1. Create an API Gateway:
- In the AWS Management Console, navigate to API Gateway.
- Create a new API.
- Create a resource and a POST method for handling form submissions.
- Create an AWS Lambda Function:

2. Create a new Lambda function to process the form data.
- Use an IAM role with the AmazonSESFullAccess policy to allow sending emails through SES.
- Write code in your preferred language (e.g., Node.js or Python) to handle the form submission and send an email using SES.

3. Integrate Lambda Function with API Gateway:
- onnect the Lambda function to the API Gateway as the integration for the POST method.

4. Test the Contact Form:
- Deploy the API Gateway.
- Replace the API_GATEWAY_URL in the JavaScript code with the deployed API endpoint.
- Test the contact form by submitting messages.


## Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS API Gateway Documentation](https://aws.amazon.com/api-gateway/)

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.