CREATE EXTERNAL TABLE IF NOT EXISTS `zc-lakehouse2`.`accelerometer_trusted` (
  `customerName` string,
  `serialNumber` string,
  `shareWithResearchAsOfDate` bigint,
  `birthDay` string,
  `email` string,
  `timestamp` bigint,
  `user` string,
  `x` float,
  `y` float,
  `z` float
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://zc-lakehouse2/accelerometer/trusted/'
TBLPROPERTIES ('classification' = 'json');