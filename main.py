from src.FaceClassification import logger
from src.FaceClassification.pipeline.stage_01_data_ingestion import DataIngestionConfigPipeline
from src.FaceClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionConfigPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e


try:
    training_config = config.get_training_config()
    training = Training(config = training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(
        callback_list = callback_list
    )

except Exception as e:
    raise e