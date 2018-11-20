from model_utils import Choices

FEE_TYPE = Choices(
    ('fixed', 'Fixed'),
    ('percentage', 'Percentage'),
)

SYSTEM_CONFIG = Choices(
    ('user_limit', 'User limit'),
)

EMAIL_PURPOSE = Choices(
    ('email_verification', 'Email verification'),
    ('forgot_password', 'Forgot password'),
    ('successful_email_verification', 'Successful email verification'),
    ('successful_phone_verification', 'Successful phone verification'),
    ('successful_id_verification', 'Successful ID verification'),
    ('failed_id_verification', 'Failed ID verification'),
    ('successful_selfie_verification', 'Successful selfie verification'),
    ('failed_selfie_verification', 'Failed selfie verification'),
    ('gift_promotion', 'Gift promotion'),
    ('coin_price', 'Coin price'),
    ('successful_buying', 'Successful buying'),
    ('successful_selling', 'Successful selling'),
)

SMS_PURPOSE = Choices(
    ('phone_verification', 'Phone verification'),
)

NOTIFICATION_TARGET = Choices(
    ('user', 'User'),
    ('system', 'System'),
)

CACHE_KEY_CONFIG = 'system_config.{}'
CACHE_KEY_FEE = 'system_fee.{}'
CACHE_KEY_COUNTRY_DEFAULT = 'system_country_default.{}'
