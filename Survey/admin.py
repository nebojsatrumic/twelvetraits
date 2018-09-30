from django.contrib import admin
from Survey.models import Respondent, Survey, Question, Answer


class RespondentAdmin(admin.ModelAdmin):
    model = Respondent

    list_display = ('id', 'ip_address', 'email', 'phone_number')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'ip_address')
    list_filter = ('email',)
    list_per_page = 50
    save_as = True

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


class SurveyAdmin(admin.ModelAdmin):
    model = Survey

    list_display = ('id', 'name', 'active')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'active')
    list_filter = ('name',)
    list_per_page = 50
    save_as = True


class QuestionAdmin(admin.ModelAdmin):
    model = Question

    list_display = ('id', 'question_text', 'survey', 'ordinal_number')
    list_display_links = ('question_text', 'ordinal_number')
    search_fields = ('question_text', 'ordinal_number')
    list_filter = ('survey',)
    list_per_page = 50
    save_as = True


class AnswerAdmin(admin.ModelAdmin):
    model = Answer

    list_display = ('id', 'answer_text', 'question', 'respondent')
    list_display_links = ('answer_text', 'question')
    search_fields = ('answer_text', 'question')
    list_filter = ('question', 'respondent')
    list_per_page = 50
    save_as = True


admin.site.register(Respondent, RespondentAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.site_header = "Surveys administration"
