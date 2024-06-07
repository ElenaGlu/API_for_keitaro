from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "affiliatenetwork" ADD "keitaro_network_id" INT NOT NULL  DEFAULT 0;
        ALTER TABLE "offer" ADD "keitaro_offer_id" INT NOT NULL  DEFAULT 0;
        ALTER TABLE "offer" DROP COLUMN "keitaro_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offer" ADD "keitaro_id" INT NOT NULL;
        ALTER TABLE "offer" DROP COLUMN "keitaro_offer_id";
        ALTER TABLE "affiliatenetwork" DROP COLUMN "keitaro_network_id";"""
