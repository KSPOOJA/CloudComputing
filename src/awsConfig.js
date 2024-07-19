// awsConfig.js
import AWS from 'aws-sdk';

AWS.config.update({
  region: 'us-east-1',
  accessKeyId: 'AKIA5FTZABD23BTA2HK3',
  secretAccessKey: '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',
});

const dynamoDB = new AWS.DynamoDB.DocumentClient();
const cognito = new AWS.CognitoIdentityServiceProvider();

export { dynamoDB, cognito };
