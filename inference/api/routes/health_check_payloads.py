from typing import Optional
from pydantic import BaseModel

class HealthCheckResult(BaseModel):
    appName: str
    appVersion: str
    debug: Optional[bool] = False



class HeartbeatResult(BaseModel):
    isAlive: bool
