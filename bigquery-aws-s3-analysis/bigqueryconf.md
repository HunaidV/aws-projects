## Connection

1. Create an external connection for Bigquery Studio using AWS Biglake s3
2. Add the role arn we copied from IAM role
3. Create dataset. Make sure to choose region of aws
4. Create external table using s3 and provide path of s3 -> s3://bucketname/filename.sql


## export query results to same s3 bucket
<code>
EXPORT DATA WITH CONNECTION '<connection-name'>
OPTIONS(uri="s3://S3 bucket name/exports/*", format="CSV")
AS <your sql query>
</code>