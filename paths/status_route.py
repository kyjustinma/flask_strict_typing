from flask import Blueprint, request
from custom_types.type_def import RaiseAPIException, api_response, check_json


base_route = "/status"
status_route = Blueprint(base_route, __name__)


@status_route.route(f"{base_route}/online", methods=["GET", "POST"])
def status_online():
    if request.method == "GET":
        ## Insert get the status of the robot
        return api_response(
            code=200,
            path=str(request.url_rule),
            object="/online",
            message="Status of the robot",
            data=True,
        )

    raise RaiseAPIException(
        "Invalid API call", "The API you are calling does not exist", status_code=404
    )
