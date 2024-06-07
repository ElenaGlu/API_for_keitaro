from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "affiliatenetwork" ALTER COLUMN "keitaro_network_id" DROP NOT NULL;
        ALTER TABLE "offer" ALTER COLUMN "keitaro_offer_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "offer" ALTER COLUMN "keitaro_offer_id" SET NOT NULL;
        ALTER TABLE "affiliatenetwork" ALTER COLUMN "keitaro_network_id" SET NOT NULL;"""
