from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "affiliatenetwork" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "postback_url" VARCHAR(256) NOT NULL,
    "offer_param" VARCHAR(256) NOT NULL,
    "notes" VARCHAR(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS "offer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "group_id" INT NOT NULL,
    "offer_type" VARCHAR(256) NOT NULL  DEFAULT 'local',
    "action_type" VARCHAR(256) NOT NULL,
    "action_payload" VARCHAR(256) NOT NULL,
    "affiliate_network_id" INT NOT NULL,
    "payout_value" INT NOT NULL,
    "payout_currency" VARCHAR(256) NOT NULL,
    "payout_type" VARCHAR(3) NOT NULL,
    "state" VARCHAR(7) NOT NULL  DEFAULT 'active',
    "payout_auto" BOOL NOT NULL  DEFAULT False,
    "payout_upsell" BOOL NOT NULL  DEFAULT False,
    "country" VARCHAR(256) NOT NULL,
    "notes" VARCHAR(256) NOT NULL,
    "archive" VARCHAR(256) NOT NULL,
    "conversion_cap_enabled" BOOL NOT NULL  DEFAULT False,
    "daily_cap" INT NOT NULL,
    "conversion_timezone" VARCHAR(256) NOT NULL,
    "alternative_offer_id" INT NOT NULL
);
COMMENT ON COLUMN "offer"."payout_type" IS 'cpa: CPA\ncpc: CPC';
COMMENT ON COLUMN "offer"."state" IS 'active: active\ndeleted: deleted';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
