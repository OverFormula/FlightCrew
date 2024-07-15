import json
from typing import Any


class CrewConfig:
  config_data: Any

  def __init__(self):
    with open('config/config.json') as config:
      self.config_data = json.load(config)

  def get_poll_interval(self):
    return self.config_data['poll_interval']

  def get_token(self):
    return self.config_data['token']

  def get_score_threshold(self):
    return self.config_data['score_threshold']

  def get_max_selected(self):
    return self.config_data['max_selected']

  def get_no_response_answer(self):
    return self.config_data['no_response_answer']

  def get_cron_task_granularity_seconds(self):
    return self.config_data['cron_task_granularity_seconds']

  def get_chat_id(self):
    return self.config_data['chat_id']

  def get_connection_pool_size(self):
    return self.config_data['connection_pool_size']
