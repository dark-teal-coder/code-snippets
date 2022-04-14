-- Author: github.com/dark-teal-coder

-- Right click on the table name and choose [Popup Describe] > [Columns] to see column names. 
-- A table's primary key is another table's foriegn key. 
-- Right click on the table name and choose [Popup Describe] > [Constraints] to check primary key and foreign keys of a table. 
-- Joining condition syntax: table1.primary_key = table2.primary_key 
-- If DELETING_DATETIME has a value, it means the record has been deleted. So, we want those that don't contain any value (i.e. NULL). 

-- Column headers 
SELECT FA.AGENT_CODE
	, FA.AGENT_NAME
	, FSC.START_TIME
	, FSC.END_TIME
	, FL.LOCATION_CODE
	, FSC.DAY_OF_WEEK
-- Table abbreviations 
FROM FA_AGENTS FA
	, FA_AGENT_CTO_SERVICES FACS
	, FA_SCHEDULE_COLLECTIONS FSC
	, FA_SCH_COLLECTION_TRUCK_DOCKS FSCT
	, FM_TRUCK_DOCKS FTD
	, FM_LOCATIONS FL
WHERE 1 = 1
-- Joining conditions
	AND FA.AGENT_UID = FACS.AGENT_UID
	AND FACS.AGENT_CTO_SERVICE_UID = FSC.AGENT_CTO_SERVICE_UID
	AND FSC.SCHEDULE_COLLECTION_UID = FSCT.SCHEDULE_COLLECTION_UID     
	AND FSCT.SCH_COLLECTION_TRUCK_DOCK_UID = FTD.SCH_COLLECTION_TRUCK_DOCK_UID
	AND FTD.TRUCK_DOCK_UID = FL.TRUCK_DOCK_UID
-- Filtering conditions
	AND FA.DATA_LIFECYCLE_MODE = 'A'
	AND FA.DELETING_DATETIME IS NULL
	AND FACS.DELETING_DATETIME IS NULL
	AND FSC.DELETING_DATETIME IS NULL
	AND FSCT.DELETING_DATETIME IS NULL
	AND FTD.DELETING_DATETIME IS NULL
	AND FL.DELETING_DATETIME IS NULL
; 
