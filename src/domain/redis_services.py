import json
from typing import Optional, List, Dict
from redis import Redis

VOICE_ASSESSMENT_PREFIX = "voice_assessment:"

# Create

def create_voice_assessment_redis(r: Redis, id: str, data: Dict) -> None:
    key = VOICE_ASSESSMENT_PREFIX + id
    r.set(key, json.dumps(data))

# Read single

def get_voice_assessment_redis(r: Redis, id: str) -> Optional[Dict]:
    key = VOICE_ASSESSMENT_PREFIX + id
    value = r.get(key)
    if value:
        return json.loads(value)
    return None

# Read all (scan keys)
def get_voice_assessments_redis(r: Redis) -> List[Dict]:
    keys = r.keys(VOICE_ASSESSMENT_PREFIX + "*")
    result = []
    for key in keys:
        value = r.get(key)
        if value:
            result.append(json.loads(value))
    return result

# Update (overwrite)
def update_voice_assessment_redis(r: Redis, id: str, data: Dict) -> None:
    key = VOICE_ASSESSMENT_PREFIX + id
    r.set(key, json.dumps(data))

# Delete
def delete_voice_assessment_redis(r: Redis, id: str) -> None:
    key = VOICE_ASSESSMENT_PREFIX + id
    r.delete(key) 