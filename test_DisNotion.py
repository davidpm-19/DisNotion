import pytest


def test_notion_config_format(tmpdir):
    file = tmpdir.mkdir("mydir").join("myfile.txt")
    text = "Notion_Cli : NotionIntegration\nDatabase_ID : Database Id\nDiscord_Bot : Webhook Url"
    file.write(text)
    assert 'Notion_Cli : NotionIntegration' in file.read()


def test_db_config_format(tmpdir):
    file = tmpdir.mkdir("mydir").join("myfile.txt")
    text = "Notion_Cli : NotionIntegration\nDatabase_ID : Database Id\nDiscord_Bot : Webhook Url"
    file.write(text)
    assert 'Database_ID : Database Id' in file.read()


def test_discord_config_format(tmpdir):
    file = tmpdir.mkdir("mydir").join("myfile.txt")
    text = "Notion_Cli : NotionIntegration\nDatabase_ID : Database Id\nDiscord_Bot : Webhook Url"
    file.write(text)
    assert 'Discord_Bot : Webhook Url' in file.read()