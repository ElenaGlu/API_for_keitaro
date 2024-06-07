from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_affiliatene_name_0445b7" ON "affiliatenetwork" ("name");
        CREATE UNIQUE INDEX "uid_offer_name_9be477" ON "offer" ("name");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_affiliatene_name_0445b7";
        DROP INDEX "idx_offer_name_9be477";"""
