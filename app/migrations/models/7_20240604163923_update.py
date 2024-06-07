from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "affiliatenetwork" DROP COLUMN "notes";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "affiliatenetwork" ADD "notes" VARCHAR(256) NOT NULL;"""
