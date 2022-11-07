from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline

# from fastapi import FastAPI
# from sensor.constant.application import APP_HOST, APP_PORT
# from starlette.responses import RedirectResponse
# from uvicorn import run as app_run
# from fastapi.responses import Response


if __name__ == '__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)