# message_senders
- テキストメッセージ配信ライブラリ
- Discord, LINE Notify, リモートホスト、ローカルファイル、標準出力

## 使用例

```python
from message_senders import DiscordSender, RemoteFileSender

discord_sender = DiscordSender(api_token='YOUR API TOKEN')
discord_sender.send('メッセージ')

remote_file_sender = RemoteFileSender(host='user@hostname', 
                                      remote_file_path='/path/to/remote/file')
remote_file_sender.send('ファイルの末尾にこのメッセージが追加されます')
```

## カスタムSenderの実装

```python
from message_senders import BaseSender

class StdOutSender(BaseSender):
    # OverRide
    def __init__(self, some):
        self.some_api_entry_point = 'www.example.com/post'

    # OverRide
    def send(self, text: str):
        API.post(self.some_api_entry_point, text)
```