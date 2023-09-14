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

# Script generated for node accelerometer_trusted
accelerometer_trusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="zc-lakehouse2",
    table_name="accelerometer_trusted",
    transformation_ctx="accelerometer_trusted_node1",
)

# Script generated for node step_trainer_landing
step_trainer_landing_node1694634844851 = glueContext.create_dynamic_frame.from_catalog(
    database="zc-lakehouse2",
    table_name="step_trainer_landing",
    transformation_ctx="step_trainer_landing_node1694634844851",
)

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1694639382796 = ApplyMapping.apply(
    frame=step_trainer_landing_node1694634844851,
    mappings=[
        ("sensorreadingtime", "long", "sensorreadingtime", "long"),
        ("serialnumber", "string", "right_serialnumber", "string"),
        ("distancefromobject", "int", "distancefromobject", "int"),
    ],
    transformation_ctx="RenamedkeysforJoin_node1694639382796",
)

# Script generated for node Join
Join_node1694634939680 = Join.apply(
    frame1=RenamedkeysforJoin_node1694639382796,
    frame2=accelerometer_trusted_node1,
    keys1=["sensorreadingtime"],
    keys2=["sharewithresearchasofdate"],
    transformation_ctx="Join_node1694634939680",
)

# Script generated for node JoinFilter
JoinFilter_node2 = ApplyMapping.apply(
    frame=Join_node1694634939680,
    mappings=[
        ("sensorreadingtime", "long", "sensorreadingtime", "long"),
        ("right_serialnumber", "string", "right_serialnumber", "string"),
        ("distancefromobject", "int", "distancefromobject", "int"),
        ("customername", "string", "customername", "string"),
        ("serialnumber", "string", "serialnumber", "string"),
        ("sharewithresearchasofdate", "long", "sharewithresearchasofdate", "long"),
        ("birthday", "string", "birthday", "string"),
        ("email", "string", "email", "string"),
        ("x", "float", "x", "float"),
        ("y", "float", "y", "float"),
        ("z", "float", "z", "float"),
    ],
    transformation_ctx="JoinFilter_node2",
)

# Script generated for node machine_learning_curated
machine_learning_curated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=JoinFilter_node2,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://zc-lakehouse2/accelerometer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="machine_learning_curated_node3",
)

job.commit()
