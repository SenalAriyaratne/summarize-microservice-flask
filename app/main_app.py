from controller import ApplicationController
from app_routes import AppRoutes
from hf_lang_model import ModelBuilder

myapp =  ApplicationController.Application(AppRoutes, ModelBuilder)

if __name__ == '__main__':
  myapp.run_application()
  