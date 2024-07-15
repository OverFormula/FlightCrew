from case.core.case import Case
from config.crew_config import CrewConfig
from tenet.core.tenet_registry import TenetRegistry
from fuzzywuzzy import fuzz

crew_config = CrewConfig()


class QueryProcessor:

  def process_query(self, text) -> str:
    query = text.lower()
    tenets = TenetRegistry.get_tenets()

    scored_cases = self.score_cases(tenets, query)
    selected_cases = self.select_cases(scored_cases)
    return self.combine_answers(selected_cases, query)

  def score_cases(self, tenets: list, query: str) -> dict:
    case_ratio = {}

    for tenet in tenets:
      for case in tenet.cases():
        case_ratio[case] = self.score_case(case, query)

    print(case_ratio)
    return case_ratio

  def score_case(self, case: Case, query: str) -> int:
    max_ratio = 0

    if not case.tags():
      return max_ratio

    for key_phrase in case.tags():
      max_ratio = max(max_ratio, fuzz.ratio(key_phrase, query))

    return max_ratio

  def select_cases(self, scored_cases: dict) -> dict:
    threshold = crew_config.get_score_threshold()
    filtered_dict = {k: v for k, v in scored_cases.items() if v > threshold}

    sorted_items = sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items[:crew_config.get_max_selected()])

  def combine_answers(self, selected_cases: dict, query: str) -> str:
    if not selected_cases:
      return crew_config.get_no_response_answer()

    answer = '\n'

    for case, score in selected_cases.items():
      answer += case.process(query) + ' (score: ' + str(score) + ')\n'

    return answer
