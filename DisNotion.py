import time
from notion_client import Client
from discord_webhook import DiscordWebhook


def conf_import():
    config = []
    with open('fileConf.txt', 'r') as f:
        for line in f:
            if line := line.strip():
                key, value = line.split(' : ')
                config.append(value)
    return config


def connection():
    # Notion connection
    notion = Client(auth=conf_list[0])
    database_id = conf_list[1]

    # Discord Webhook
    webhook_url = conf_list[2]
    webhook = DiscordWebhook(url=webhook_url)
    return notion, database_id, webhook


def discord_notion():
    notion, database_id, webhook = connection()
    # Query to get database elements
    results = notion.databases.query(
        **{
            "database_id": database_id,
        }
    ).get("results")
    for item in results:
        item_id = item["id"]
        last_edited_time = last_edited_times.get(item_id, "")
        # Control to check if element has changed
        if item["last_edited_time"] != last_edited_time:
            # Variables to notify
            entry_title = item["properties"]["CHANGE"]["title"][0]["text"]["content"]
            entry_property_1 = item["properties"]["CHANGE"]['select']["name"]
            entry_property_2 = item['properties']['CHANGE']['select']['name']
            message = f"Change this to the message you want to send"
            # Message sender
            webhook.content = message
            webhook.execute()
            # Update the values of dictionaries to the last ones
            last_edited_times[item_id] = item["last_edited_time"]

# Control dictionaries
last_edited_times = {}
conf_list = conf_import()
connection()
while True:
    discord_notion()
    time.sleep(3)

