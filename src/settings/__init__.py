from src.settings.descriptor_settings import DescriptorSettings
from src.settings.db_settings import DatabaseSettings
from src.settings.api_settings import ApiSettings

db_settings: DatabaseSettings = DatabaseSettings()
api_settings: ApiSettings = ApiSettings()

__all__ = [DescriptorSettings, db_settings, api_settings, DatabaseSettings, ApiSettings]
