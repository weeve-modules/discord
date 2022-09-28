# Discord

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Discord                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/discord](https://hub.docker.com/r/weevenetwork/discord) |
| authors        | Jakub Grzelak                    |

- [Discord](#discord)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This modules sends messages and notifications to a selected Discord channel. It requires setting up a webhook integration for the Discord channel (see official [Discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)). Additionally, we recommend running this module together with our [Message Composer](https://github.com/weeve-modules/message-composer) module that helps in writing alerts within weeve Edge Application.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Webhook URL    | DISCORD_WEBHOOK_URL         | string   | Webhook URL of Discord channel where messages will be sent.            |
| Message Label    | MESSAGE_LABEL         | string  | Label in incoming data that holds the message to be sent.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
discordwebhook
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "alertMessage": "Device hf238hf23h7 (in Berlin) measured temperature 12 on 2022-09-25 15:35:17.31234"
}
```

## Output

Message send to the selected Discord channel. Given the above input, message will be `Device hf238hf23h7 (in Berlin) measured temperature 12 on 2022-09-25 15:35:17.31234`.
