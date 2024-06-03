from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "affiliatenetwork" ALTER COLUMN "keitaro_network_id" DROP DEFAULT;
        ALTER TABLE "offer" ALTER COLUMN "keitaro_offer_id" DROP DEFAULT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offer" ALTER COLUMN "keitaro_offer_id" SET DEFAULT 0;
        ALTER TABLE "affiliatenetwork" ALTER COLUMN "keitaro_network_id" SET DEFAULT 0;"""
