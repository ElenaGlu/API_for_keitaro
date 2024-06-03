from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "affiliatenetwork" RENAME COLUMN "keitaro_network_id" TO "keitaro_id";
        ALTER TABLE "offer" RENAME COLUMN "keitaro_offer_id" TO "keitaro_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offer" RENAME COLUMN "keitaro_id" TO "keitaro_offer_id";
        ALTER TABLE "affiliatenetwork" RENAME COLUMN "keitaro_id" TO "keitaro_network_id";"""
