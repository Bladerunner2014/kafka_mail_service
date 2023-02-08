from smtplib import SMTP_SSL
from email.message import EmailMessage
from dotenv import dotenv_values
from constants.error_message import ErrorMessage
from constants.info_message import InfoMessage
from constants.status_code import StatusCode
import logging
from http_handler.request_handler import RequestHandler
from http_handler.response_handler import ResponseHandler

logger = logging.getLogger(__name__)
req = RequestHandler()
config = dotenv_values(".env")
res = ResponseHandler()


def send_mail(contacts):
    msg = EmailMessage()
    print (msg)
    msg["From"] = config["EMAIL_SENDER"]
    msg["Subject"] = "test"
    try:
        with SMTP_SSL(config["EMAIL_SERVER"], config["PORT"]) as smtp:
            for contact in contacts:
                # to get html temp and format it with user details
                result = get_html_temp(contacts["template"])
                # with open(get_html_temp(contacts["template_id"]), 'r+') as level_1:
                #     string_html_temp = level_1.read().format(**contact)
                result = result["content"]

                msg.add_alternative(result.format(**contact), subtype="html")
                smtp.login(config["EMAIL_SENDER"], config["PASSWORD"])
                smtp.send_message(msg, to_addrs=contact["email"])
                logger.info(InfoMessage.EMAIL_SENT)

    except Exception as error:
        logger.error(ErrorMessage.HTML_FILE)
        logger.error(error)
        raise Exception
    res.set_status_code(StatusCode.SUCCESS)
    return res


def get_html_temp(template_id):
    try:
        result = req.send_get_request(base_url=config["MAIL_BASE_URL"],
                                      end_point=config["MAIL_GET_URL"]+template_id,
                                      port=config["MAIL_PORT"],
                                      timeout=config["MAIL_TIMEOUT"],
                                      error_log_dict={"message": ErrorMessage.BAD_REQUEST})
        print(result)
    except Exception as error:
        logger.error(ErrorMessage.HTML_DB)
        logger.error(error)
        raise Exception

    return result
