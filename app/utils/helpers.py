from ..models import UserProject, UserStage
from . import constants


def check_token(user, token):
    return user.customuser.verify_token == token


def is_in_project(user, project):
    return UserProject.objects.filter(user=user, project=project).exists()


def is_pm(user, project):
    user_project = UserProject.objects.filter(user=user, project=project)
    return user_project[0].role == constants.PROJECT_MANAGER


def is_stage_owner(user, stage):
    user_stage = UserStage.objects.filter(user=user, stage=stage)
    return user_stage[0].role == constants.STAGE_OWNER