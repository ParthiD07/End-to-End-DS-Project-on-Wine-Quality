from src.DSProject_Winequality.config.configuration import ConfigurationManager
from src.DSProject_Winequality.components.model_evaluation import ModelEvaluation
from src.DSProject_Winequality import logger

STAGE_NAME="Model_Evaluation_Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()