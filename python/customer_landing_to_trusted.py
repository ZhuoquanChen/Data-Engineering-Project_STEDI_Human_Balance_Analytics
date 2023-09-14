import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="zc-lakehouse2",
    table_name="customer_landing",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("serialnumber", "string", "serialnumber", "string"),
        ("birthday", "string", "birthday", "string"),
        ("sharewithresearchasofdate", "long", "sharewithresearchasofdate", "long"),
        ("customername", "string", "customername", "string"),
        ("email", "string", "email", "string"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node Filter
Filter_node1694722374865 = Filter.apply(
    frame=ChangeSchema_node2,
    f=lambda row: (not (row["sharewithresearchasofdate"] == 0)),
    transformation_ctx="Filter_node1694722374865",
)

# Script generated for node customer_trusted
customer_trusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=Filter_node1694722374865,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://zc-lakehouse2/customer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="customer_trusted_node3",
)

job.commit()
