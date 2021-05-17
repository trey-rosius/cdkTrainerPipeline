from aws_cdk import core

from cdk_trainer_pipeline.cdk_trainer_pipeline_stack import CdkPipelineTrainerStack

class WebServiceStage(core.Stage):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = CdkPipelineTrainerStack(self, 'WebService')

