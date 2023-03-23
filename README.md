
# DisNotion
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

DisNotion is a python script that connects a Notion database to a Discord channel and sends simple notifications when changes are made to the database.


## Installation

Install packages

```python
  pip install -r requirements.txt
```


    
## Setup

- Create a notion integration and replace NotionIntegration with it in fileConf.txt

![IntegrationToken](https://raw.githubusercontent.com/davidpm-19/DisNotion/rmePics/notionKey.PNG)

- Connect the new integration to the database page

![Share Integration](https://raw.githubusercontent.com/davidpm-19/DisNotion/rmePics/notionInvite.PNG) 

- Copy the Database ID defined in the database page URL and replace DatabaseUrl with it in fileConf.txt

![url](https://raw.githubusercontent.com/davidpm-19/DisNotion/rmePics/url.PNG)

- Go to the Integrations Section in Discord Server Configuration Menu

![Discord Menu](https://raw.githubusercontent.com/davidpm-19/DisNotion/rmePics/discord%20main%20menu.PNG)

- Configure the channel, copy the Webhook URL and replace WebhookUrl with it in fileConf.txt

![Webhook](https://raw.githubusercontent.com/davidpm-19/DisNotion/rmePics/discord%20wh.PNG)


## Usage

As a Python Script designed to be always running, DisNotion just needs to be executed

If the script stops all variables will reset so the first check will consider every element in database as a changed one, so the script will work as expected in a server.

## Future Changes and Tools

This toll is still in development, the final version will include more tools, checks, a way to store data persistently, and optimitzation, please be patient while the rest of the features are developed.
