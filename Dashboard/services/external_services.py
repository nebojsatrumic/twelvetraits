class ExternalService():
    def retrieve_respondat_survey_data(self):
        return [{'email': 'test@test.com',
                'location': 'France',
                'phone_number': '+38111233233'
                }]


class GoogleSurveyService():
    def retrieve_respondat_survey_data(self):
        return [{'email': 'flow@test.com',
                'location': 'USA',
                'phone_number': '+381114444333'
                }]


class FacebookSurveyService():
    def retrieve_respondat_survey_data(self):
        return [{'email': 'one@test.com',
                'location': 'Austria',
                'phone_number': '+38111321211'
                }]
