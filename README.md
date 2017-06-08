# ohMeiji_autologin_app
ohMeijiに自動ログインできるpython3。AlfredのWorkflowアプリ化

ログイン機能自体はpythonで完結しています。  
設定とかドライバのインストールの説明はたぶんまたやります。

Alfredのworkflowでは以下のように/bin/bashを記述してください。

```bash:workflow
cd 実行ファイルのあるパス
bash -l -c 'python3 oh_meiji_login.py'
```

# 動作

![2017-06-09 3 49 00](https://user-images.githubusercontent.com/17490886/26945447-b735f94a-4cc6-11e7-9d91-8decbc278dec.png)

この後、自動でブラウザ起動、ログイン行われる。

# 余談

- 自動でドライバとか足りない場合インストールできるようにしたい。
- セキュリティの問題が強いし、立ち上げに少し時間かかるから、applescriptかJAXで書き直したい。
- また、詰まったところを書く。
