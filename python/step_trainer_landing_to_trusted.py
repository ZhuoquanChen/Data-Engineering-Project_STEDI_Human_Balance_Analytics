import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="zc-lakehouse2",
    table_name="step_trainer_landing",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node PrivacyFilter
PrivacyFilter_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("sensorreadingtime", "long", "sensorreadingtime", "long"),
        ("serialnumber", "string", "serialnumber", "string"),
        ("distancefromobject", "int", "distancefromobject", "int"),
    ],
    transformation_ctx="PrivacyFilter_node2",
)

# Script generated for node step_trainer_trusted
step_trainer_trusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=PrivacyFilter_node2,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://zc-lakehouse2/step_trainer/trusted/",
        "compression": "snappy",
        "partitionKeys": [],
    },
    transformation_ctx="step_trainer_trusted_node3",
)

job.commit()
