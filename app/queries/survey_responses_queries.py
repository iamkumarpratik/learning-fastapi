from app.queries.sql_context import session
from app.models.survey_responses_table import SurveyResponses


class SurveyResponseQueries:

    @staticmethod
    def create_survey_response(response_data):
        response = SurveyResponses()
        response.full_name = response_data.full_name
        response.occupation = response_data.occupation
        response.favourite_tech = response_data.favourite_tech
        response.skill = response_data.skill
        response.current_competence_area = response_data.current_competence_area
        response.linkedin_url = response_data.linkedin_url
        response.certificates = response_data.certificates
        response.modified_by = 'Kumar'
        with session.begin() as context:
            context.add(response)
