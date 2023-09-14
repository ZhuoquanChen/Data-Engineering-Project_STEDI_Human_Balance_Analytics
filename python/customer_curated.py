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

# Script generated for node customer_trusted
customer_trusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="zc-lakehouse2",
    table_name="customer_trusted",
    transformation_ctx="customer_trusted_node1",
)

# Script generated for node accelerometer_landing
accelerometer_landing_node1694617034207 = glueContext.create_dynamic_frame.from_catalog(
    database="zc-lakehouse2",
    table_name="accelerometer_landing",
    transformation_ctx="accelerometer_landing_node1694617034207",
)

# Script generated for node Join
Join_node1694617205090 = Join.apply(
    frame1=customer_trusted_node1,
    frame2=accelerometer_landing_node1694617034207,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="Join_node1694617205090",
)

# Script generated for node JoinFilter
JoinFilter_node2 = ApplyMapping.apply(
    frame=Join_node1694617205090,
    mappings=[
        ("customername", "string", "customername", "string"),
        ("serialnumber", "string", "serialnumber", "string"),
        ("sharewithresearchasofdate", "long", "sharewithresearchasofdate", "long"),
        ("birthday", "string", "birthday", "string"),
        ("email", "string", "email", "string"),
        ("timestamp", "long", "timestamp", "long"),
        ("user", "string", "user", "string"),
        ("x", "float", "x", "float"),
        ("y", "float", "y", "float"),
        ("z", "float", "z", "float"),
    ],
    transformation_ctx="JoinFilter_node2",
)

# Script generated for node Drop Fields
DropFields_node1694633530136 = DropFields.apply(
    frame=JoinFilter_node2,
    paths=["timestamp", "user", "x", "y", "z"],
    transformation_ctx="DropFields_node1694633530136",
)

# Script generated for node customer_curated
customer_curated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1694633530136,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://zc-lakehouse2/customer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="customer_curated_node3",
)

job.commit()
