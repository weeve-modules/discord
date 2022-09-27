"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from discordwebhook import Discord
import os

log = getLogger("module")

log.debug(f'Connecting to Discord client... Webhook URL: {os.getenv("DISCORD_WEBHOOK_URL")}')
client = Discord(url=os.getenv("DISCORD_WEBHOOK_URL"))
log.debug('Successfully connected to Discord client!')

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Sending data to Discord channel ...")

    try:
        # YOUR CODE HERE
        resp = client.post(content=received_data[os.getenv("MESSAGE_LABEL")])

        if resp.status_code != 204:
            return f"Error when sending data to Discord channel. Server response: {resp.status_code}, {resp.text}"

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
