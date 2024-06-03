from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offer" DROP COLUMN "alternative_offer_id";
        ALTER TABLE "offer" DROP COLUMN "payout_auto";
        ALTER TABLE "offer" DROP COLUMN "payout_value";
        ALTER TABLE "offer" DROP COLUMN "payout_upsell";
        ALTER TABLE "offer" DROP COLUMN "country";
        ALTER TABLE "offer" DROP COLUMN "notes";
        ALTER TABLE "offer" DROP COLUMN "conversion_timezone";
        ALTER TABLE "offer" DROP COLUMN "state";
        ALTER TABLE "offer" DROP COLUMN "archive";
        ALTER TABLE "offer" DROP COLUMN "conversion_cap_enabled";
        ALTER TABLE "offer" DROP COLUMN "daily_cap";
        ALTER TABLE "offer" DROP COLUMN "payout_currency";
        ALTER TABLE "offer" DROP COLUMN "group_id";
        ALTER TABLE "offer" DROP COLUMN "action_type";
        ALTER TABLE "offer" DROP COLUMN "payout_type";
        ALTER TABLE "offer" ADD CONSTRAINT "fk_offer_affiliat_72643f87" FOREIGN KEY ("affiliate_network_id") REFERENCES "affiliatenetwork" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offer" DROP CONSTRAINT "fk_offer_affiliat_72643f87";
        ALTER TABLE "offer" ADD "alternative_offer_id" INT NOT NULL;
        ALTER TABLE "offer" ADD "payout_auto" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "offer" ADD "payout_value" INT NOT NULL;
        ALTER TABLE "offer" ADD "payout_upsell" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "offer" ADD "country" VARCHAR(256) NOT NULL;
        ALTER TABLE "offer" ADD "notes" VARCHAR(256) NOT NULL;
        ALTER TABLE "offer" ADD "conversion_timezone" VARCHAR(256) NOT NULL;
        ALTER TABLE "offer" ADD "state" VARCHAR(7) NOT NULL  DEFAULT 'active';
        ALTER TABLE "offer" ADD "archive" VARCHAR(256) NOT NULL;
        ALTER TABLE "offer" ADD "conversion_cap_enabled" BOOL NOT NULL  DEFAULT False;
        ALTER TABLE "offer" ADD "daily_cap" INT NOT NULL;
        ALTER TABLE "offer" ADD "payout_currency" VARCHAR(256) NOT NULL;
        ALTER TABLE "offer" ADD "group_id" INT NOT NULL;
        ALTER TABLE "offer" ADD "action_type" VARCHAR(256) NOT NULL;
        ALTER TABLE "offer" ADD "payout_type" VARCHAR(3) NOT NULL;"""
