from ..services.services import EmailService
from ..utils.utils import EmailUtils
from ..infra.orm import EmailOrm
from ..infra.gateway import EmailSender


def build_email_service(email: str) -> EmailService:
    utils = EmailUtils(email)
    orm = EmailOrm(email)
    sender = EmailSender()
    return EmailService(utils, orm, sender)
