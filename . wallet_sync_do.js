E:/name = "deep-echo-spell"
type = "javascript"

[[durable_objects.bindings]]
name = "WALLET_SYNC_DO"
class_name = "WalletSync"

[[migrations]]
tag = "v1"
new_classes = ["WalletSync"]

[build]
upload.format = "modules"
EchoVault/Cloudflare/Spells/wallet_sync_do.js