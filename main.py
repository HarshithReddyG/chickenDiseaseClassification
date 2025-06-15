from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipeline
from cnnClassifier.constants import STAGE_1




try:
        logger.info(f">>>>> stage {STAGE_1} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_1} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e