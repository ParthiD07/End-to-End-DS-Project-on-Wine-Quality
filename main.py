from src.DSProject_Winequality import logger
from src.DSProject_Winequality.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DSProject_Winequality.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DSProject_Winequality.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DSProject_Winequality.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.DSProject_Winequality.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data_Validation_Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data_Transformation_StAGE"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model_Trainer_Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model_Evaluation_Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_evaluation=ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
      
