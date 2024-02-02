## Create Policy for s3 to provide required access for read and write

1. Bucketlevel list access for the bucket
2. Add object level access if required
3. Add object put access to write data to that bucket

Refer the policy s3policy.json

## Create role and add trust relationship with federating google service
1. Add the trust relationship json policy as specified in bigqueryconf.d
2. Save the arn of aws role for further use


