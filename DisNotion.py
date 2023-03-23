import time
from notion_client import Client
from discord_webhook import DiscordWebhook


def conf_import():
    config = []
    with open('fileConf.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()  # remove any leading or trailing whitespace
        if line:  # check if the line is not empty
            key, value = line.split(' : ')
            config.append(value)
    return config


def connection():
    # Notion connection
    notion = Client(auth=conf_list[0])
    database_id = conf_list[1]

    # Discord Webhook
    webhook_url = conf_list[2]  # Replace this with the URL of your Discord webhook
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
        last_edited_status = last_edited_statuses.get(item_id, "")
        # Control to check if element has changed
        if item["last_edited_time"] != last_edited_time:
            # Variables to notify
            entry_sprint = item["properties"]["Sprint"]['select']["name"]
            entry_project = item["properties"]["Projects"]["title"][0]["text"]["content"]
            entry_status = item['properties']['Status']['select']['name']
            # Inner control to check if task has changed it status or has been completed
            if entry_status != last_edited_status:
                if entry_status == "Complete 🙌":
                    message = "La tarea: " + entry_project + " del " + entry_sprint + " ha sido completada"
                else:
                    message = "La tarea: " + entry_project + " del " + entry_sprint + " ha cambiado de: " + last_edited_status + " a: " + entry_status
            else:
                message = "La tarea: " + entry_project + " del " + entry_sprint + " ha sido modificada"
            # Message sender
            webhook.content = message
            response = webhook.execute()
            # Update the values of dictionaries to the last ones
            last_edited_times[item_id] = item["last_edited_time"]
            last_edited_statuses[item_id] = entry_status


# Control dictionaries
last_edited_times = {}
last_edited_statuses = {}

conf_list = conf_import()
connection()
while True:
    discord_notion()
    time.sleep(10)
