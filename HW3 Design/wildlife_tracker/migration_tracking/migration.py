from typing import Any
from wildlife_tracker.habitat import Habitat
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    def __init__(self, migration_id: int, migration_path: MigrationPath, start_date: str, status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.start_date = start_date
        self.status = status
    
    
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass
    

    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        pass    