# Lambda Notes

## Lambda Function Handler

Every Lambda function requires a Handler function. This function consists of an: `event` & `context`.

-   `event`: The payload that gets sent to the Lambda function after a trigger is executed

    -   **Type**: This is typically in the form of a _dictionary_, though could be a _list_, _string_, _integer_, _float_, or _NoneType._
    -   _S3 file that got uploaded, CloudWatch Metric, etc._

-   `context`: Provides additional runtime information to your handler function.
    -   **Type**: _LambdaContext_

## Tid Bits

-   Lambda functions will run for 5 minutes at most
