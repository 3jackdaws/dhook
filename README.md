# dhook - CLI Discord Webhook Executor
This is a command line python3 script that allows for the execution of Discord webhooks.  Webhooks are a low effort way to post content to a channel in a discord server.  Webhooks must be set up per channel.  

# Requirements
* Python3
* A Valid Webhook URL

# Usage
`dhook -i <webhook id> -t <webhook token> [-n <name>] [-a <avatar url>] <message content>`

Discord webhook urls take this form:
`https://discordapp.com/api/webhooks/<webhook id>/<webhook token>`

# Recommendations
It's often a good idea to create abash script that contains relevant webhook information, so that it doesn't have to be passed to the dhook script manually every time.

## Example Script
This is an example script that would be used for notifications.  It's signature would be: `./notify.sh "My message content"`
```bash
#!/bin/bash
# notify.sh
HOOK_ID=12345678901234324
HOOK_TOKEN=HGSDHDFGHDFGH$%$^WEGXBVG$^^GH_)HMKCBDFG
HOOK_NAME='Alert Bot'
HOOK_AVATAR='http://pictures.com/picture'
MENTION='<@483094830948403948>'

dhook -i$HOOK_ID -t$HOOK_TOKEN -n"$HOOK_NAME" -a"$HOOK_AVATAR" "Alert for $MENTION: $1"
```




