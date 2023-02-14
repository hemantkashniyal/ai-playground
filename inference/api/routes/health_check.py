from fastapi import APIRouter

from inference.core.config import API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG
from inference.api.routes.health_check_payloads import HeartbeatResult, HealthCheckResult

router = APIRouter()

@router.get("/", response_model=HealthCheckResult, name="health")
def get_health() -> HealthCheckResult:
    health = HealthCheckResult(
        appName=APP_NAME,
        appVersion=APP_VERSION,
        debug=IS_DEBUG
    )
    return health


@router.get("/heartbeat", response_model=HeartbeatResult, name="heartbeat")
def get_hearbeat() -> HeartbeatResult:
    heartbeat = HeartbeatResult(isAlive=True)
    return heartbeat
