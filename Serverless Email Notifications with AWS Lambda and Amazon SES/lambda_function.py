const AWS = require('aws-sdk');

const ses = new AWS.SES();

exports.handler = async (event, context, callback) => {
    const params = {
        Destination: {
            ToAddresses: ['recipient@example.com'], // Replace with your recipient email address
        },
        Message: {
            Body: {
                Text: { Data: 'Hello, this is a serverless email notification!' },
            },
            Subject: { Data: 'Serverless Email Notification' },
        },
        Source: 'sender@example.com', // Replace with your verified SES sender email address
    };

    try {
        const result = await ses.sendEmail(params).promise();
        console.log('Email sent:', result);
        callback(null, 'Email sent successfully.');
    } catch (error) {
        console.error('Error sending email:', error);
        callback('Error sending email.');
    }
};
