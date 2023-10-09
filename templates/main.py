from cnnClassifier import logger
from cnnClassifier.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.state_02_prepare_base_model import PrepareBaseModelTrainingPipeline
STAGE_NAME = " Data Ingestion Stage"

try:
        
        logger.info(f">>>> stage {STAGE_NAME} started>>>>")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> stage {STAGE_NAME} completed>>>>")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e