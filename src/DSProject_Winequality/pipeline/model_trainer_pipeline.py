from src.DSProject_Winequality.config.configuration import ConfigurationManager
from src.DSProject_Winequality.components.model_trainer import ModelTrainer
from src.DSProject_Winequality import logger

STAGE_NAME="Model_Trainer_Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer= ModelTrainer(config=model_trainer_config)
        model_trainer.train()