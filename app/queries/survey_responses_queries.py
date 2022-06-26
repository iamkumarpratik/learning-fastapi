from app.queries.sql_context import session
from app.models.survey_responses_table import SurveyResponses


class SurveyResponseQueries:

    @staticmethod
    def create_survey_response(response_data):
        response = SurveyResponses()
        response.set_attributes(response_data)
        response.modified_by = 'Kumar'
        with session.begin() as context:
            context.add(response)
