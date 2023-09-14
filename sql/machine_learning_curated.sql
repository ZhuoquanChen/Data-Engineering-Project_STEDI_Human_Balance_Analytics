CREATE EXTERNAL TABLE IF NOT EXISTS `zc-lakehouse2`.`machine_learning_curated` (
  `customername` string,
  `serialNumber` string,
  `sharewithresearchasofdate` bigint,
  `birthday` string,
  `email` string,
  `x` float,
  `y` float,
  `z` float,
  `sensorreadingtime` bigint,
  `right_serialnumber` string,
  `distancefromobject` int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://zc-lakehouse2/accelerometer/curated/'
TBLPROPERTIES ('classification' = 'json');